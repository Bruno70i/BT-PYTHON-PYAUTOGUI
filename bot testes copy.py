# Utilizando biblioteca pyautogui

import pyautogui
import time


time.sleep(3)

posicao = pyautogui.locateOnScreen("logo_comentario.png", confidence=0.8)

if posicao:
    # Obtenha as coordenadas do centro da imagem
    centro = pyautogui.center(posicao)
    # Clique no centro da imagem
    pyautogui.click(centro)
    print("Imagem encontrada e clicada!")
else:
    print("Imagem não encontrada.")

time.sleep(3)



posicao = pyautogui.locateOnScreen("img_adicione_um_comentario.png", confidence=0.8)

if posicao:
    # Obtenha as coordenadas do centro da imagem
    centro = pyautogui.center(posicao)
    # Clique no centro da imagem
    pyautogui.click(centro)
    print("Imagem encontrada e clicada!")
else:
    print("Imagem não encontrada.")


time.sleep(3)
pyautogui.write("muito bom")