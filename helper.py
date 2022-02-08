import pandas as pd
import json
from sqlalchemy import create_engine


with open('cotacao_dolar.json') as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data['value'])
print(df)

df.info()

con = create_engine("mysql+mysqldb://root:"+'brasil01'+"@127.0.0.1/comandadigital2")

df.to_sql(con=con, name='cad_moeda_cotacao_valor', if_exists='replace')