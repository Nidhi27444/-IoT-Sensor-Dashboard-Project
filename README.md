
# 🌍 IoT Sensor Dashboard Project – Power BI + Streamlit

This project demonstrates a real-world **data dashboard system** for IoT sensor data, originally generated from simulated or real devices (I2C, SPI, BLE, Wi-Fi). It showcases both **no-code (Power BI)** and **code-first (Streamlit)** approaches — ideal for field monitoring operational use cases.

---

## 🔧 Data Flow Overview

```
Simulated Sensors (Python/Wokwi)
        ↓
JSON Output → MongoDB (via Docker)
        ↓
Unified JSON → Cleaned CSV
        ↓
📊 Power BI | 🧪 Streamlit Dashboard
```

---

## 📊 Power BI Report Highlights

- Connected to cleaned `.csv` from MongoDB
- Interactive filters for:
  - Temperature
  - Time window
  - TempStatus (Normal/High)
- Visuals:
  - Line chart (Temp vs Time)
  - Bar chart (Status distribution)
  - Slicers + Raw table view

📎 Used by: **Non-technical users / operations teams**

---

## 🧪 Streamlit Dashboard Highlights

- Built using Python, Streamlit, Pandas, and Plotly
- Loads the same CSV from MongoDB JSON pipeline
- Features:
  - Sidebar filters (temp, pressure)
  - Live plots: Temp, Pressure, Humidity, AQI
  - Stats view (`df.describe()`)

🎯 Ideal for: **Developers / engineers / cloud deployments**

---

## 🗂 Files Included

| File | Purpose |
|------|---------|
| `cleaned_sensor_data.csv` | Cleaned, flattened sensor data |
| `streamlit_sensor_dashboard.py` | Streamlit app script |
| `PowerBI_Report.pbix` | Optional Power BI file |
| `README_UNDP_Dashboard.md` | This explanation |

---

## 🌐 Why This Project Matters
 
- Demonstrates end-to-end data pipeline handling — from raw JSON to structured insights
- Combines technical (Streamlit) and non-technical (Power BI) tools to serve diverse user needs
- Simulates a field-ready dashboard for real-time sensor or energy data monitoring
- Built entirely using free, open-source, and student-accessible technologies
  
---

## 🚀 To Run Streamlit App

```bash
pip install streamlit pandas plotly
streamlit run streamlit_sensor_dashboard.py
```

---

## 📍 Future Enhancements

- MQTT/real-time data streaming
- Power Automate (alerts)
- Web deployment (Streamlit Cloud)
- Google Sheets/SharePoint sync

---

## 📬 Author

👩‍💻 Nidhi Shah  
📧 nidhijshah95@gmail.com
🎓 Master's in Computer Engineering for IoT Systems  
🏢 Hochschule Nordhausen 
