# 💰 Automated Debt Collector (Le Relanceur Automatique)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white) 
![PDF](https://img.shields.io/badge/FPDF-Document_Gen-darkred?style=for-the-badge)

## 📋 Overview
The **Automated Debt Collector** is a financial automation pipeline built for B2B logistics and manufacturing companies. 

Managing unpaid invoices at the end of the month is traditionally a slow, manual process prone to human error. This tool acts as a "Digital Accountant." It scans a master accounting ledger (Excel), instantly identifies clients with outstanding balances, generates highly professional PDF account statements, and dispatches targeted email reminders—reducing a 3-day accounting task to a 5-second script.

## 🚀 Key Features
* **🧠 Smart Ledger Parsing:** Utilizes Pandas to ingest massive Excel files and filter clients based on payment status (`Impayée`).
* **📄 Automated PDF Generation:** Uses the FPDF library to dynamically draw clean, printable "Relevé de Compte" (Statement of Account) tables for each indebted client.
* **✉️ Email Dispatch Engine:** Features a built-in SMTP module to automatically attach the correct PDF and send a customized reminder email to the specific client's accounting department.
* **🛡️ Local Execution:** Processes sensitive financial data entirely locally, ensuring zero data leakage to third-party cloud services.

## 🛠️ Technical Stack
* **Language:** Python 3.12
* **Data Engine:** Pandas & Openpyxl
* **Document Engine:** FPDF
* **Automation:** Standard Python `os` and `smtplib`

## 📂 Project Structure
| File | Description |
| :--- | :--- |
| `auto_relance.py` | The core engine: reads data, draws PDFs, and triggers the email pipeline. |
| `generate_ledger.py` | A script to create a randomized `comptabilite.xlsx` ledger with Moroccan market data for safe testing. |
| `comptabilite.xlsx` | The master Excel ledger (generated for testing). |
| `Output_PDFs/` | The destination folder where generated PDF statements are saved. |
| `.gitignore` | Ensures generated PDFs and secure `.env` files stay off public repositories. |

## ⚙️ Setup & Installation

### 1. Initialize the Environment
```bash
git clone https://github.com/El-walid/automated-debt-collector.git
cd automated-debt-collector
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install pandas fpdf openpyxl
```

## 🏃‍♂️ How to Run & Demo

**Step 1: Generate Mock Data**
If you are testing the system, generate a fresh ledger of 100 simulated B2B invoices.
```bash
python generate_ledger.py
```

**Step 2: Run the Relance Pipeline**
Execute the master script. The terminal will show the AI identifying debtors, generating the PDFs, and simulating the email dispatch.
```bash
python auto_relance.py
```
*Check the `Output_PDFs/` directory to view the generated financial statements!*

## 👨‍💻 Author
**El Walid El Alaoui Fels**

*Data Engineer | Automation Specialist*

***