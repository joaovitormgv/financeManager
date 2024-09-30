import csv
import gspread
import time
from collections import namedtuple
from script import formate_csv
from dotenv import load_dotenv
import os

load_dotenv()
month = os.getenv("MONTH")
file = f"Inter_{month}.csv"


input_file = f"/Users/joaovitormesquita/Desktop/Workspace/financeManager/input.csv"
output_file = f"/Users/joaovitormesquita/Desktop/Workspace/financeManager/{file}"

Category = namedtuple('Category', ['name', 'keywords'])

categories = [
    Category("Lanchonete", {"FRANCISCO CELIO", "Carla Ranielly de Lima", "ACAIDARANNYAVENIDA", "CANTINA", "NATALINE PINHEIRO"}),
    Category("Supermercado", {"Supermercado", "super lua", "SAMIA CARLA P SOUSA", "CENTERBOX"}),
    Category("Dentista", {"Dentista"}),
    Category("Ônibus", {"MANDACARU"}),
    Category("Uber/99", {"No estabelecimento 99 *"}),
    Category("Lavagens", {"Nerivaldo", "Lava Jato"}),
    Category("Combustível", {"Posto", "Petro Super"}),
    Category("Cabeleireiro", {"CARLOS ANTONIO DA SILVA MONTEIRO", "Sara da Silva"}),
    Category("Vestuário", {"Renner", "Zara", "Insider", "Shein", "MARTA CLEIDE"}),
    Category("Academia", {"DAVI ALMEIDA PORTO"}),
    Category("Restaurantes", {"Camarada", "ORDONES", "Gilson Paulo"}),
    Category("Cafés, bares e boates", {"AustinPub", "Seu Domingo", "Pub", "Boteco", "Matuto"}),
    Category("Almoço", {"CLEIDE PEREIRA BACURY"}),
    Category("CDB Mais Limite", {"APLICACAO", "CDB"})
]


def test_category(description, category):
    for string in category.keywords:
        
        if string.upper() in description.upper():
            return category.name
        else:
            pass
    return "Classificar"



transactions = []
def InterFin(file, categories):
    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            description = row[1]
            value = float(row[2])
            category = "Classificar"
            # add here ways of discovering the category of the transaction by its description
            if "WELLERSON" in description:
                category = "Empréstimos"
            elif "FATURA" in description:
                pass
            elif "Levy" in description and value == -20:
                category = "Renda 1"
            elif "JOAO VORCEI GONCALVES GOUVEA" in description:
                category = "Renda 2"
            else:
                for cat in categories:
                    category = test_category(description, cat)
                    if category != "Classificar":
                        break

            transaction = (date, description, value, category)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{month}")

formate_csv(input_file, output_file)

rows = InterFin(file, categories)

# Inicializa a variável para rastrear a última linha inserida
last_row = len(wks.get_all_values()) + 1

# Lidar com o formato da minha tabela
if last_row <= 8:
    last_row = 8

for row in rows:
    wks.insert_row([row[0], row[1], row[3], "", row[2]], last_row)
    last_row += 1
    time.sleep(1.5)
