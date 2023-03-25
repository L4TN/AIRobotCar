from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Define as opções do driver
opcoes = Options()

# Cria uma instância do driver do Chrome
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opcoes)


def start_robot():
    # Abre uma página web
    driver.get(
        "https://create.arduino.cc/editor/l4tn/34f7b74b-89cb-427d-90eb-41b8d1aef3ba")
    sleep(2)

    try:
        # Encontra o elemento "//*[@id="root"]/div/div/main/section/button" e clica nele
        driver.find_element_by_xpath(
            xpath="//*[@id=\"root\"]/div/div/main/section/button").click()
        sleep(2)
    except:
        print("Campo de login")

    # Tenta encontrar o campo de login e preenche com o valor "matheus.dias17@fatec.sp.gov.br"
    try:
        campo_login = driver.find_element_by_xpath(
            xpath="/html/body/div[1]/div[1]/div/div/div/main/section/form/div[1]/div/div[1]/input")
        campo_login.send_keys("matheus.dias17@fatec.sp.gov.br")
    except:
        print("Campo de login não encontrado")

    # Tenta encontrar o campo de senha e preenche com o valor "HShas@064"
    try:
        campo_senha = driver.find_element_by_xpath(
            xpath="/html/body/div[1]/div[1]/div/div/div/main/section/form/div[2]/div/div[1]/input")
        campo_senha.send_keys("HShas@064")
    except:
        print("Campo de senha não encontrado")

    # Tenta encontrar o botão de login e clica nele
    try:
        botao_login = driver.find_element_by_xpath(
            xpath="/html/body/div[1]/div[1]/div/div/div/main/section/form/button")
        botao_login.click()
    except:
        print("Botão de login não encontrado")
    sleep(10)

    try:
        driver.find_element_by_xpath(
            xpath="/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/main-menu/ul/li[4]/a").click()
        sleep(2)
    except:
        print("Botão Serial não encontrado")


def typing_robot(direction):
    try:
        botao_login = driver.find_element_by_xpath(
            xpath="/html/body/div[2]/div/div/div/div[2]/div/div/div[4]/div[2]/form/input[1]")
        botao_login.click()
        botao_login.send_keys(direction)

        botao_send = driver.find_element_by_xpath(
            xpath="/html/body/div[2]/div/div/div/div[2]/div/div/div[4]/div[2]/form/input[2]")
        botao_send.click()
    except:
        print("Send Monitor error ")
