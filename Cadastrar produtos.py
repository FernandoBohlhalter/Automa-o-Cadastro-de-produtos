import webbrowser as web
import pyautogui as py
import pandas as pd
import time

#Open the web-site
#abre site do sistema
web.open("https://dlp.hashtagtreinamentos.com/python/intensivao/login", new=2)

#Wait x seconds for proper website loading
#Espera x segundos para o site carregar
time.sleep(2)

#logs-in the website
#faz login do sitema
py.press("tab")
py.write("email@gmail.com")
py.press("tab")
py.write("senha")
py.press("enter")

#import product database
#importa base de dados dos produtos
data = pd.read_csv("produtos.csv")

#Wait x seconds for proper website loading
#Espera x segundos para o site carregar
time.sleep(0.5)

#Creates array with all columns as index
#Cria vetor com cada index sendo uma coluna
columns = []
for col in data.columns:
    columns.append(col)

for i in range(10):
    py.click(x= 758, y= 351)
    for j in range(6):
        if(str(data.loc[i, columns[j]]) != "nan"):
            py.write(str(data.loc[i, columns[j]]))
        py.press('tab')

    py.press('enter')
    py.press('tab')
    py.press('home')
    time.sleep(0.5)