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

dataValidade = [fake.date_between(start_date='+10d', end_date='+200d') for _ in range(n)]

df["data_validade_produtos"] = dataValidade
# %%


df

# %%
#transforma a coluna de preço para float
#gera uma coluna com o valor de preço de custo

df["preço"] = df["preço"].str.replace(",", ".").astype(float)

df["preço_de_custo"] = (df["preço"] * 0.6).round(2)


df["preço"].dtype
df["preço_de_custo"].dtype


df
# %%

df
# %%
import random
def random_numbers(n):
    return [random.randint(1, 20) for _ in range(n)]


df["quantidade_vendida"] = random_numbers(n)
# %%

# Limpa os nomes dos produtos

import re
import unicodedata

def limpar_nome(nome):
    # Remove acentuação
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')

    # Substitui "biscoito" por "bolacha" (case-insensitive)
    nome = re.sub(r'\bbiscoito\b', 'Bolacha', nome, flags=re.IGNORECASE)

    # Remove a palavra "kit" e números sozinhos
    nome = re.sub(r'\bkit\b', '', nome, flags=re.IGNORECASE)
    nome = re.sub(r'\b\d+\b', '', nome)

    # Remove pesos/unidades (ex: 120g, 1kg, 6un, 230ml)
    nome = re.sub(r'\d+\s*(g|kg|ml|l|un|unidades)', '', nome, flags=re.IGNORECASE)

    # Remover duplicação da palavra "bolacha"
    nome = re.sub(r'\b(bolacha)(\s+\1)+\b', r'\1', nome, flags=re.IGNORECASE)

    # Remove espaços duplicados e tira espaços laterais
    nome = re.sub(r'\s+', ' ', nome).strip()

    # Remove hifen
    nome = re.sub(r'-', ' ', nome)

    return nome

df['nome_limpo'] = df['nome'].apply(limpar_nome)

# %%
df

# %%
df["preço"] = df["preço"].map("{:.2f}".format).str.replace(".", ",")
df["preço_de_custo"] = df["preço_de_custo"].map("{:.2f}".format).str.replace(".", ",")


df['preço'].dtype
# %%

#busca nomes que sao iguais
df[df['nome_limpo'].duplicated(keep=False)]
# %%

#exportando csv final!

df.to_csv('produtosETL.csv', index=False, encoding='utf-8')
# %%
