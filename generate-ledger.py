import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Realistic Sidi Ghanem Client Names
clients = [
    "Menara Logistics", "Atlas Manufacturing", "Sidi Ghanem Textiles", 
    "Marrakech Express", "BatiSud SARL", "TechNord Maroc", "AutoParts Kech"
]

statuses = ["Payée", "Impayée", "En cours"]

# 2. Generate 100 fake invoices
data = []
for i in range(1, 101):
    client = random.choice(clients)
    invoice_num = f"FAC-2026-{i:03d}"  # Creates FAC-2026-001, etc.
    amount = round(random.uniform(1500.0, 25000.0), 2)
    status = random.choices(statuses, weights=[50, 30, 20])[0] # 30% chance of being unpaid
    
    # Generate a random date from the last 60 days
    days_ago = random.randint(1, 60)
    date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    data.append([invoice_num, client, date, amount, status])

# 3. Use Pandas to turn our list into a DataFrame
df = pd.DataFrame(data, columns=["N° Facture", "Client", "Date", "Montant (DH)", "Statut"])

# 4. Save it as a real Excel file!
# index=False means we don't save those 0,1,2,3 row numbers to the Excel sheet
df.to_excel("comptabilite.xlsx", index=False)

print("✅ Fichier 'comptabilite.xlsx' généré avec succès avec 100 factures !")