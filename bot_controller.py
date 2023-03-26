from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Define as opções do driver
opcoes = Options()

# Cria uma instância do driver do Chrome
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opcoes)


def start_robot():
   
