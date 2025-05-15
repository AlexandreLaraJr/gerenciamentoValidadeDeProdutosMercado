# %%

# inicia imports/bibliotecas e Selenium

def getChocolates():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import pandas as pd
    import random
    from datetime import datetime, timedelta

    def gerar_data_aleatoria():
            inicio = datetime(2025, 1, 1)
            fim = datetime(2025, 5, 16)
            delta = fim - inicio
            dias = random.randint(0, delta.days)
            return (inicio + timedelta(days=dias)).date()

    options = Options()
    service = Service()
    options.add_argument('--headless')  
    optionsWebDriver = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service, options=optionsWebDriver)

    url = "https://lista.mercadolivre.com.br/alimentos-bebidas/mercearia/doces-chocolates/chocolates/barra-chocolate_NoIndex_True?sb=category#D[A:barra%20chocolate]"
    driver.get(url)

    # espera até que o elemento esteja presente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'poly-component__title'))
        # EC.visibility_of_element_located((By.CLASS_NAME, 'poly-component__title'))
    )

    # pega o html da página
    html = driver.page_source

    # inicia o BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    # raspagem com BeautifulSoup
    titles = soup.find_all('a', class_='poly-component__title')
    fractions = soup.find_all('span', class_='andes-money-amount__fraction')
    cents = soup.find_all('span', class_='andes-money-amount__cents')

    categoriaProduto = 'Chocolates'
    vendas = []

    # para cada produto, gera entre 1 a 20 vendas com data aleatória
    for title, frac, cent in zip(titles, fractions, cents):
        nome = title.get_text(strip=True)
        preco = frac.get_text(strip=True) + ',' + cent.get_text(strip=True)
        num_vendas = random.randint(1, 20)

        for _ in range(num_vendas):
            vendas.append({
                'nome': nome,
                'preço': preco,
                'categoriaProduto': categoriaProduto,
                'data_venda': gerar_data_aleatoria()
            })

    driver.quit()

    df = pd.DataFrame(vendas)

    return df