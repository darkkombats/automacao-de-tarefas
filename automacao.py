import pyautogui
import time
import pandas # importa a base de dados

pyautogui.PAUSE = 0.5  # Pausa entre os comandos

# Entrar no sistema
# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Digitar o site e entrar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 3 segundos
time.sleep(3)

# Fazer o login
pyautogui.click(x=2441, y=754)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")

# Botão logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

# Importar base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Cadastrar um produto
for linha in tabela.index:  # Para cada linha da minha tabela

    pyautogui.click(x=2342, y=636)
    4
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    
    pyautogui.press("tab") # Passou para o botão enviar
    pyautogui.press("enter")

    pyautogui.scroll(1000)

# Repetir para todos os produtos

