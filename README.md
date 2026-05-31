# Tech-Interactives Military Grade Radar System

**WiFi CSI-Based Human Detection and Localization Platform**

**Created by: Tech-Interactives**  
**Founder: Akhilesh TU**

---

## 🎯 System Overview

The Tech-Interactives Military Grade Radar System is a production-grade WiFi CSI (Channel State Information) based human sensing platform that provides real-time presence detection, motion tracking, localization, and advanced signal analysis.

### Current Topology
```
             Router (2.4GHz)
                ▲
               / \
              /   \
             /     \
            /       \
       ESP32-1   ESP32-2
       (RX-1)    (RX-2)
```

### Future Expandable Topology
```
             Router
                ▲
            /   |   \
           /    |    \
       RX-1   RX-2   RX-3
                |
               RX-4
                |
               RX-5
```

---

## ✨ Core Features

### Detection & Sensing
- ✅ **Presence Detection** - Real-time human presence
- ✅ **Motion Detection** - Movement identification
- ✅ **Zone Detection** - Multi-zone occupancy mapping
- ✅ **Human Localization** - XY/XYZ position estimation
- ✅ **Multi-Zone Tracking** - Simultaneous tracking
- ✅ **Person Counting** - Occupancy estimation
- ✅ **Breathing Detection** - Cardiopulmonary analysis
- ✅ **Direction Detection** - Movement vector analysis

### System Management
- ✅ **Receiver Health Monitoring**
- ✅ **Network Diagnostics**
- ✅ **Calibration System**
- ✅ **OTA Updates**
- ✅ **Data Logging**

### Visualization & Control
- ✅ **3D Dashboard** - Real-time Three.js visualization
- ✅ **Signal Dome** - CSI heatmap visualization
- ✅ **Zone Mapping** - Dynamic grid display
- ✅ **Real-Time Analytics** - Live metrics and statistics
- ✅ **Desktop Application** - PySide6 native Windows app

### AI & ML Ready
- ✅ **ONNX Model Support** - Plug-and-play AI models
- ✅ **Custom Model Framework** - Train and deploy custom models
- ✅ **Future Extensions** - Pose estimation, fall detection

---

## 📋 System Requirements

### Hardware
- **Router**: 802.11n/ac with 2.4GHz band
- **Receivers**: ESP32-WROOM-32 Dev Kit (minimum 2)
- **Connectivity**: WiFi connection for backend

### Software (Windows 11)
- **Python**: 3.14 or later
- **USB Drivers**: CH340 or CP2102

### Network
- **Bandwidth**: 5 Mbps minimum per receiver
- **Latency**: < 100ms recommended

---

## 🚀 Quick Start

```bash
# 1. Install
.\install.bat

# 2. Flash ESP32
.\flash_tx.bat    # TX board
.\flash_rx.bat    # RX board

# 3. Configure
# Edit: backend/config/network_config.json

# 4. Run
.\start_all.bat
```

---

## 📁 Complete Repository Structure

```
radar-syste-/
├── firmware/
│   ├── tx/
│   │   └── esp32_tx.ino
│   ├── rx/
│   │   └── esp32_rx.ino
│   └── shared/
│       ├── config.h
│       ├── wifi_manager.h
│       ├── wifi_manager.cpp
│       ├── csi_manager.h
│       ├── csi_manager.cpp
│       ├── packet_protocol.h
│       ├── packet_protocol.cpp
│       ├── network_manager.h
│       ├── network_manager.cpp
│       ├── device_info.h
│       ├── device_info.cpp
│       ├── diagnostics.h
│       ├── diagnostics.cpp
│       ├── ota_update.h
│       └── ota_update.cpp
│
├── backend/
│   ├── csi_reader.py
│   ├── signal_processor.py
│   ├── presence_detector.py
│   ├── motion_detector.py
│   ├── localization_engine.py
│   ├── person_counter.py
│   ├── tracking_engine.py
│   ├── breathing_detector.py
│   ├── receiver_manager.py
│   ├── router_manager.py
│   ├── network_manager.py
│   ├── settings_manager.py
│   ├── diagnostics.py
│   ├── data_logger.py
│   ├── api_server.py
│   ├── websocket_server.py
│   ├── main.py
│   ├── config/
│   │   ├── network_config.json
│   │   ├── detection_config.json
│   │   ├── localization_config.json
│   │   └── ui_config.json
│   ├── models/
│   └── logs/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   ├── dashboard.js
│   ├── three_scene.js
│   ├── websocket_client.js
│   ├── settings_panel.js
│   ├── zone_map.js
│   ├── human_tracker.js
│   └── assets/
│
├── desktop/
│   ├── main.py
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── dashboard_widget.py
│   │   ├── settings_widget.py
│   │   └── diagnostics_widget.py
│   └── config/
│
├── scripts/
│   ├── install.bat
│   ├── setup.ps1
│   ├── run_backend.bat
│   ├── run_dashboard.bat
│   ├── start_all.bat
│   ├── flash_tx.bat
│   ├── flash_rx.bat
│   ├── verify_installation.py
│   └── create_venv.bat
│
├── docs/
│   ├── INSTALL.md
│   ├── HARDWARE_SETUP.md
│   ├── NETWORK_SETUP.md
│   ├── CALIBRATION_GUIDE.md
│   ├── UPGRADE_GUIDE.md
│   ├── API_REFERENCE.md
│   ├── DEVELOPER_GUIDE.md
│   ├── TROUBLESHOOTING.md
│   └── FAQ.md
│
├── tests/
│   ├── test_signal_processor.py
│   ├── test_localization.py
│   ├── test_api.py
│   └── test_websocket.py
│
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── .env.example
└── LICENSE
```

---

## 📞 Support

- See `docs/FAQ.md` for common questions
- Review `docs/TROUBLESHOOTING.md` for solutions
- Contact Tech-Interactives support

---

**Tech-Interactives Military Grade Radar System**  
**Version**: 1.0.0 | **Status**: Production Ready  
**Created by**: Tech-Interactives | **Founder**: Akhilesh TU
