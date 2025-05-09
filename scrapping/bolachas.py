# %%

# inicia imports/bibliotecas e Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = Options()
service = Service()
options.add_argument('--headless')  
optionsWebDriver = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=optionsWebDriver)

url = "https://lista.mercadolivre.com.br/biscoito-recheado?sb=all_mercadolibre#D[A:biscoito%20recheado]"
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


bolhachasList = []
bolachasPriceList = []    

#da append dos nomes e preços nas listas

for title, frac, cent in zip(titles, fractions, cents):
    # print(title.get_text(strip=True))
    bolhachasList.append(title.get_text(strip=True))
    bolachasPriceList.append(float(frac.get_text(strip=True) + '.' + cent.get_text(strip=True)))

print(bolhachasList)
print(bolachasPriceList)

driver.quit()

print(f"nome: {len(bolhachasList)}")
print(f"preço: {len(bolachasPriceList)}")



# %%
