import csv
import gspread
import time

month = "january"

file =f"Inter_{month}.csv"

Lanchonete_nomes = ["Alimentação", {"FRANCISCO CELIO", "Carla Ranielly de Lima", "ACAIDARANNYAVENIDA", "CANTINA", "NATALINE PINHEIRO"}]
Supermercado_nomes = ["Supermercado", {"Supermercado", "super lua", "SAMIA CARLA P SOUSA"}]
Dentista_nomes = ["Dentista", {"Dentista"}]
Onibus_nomes = ["Ônibus", {"MANDACARU"}]
Lavagens_nomes = ["Lavagens", {"Nerivaldo", "Lava Jato"}]
Combustivel_nomes = ["Combustível", {"Posto", "Petro Super"}]
Corte_nomes = ["Cabeleireiro", {"CARLOS ANTONIO DA SILVA MONTEIRO", "Sara da Silva"}]
Vest_nomes = ["Vestuário", {"Renner", "Zara", "Insider", "Shein", "MARTA CLEIDE"}]
Acad_nomes = ["Academia", {"DAVI ALMEIDA PORTO"}]
Restaurantes_nomes = ["Restaurantes", {"Camarada", "ORDONES", "Gilson Paulo"}]
Lazer_nomes = ["Cafés, bares e boates", {"AustinPub", "Seu Domingo", "Pub", "Boteco", "Matuto"}]
INVEST_NAMES = ["CDB Mais Limite", {"APLICACAO", "CDB"}]

categorys = [Lanchonete_nomes, Supermercado_nomes, Dentista_nomes, Onibus_nomes, Lavagens_nomes, Combustivel_nomes, Corte_nomes, Vest_nomes, Acad_nomes, Restaurantes_nomes, Lazer_nomes, INVEST_NAMES]

def test_category(description, cat):
    for string in cat[1]:
        
        if string.upper() in description.upper():
            return cat[0]
        else:
            pass
    return "Classificar"



transactions = []
def InterFin(file, categorys):
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
                for cat in categorys:
                    category = test_category(description, cat)
                    if category != "Classificar":
                        break

            transaction = ((date, description, value, category))
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{month}")

rows = InterFin(file, categorys)

for row in rows:
    wks.insert_row([row[0],row[1],row[3],"",row[2]], 8)
    time.sleep(2)