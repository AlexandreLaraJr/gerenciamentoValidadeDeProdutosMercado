import pandas as pd
from scrapping.bolachas import getBolachas
from scrapping.chocolates import getChocolates
from scrapping.salgadinhos import getSalgadinhos


df_bolachas = getBolachas()
df_chocolates = getChocolates()
df_salgadinhos = getSalgadinhos()

df_produtos = pd.concat([df_bolachas, df_chocolates, df_salgadinhos], ignore_index=True)

print(df_produtos)

df_produtos.to_csv('produtos.csv', index=False, encoding='utf-8')

print("Arquivo CSV gerado com sucesso!")