# %%
import pandas as pd

# importa e le o arquivo CSV 
df = pd.read_csv('produtos.csv', encoding='utf-8')

df
# %%
df.head()


# %%
df.tail()
# %%
#visualiza o dataframe nos registros 20 ao 30
df.iloc[20:31]


# %%

from faker import Faker

fake = Faker()

n = len(df)

dataAbastecimento = [fake.date_between(start_date='+10d', end_date='+100d') for _ in range(n)]
dataValidade = [fake.date_between(start_date='+10d', end_date='+200d') for _ in range(n)]

df["data_chegada_produtos"] = dataAbastecimento
df["data_validade_produtos"] = dataValidade
# %%

df.head()
# %%

#cria numeros entre 1 a 50
import random
def random_numbers(n):
    return [random.randint(1, 50) for _ in range(n)]


df["quantidade_produtos"] = random_numbers(n)

df.head()
# %% 

#cria numeros entre 60 a 100
def random_numbers(n):
    return [random.randint(60, 100) for _ in range(n)]

df["limite_estoque"] = random_numbers(n)
df.head()
# %%

#cria numeros entre 1 a 100
def random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

df["qtd_vendas_1mes_anterior"] = random_numbers(n)
df["qtd_vendas_2mes_anterior"] = random_numbers(n)
df["qtd_vendas_3mes_anterior"] = random_numbers(n)
df.head()

# %%
