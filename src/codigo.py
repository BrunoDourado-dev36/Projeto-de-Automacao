import pyautogui
import time
import pandas as pd

# Passo a passo do meu programa
# Passo 1: Entrar no sistema da empresa. 

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login.

pyautogui.click(x=815, y=413)
pyautogui.write("seila@gmail.com")
pyautogui.press("tab")
pyautogui.write("qualquer uma senha")
pyautogui.press("tab")
pyautogui.click(x=970, y=570)
pyautogui.click(x=970, y=570)
#pausa para o site("enter")
time.sleep(4)

# Passo 3: Abrir a base de dados. 

table = pd.read_csv("data/produtos.csv")
print(table)

for linha in table.index:
    # Passo 4: Cadastrar um produto.
    pyautogui.click(x=801, y=296)

    #codigo
    codigo = str(table.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(table.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo 
    tipo = str(table.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(table.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preco
    preco_unitario = str(table.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #custo
    custo = str(table.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(table.loc[linha, "obs"])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") #Cadastra um produto
    pyautogui.scroll(5000)  #Volta para o inicio da tela

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos.