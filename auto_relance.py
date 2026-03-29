import pandas as pd
from fpdf import FPDF
import os

# 1. Create a clean folder to hold the generated PDFs
if not os.path.exists("Output_PDFs"):
    os.makedirs("Output_PDFs")

# 2. Load our generated accounting ledger
print("📥 Chargement de la base de donnees Excel...")
df = pd.read_excel("comptabilite.xlsx")

# 3. Filter for clients who OWE money (Impayée)
impayees_df = df[df["Statut"] == "Impayée"]
clients_endettes = impayees_df["Client"].unique()

print(f"🚨 {len(clients_endettes)} clients detectes avec des impayes. Generation des releves...\n")

# 4. The Automation Loop
for client in clients_endettes:
    # Isolate this specific client's data
    client_data = impayees_df[impayees_df["Client"] == client]
    
    # Calculate their total debt
    total_dette = client_data["Montant (DH)"].sum()
    
    # --- START DRAWING THE PDF ---
    pdf = FPDF()
    pdf.add_page()
    
    # Set Font (Arial, Bold, Size 16)
    pdf.set_font("Arial", "B", 16)
    
    # Add Title
    pdf.cell(200, 10, txt="RELEVE DE COMPTE - RAPPEL DE PAIEMENT", ln=True, align="C")
    pdf.ln(10) # Add a blank line
    
    # Add Client Info & Total Debt
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, txt=f"Client : {client}", ln=True)
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, txt=f"Total a regler : {total_dette:,.2f} DH", ln=True)
    pdf.ln(10)
    
    # --- DRAW THE INVOICE TABLE ---
    # Table Header
    pdf.set_font("Arial", "B", 10)
    pdf.cell(50, 10, "N Facture", border=1, align="C")
    pdf.cell(50, 10, "Date", border=1, align="C")
    pdf.cell(50, 10, "Montant (DH)", border=1, ln=True, align="C")
    
    # Table Rows (Using a loop inside our loop to print each invoice)
    pdf.set_font("Arial", "", 10)
    for index, row in client_data.iterrows():
        pdf.cell(50, 10, str(row["N° Facture"]), border=1, align="C")
        pdf.cell(50, 10, str(row["Date"]), border=1, align="C")
        pdf.cell(50, 10, f"{row['Montant (DH)']:,.2f}", border=1, ln=True, align="R")
        
    # --- SAVE THE PDF ---
    # Replace spaces with underscores so the file name is clean
    safe_filename = client.replace(" ", "_")
    pdf.output(f"Output_PDFs/Relance_{safe_filename}.pdf")
    
    print(f"✅ Document genere : Relance_{safe_filename}.pdf ({total_dette:,.2f} DH)")

print("\n🎉 Termine ! Ouvrez le dossier 'Output_PDFs' pour voir le resultat.")