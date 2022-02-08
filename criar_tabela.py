#
# #### CONECTAR COM A BASE DE DADOS E CRIAR A TABELA ####
# import mysql.connector
#
# comandadigital_db = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="brasil01",
#     database="comandadigital2",
# )
#
# meu_cursor = comandadigital_db.cursor()
#
# meu_cursor.execute("CREATE TABLE cad_moeda_cotacao_valor "
#                    "("
#                    "id INT UNSIGNED AUTO_INCREMENT COMMENT 'ID unico' PRIMARY KEY,"
#                    "moeda_cotacao_id INT UNSIGNED NOT NULL COMMENT 'FK indice de mercado',"
#                    "data DATE DEFAULT NULL COMMENT 'Data do valor para o indice de mercado: dia(aaaa-mm-dd) | mes(aaaa-mm-01) | ano (aaaa-01-01)',"
#                    "abrangencia_tempo CHAR(2) NULL COMMENT 'DD. dia, DM.mês, DA.ano., DE.especial',"
#                    "valor DECIMAL(17, 6) NULL COMMENT 'valor indice para a data',"
#                    "status TINYINT UNSIGNED DEFAULT '1' NOT NULL COMMENT '1.Ativo 0.inativo - status de consideração do registro',"
#                    "criacao DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT 'Data inclusao do registro',"
#                    "atualizacao DATETIME DEFAULT NULL COMMENT 'Data ultima atualizacao',"
#                    "proprietario_id INT UNSIGNED NULL COMMENT'Grupo proprietario de todos os dados - saas'"
#                    ")")
#
# meu_cursor.execute("SHOW TABLES")

### INSERIR DADOS EM JSON NO BANCO DE DADOS ###

# for tabela in meu_cursor:
#     print(tabela)

import json

json_dolar = open('cotacao_dolar.json')


data = json.load(json_dolar)

for j in data['value']:
  print(j)

json_dolar.close()

