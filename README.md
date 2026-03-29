# 📦 Smart Warehouse Scanner (Mobile-to-Cloud)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white) 
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

## 📋 Overview
The **Smart Warehouse Scanner** is a lightweight, mobile-friendly web application designed for factory floor workers. It eliminates paper-based inventory tracking by turning any standard smartphone into an enterprise-grade barcode and QR code scanner.

Instead of buying expensive proprietary hardware, workers simply open a local web link on their phones, scan a product, enter the quantity, and the system instantly updates the master centralized database (Excel/SQL) in real-time.

## 🚀 Key Features
* **📱 Bring Your Own Device (BYOD):** Runs entirely in the smartphone's web browser via Streamlit. No app store installation required.
* **📷 Real-Time Computer Vision:** Utilizes `pyzbar` and `OpenCV` to instantly decode barcodes and QR codes from the device's live camera feed.
* **⚡ Instant Synchronization:** Eliminates end-of-day data entry. When a worker taps "Update," the central inventory ledger is updated in milliseconds.
* **👷 Worker-Proof UI:** Designed for high-speed industrial environments. Large buttons, dark mode compatibility, and zero complex menus.

## 🛠️ Technical Stack
* **Frontend/Backend Engine:** Streamlit (Python)
* **Computer Vision:** OpenCV (`opencv-python-headless`) & PyZbar
* **Data Management:** Pandas & Openpyxl
* **Networking:** Local Area Network (LAN) binding for mobile access

## 📂 Project Structure
| File | Description |
| :--- | :--- |
| `app.py` | The main Streamlit web application and UI layout. |
| `scanner_engine.py` | The backend logic for decoding images and reading barcodes. |
| `database.py` | Handles reading and writing to the master `inventory.xlsx` file. |
| `inventory.xlsx` | The simulated master ledger containing stock levels. |
| `requirements.txt` | Python dependencies. |

## ⚙️ Setup & Installation

### 1. Initialize the Environment
```bash
git clone https://github.com/El-walid/smart-warehouse-scanner.git
cd smart-warehouse-scanner
python3 -m venv venv
source venv/bin/activate
```

### 2. Install System Dependencies
*Note: PyZbar requires the ZBar library to be installed on your operating system.*
* **Ubuntu/WSL:** `sudo apt-get install libzbar0`
* **Windows/Mac:** Automatically handled via pip in most environments.

### 3. Install Python Libraries
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ How to Run & Demo on Mobile

To demo this software to a client, you need to host it on your laptop and access it via your smartphone on the same Wi-Fi network.

**1. Start the Server**
Run the Streamlit app and bind it to your local network:
```bash
streamlit run app.py --server.address 0.0.0.0
```

**2. Access via Smartphone**
* The terminal will output a **Network URL** (e.g., `http://192.168.1.15:8501`).
* Open Safari or Chrome on your phone.
* Type that exact IP address into the search bar.
* Grant camera permissions, point your phone at a barcode, and watch the master ledger update on your laptop screen!

## 👨‍💻 Author
**El Walid El Alaoui Fels**
*Data Engineer | Automation Specialist*
