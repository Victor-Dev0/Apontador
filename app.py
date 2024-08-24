import pyautogui
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import tkinter as tk
from tkinter import simpledialog
import requests

pyautogui.alert('O codigo vai começar!')
pyautogui.PAUSE = 0.5


def salvar_credencial(usuario,senha):
    dados = {'usuarios': usuario, 'senha': senha}
    with open('usuarios.json', 'w') as file:
        json.dump(dados, file, indent=4)

def obter_credencial():
    try:
        with open('usuarios.json', 'r') as file:
            dados = json.load(file)
            return dados['usuarios'], dados['senha']
    except FileNotFoundError:
        return None, None


usuario_salvo, senha_salva = obter_credencial()

if usuario_salvo is None and senha_salva is None:
    root = tk.Tk()
    root.withdraw()

    usuario = simpledialog.askstring("Login", "Digite seu usuário do GM3:")
    senha = simpledialog.askstring("Login", "Digite sua senha do GM3:", show="*")
    salvar_credencial(usuario, senha)
    usuario_salvo , senha_salva = obter_credencial()


dia = str(datetime.datetime.now().day)

driver = webdriver.Chrome()

try:
    driver.get('http://www.gm3.meta3group.com.br/')
    driver.maximize_window()

    time.sleep(1)

    pyautogui.press('TAB')
    pyautogui.write(usuario_salvo)
    pyautogui.press('TAB')
    pyautogui.write(senha_salva)
    pyautogui.press('enter')

    time.sleep(5)

    elementos = driver.find_elements(By.XPATH, "//a[@class='fc-daygrid-day-number']")
    elementos_dia = []
    
    if elementos == 0:
        print("Nenhum elemento encontrado!")
        pyautogui.alert("Nenhum elemento encontrado!")
        quit()

    for elemento in elementos:
        if elemento.text == dia:
            elementos_dia.append(elemento)

    if len(elementos_dia) > 1:
        elementos_dia[1].click()

    elif len(elementos_dia) == 1:
        elementos_dia[0].click()

    
    # APONTANDO
    pyautogui.click(x=1080, y=459, duration=1)
    pyautogui.press('pgdn')
    pyautogui.press('enter')
    pyautogui.press('TAB')
    pyautogui.write('08:00')
    pyautogui.press('TAB')
    pyautogui.write('Meta3AI')
    pyautogui.press('TAB')
    pyautogui.press('enter')
    driver.quit()
    pyautogui.alert('Apontamento feito com sucesso!')
except Exception as e:
    print(f'Erro: {e}')
    pyautogui.alert(f'Erro: {e}')
    quit()

