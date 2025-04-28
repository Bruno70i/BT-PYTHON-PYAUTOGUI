# Utilizando biblioteca Pyautogui 

import pyautogui
import time

#pyautogui.press("win")
#pyautogui.PAUSE = 2
#pyautogui.write("gimp")


pyautogui.press("win")
time.sleep(3)

pyautogui.write("google")
time.sleep(3)

pyautogui.press("enter")
time.sleep(3)


# Clica no link do instagram
pyautogui.click(x=430, y=90)
time.sleep(5)



# Clica no comentario do instagram
posicao = pyautogui.locateOnScreen("logo_comentario.png", confidence=0.8)

if posicao:
    # Obtenha as coordenadas do centro da imagem
    centro = pyautogui.center(posicao)
    # Clique no centro da imagem
    pyautogui.click(centro)
    print("Imagem encontrada e clicada!")
else:
    print("Imagem não encontrada.")

time.sleep(4)



# Clica para ativar o comentario
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


# escreve o comantario
pyautogui.write("nossa")
time.sleep(2)
pyautogui.press("enter")




posicaoCursor = pyautogui.position()

print(posicaoCursor)

