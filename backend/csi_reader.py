"""
Tech-Interactives Military Grade Radar System
CSI Reader Module - Acquires real-time CSI data from receivers
Founder: Akhilesh TU
"""

import socket
import json
import struct
import threading
import queue
from datetime import datetime
import logging

class CSIReader:
    def __init__(self, config_path='backend/config/network_config.json'):
        self.config = self._load_config(config_path)
        self.logger = logging.getLogger(__name__)
        self.csi_data_queue = queue.Queue(maxsize=1000)
        self.receivers = {}
        self.running = False
        self.lock = threading.Lock()
        
    def _load_config(self, config_path):
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            return {}
    
    def start_listening(self, port=5000):
        """Start listening for CSI data from ESP32 receivers"""
        self.running = True
        listener_thread = threading.Thread(target=self._listen_loop, args=(port,), daemon=True)
        listener_thread.start()
        self.logger.info(f"CSI Reader listening on port {port}")
    
    def _listen_loop(self, port):
        """Main listening loop"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(5)
        server_socket.settimeout(1.0)
        
        self.logger.info(f"CSI Reader socket listening on 0.0.0.0:{port}")
        
        while self.running:
            try:
                client_socket, address = server_socket.accept()
                handler_thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, address),
                    daemon=True
                )
                handler_thread.start()
            except socket.timeout:
                continue
            except Exception as e:
                self.logger.error(f"Listener error: {e}")
        
        server_socket.close()
    
    def _handle_client(self, client_socket, address):
        """Handle incoming data from a receiver"""
        device_id = None
        try:
            with client_socket:
                buffer = ""
                while self.running:
                    data = client_socket.recv(1024).decode('utf-8', errors='ignore')
                    if not data:
                        break
                    
                    buffer += data
                    lines = buffer.split('\n')
                    buffer = lines[-1]
                    
                    for line in lines[:-1]:
                        try:
                            json_data = json.loads(line)
                            device_id = json_data.get('device_id', 'unknown')
                            
                            with self.lock:
                                if device_id not in self.receivers:
                                    self.receivers[device_id] = {
                                        'address': address,
                                        'connected_at': datetime.now(),
                                        'last_data': datetime.now(),
                                        'sample_count': 0
                                    }
                                self.receivers[device_id]['last_data'] = datetime.now()
                                self.receivers[device_id]['sample_count'] += 1
                            
                            # Add to queue
                            try:
                                self.csi_data_queue.put_nowait(json_data)
                            except queue.Full:
                                self.csi_data_queue.get()
                                self.csi_data_queue.put(json_data)
                            
                            self.logger.debug(f"CSI data from {device_id}: RSSI={json_data.get('rssi')}")
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            self.logger.error(f"Client handler error for {address}: {e}")
    
    def get_latest_csi(self):
        """Get latest CSI data from queue"""
        try:
            return self.csi_data_queue.get_nowait()
        except queue.Empty:
            return None
    
    def get_receiver_count(self):
        """Get number of connected receivers"""
        with self.lock:
            return len(self.receivers)
    
    def get_receiver_status(self):
        """Get status of all receivers"""
        with self.lock:
            return dict(self.receivers)
    
    def stop(self):
        """Stop CSI reader"""
        self.running = False
        self.logger.info("CSI Reader stopped")
