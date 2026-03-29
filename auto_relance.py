import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from fpdf import FPDF

# ==========================================
# ✉️ THE EMAIL ENGINE (SIMULATION MODE)
# ==========================================
def envoyer_email(client_nom, montant, fichier_pdf):
    # This is exactly how the real email is built
    msg = EmailMessage()
    msg['Subject'] = f"URGENT : Relevé de compte - {client_nom}"
    msg['From'] = "votre-entreprise@factory.com"
    msg['To'] = f"comptabilite@{client_nom.replace(' ', '').lower()}.com"
    
    contenu = f"""
    Bonjour l'équipe {client_nom},
    
    Sauf erreur ou omission de notre part, nous constatons qu'un montant total de {montant:,.2f} DH reste impayé sur votre compte.
    Vous trouverez en pièce jointe le détail de vos factures.
    
    Merci de procéder au règlement dans les plus brefs délais.
    
    Cordialement,
    Le Département Financier
    """
    msg.set_content(contenu)
    
    # Simulate attaching the PDF and sending
    print(f"   [SIMULATION EMAIL] 📧 Préparation de l'email pour {msg['To']}...")
    print(f"   [SIMULATION EMAIL] 📎 Pièce jointe attachée : {fichier_pdf}")
    print(f"   [SIMULATION EMAIL] 🚀 EMAIL ENVOYÉ !\n")
    
    # 💡 When you want to send REAL emails, you just uncomment this block:
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.login("votre_email@gmail.com", "votre_mot_de_passe_app")
    # server.send_message(msg)
    # server.quit()

# ==========================================
# 📄 THE PDF & DATA PIPELINE
# ==========================================
if not os.path.exists("Output_PDFs"):
    os.makedirs("Output_PDFs")

print("📥 Chargement de la base de données Excel...")
df = pd.read_excel("comptabilite.xlsx")

impayees_df = df[df["Statut"] == "Impayée"]
clients_endettes = impayees_df["Client"].unique()

print(f"🚨 {len(clients_endettes)} clients avec impayés. Lancement du robot de relance...\n")

for client in clients_endettes:
    client_data = impayees_df[impayees_df["Client"] == client]
    total_dette = client_data["Montant (DH)"].sum()
    
    # --- 1. DRAW PDF ---
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="RELEVE DE COMPTE - RAPPEL DE PAIEMENT", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 8, txt=f"Client : {client}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 8, txt=f"Total à régler : {total_dette:,.2f} DH", ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 10)
    pdf.cell(50, 10, "N Facture", border=1, align="C")
    pdf.cell(50, 10, "Date", border=1, align="C")
    pdf.cell(50, 10, "Montant (DH)", border=1, ln=True, align="C")
    
    pdf.set_font("Arial", "", 10)
    for index, row in client_data.iterrows():
        pdf.cell(50, 10, str(row["N° Facture"]), border=1, align="C")
        pdf.cell(50, 10, str(row["Date"]), border=1, align="C")
        pdf.cell(50, 10, f"{row['Montant (DH)']:,.2f}", border=1, ln=True, align="R")
        
    safe_filename = client.replace(" ", "_")
    pdf_path = f"Output_PDFs/Relance_{safe_filename}.pdf"
    pdf.output(pdf_path)
    print(f"✅ Document généré : {pdf_path}")
    
    # --- 2. TRIGGER THE EMAIL ENGINE ---
    envoyer_email(client, total_dette, pdf_path)

print("🎉 Processus de facturation et de relance terminé !")