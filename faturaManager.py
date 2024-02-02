import csv
import gspread
import time

month = "january"
banco = "Nubank"

file =f"Fatura{banco}_{month}.csv"

TRANSPORT_NAMES = {"99app *99app"}
SIGNATURES_NAMES = {"Apple.Com/Bill", "Mp *Melimais", "Claro*98985449980", "IANA KEMILY CRUZ LIMA", "Amazonprimebr"}
EDUCATION_NAMES = {"Htm*Reservatorio", "Htm*Comsobral"}
HEALTH_NAMES = {"Clinica*Smilecenter e"}
BUYINGS_NAMES = {"Renner"}

transactions = []
def NuFaturaFin(file):
    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            description = row[2]
            value = -1 * float(row[3])
            category = "other"
            # add here ways of discovering the category of the transaction by its description
            if description in TRANSPORT_NAMES:
                category = "Transporte"
            elif description in SIGNATURES_NAMES:
                category = "Assinaturas"
            elif description in EDUCATION_NAMES:
                category = "Educação"
            elif description in HEALTH_NAMES:
                category = "Saúde"
            elif description in BUYINGS_NAMES:
                category = "Compras"

            transaction = ((date, description, value, category))
            transactions.append(transaction)
        return transactions

def InterFaturaFin(file):
    return

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{month}")

rows = NuFaturaFin(file)

for row in rows:
    wks.insert_row([row[0],row[1],"",row[3],row[2]], 8)
    time.sleep(2)