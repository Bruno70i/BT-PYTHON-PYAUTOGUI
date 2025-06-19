# Utilizando biblioteca Pyautogui 

import pyautogui
import time

#pyautogui.press("win")
#pyautogui.PAUSE = 2
#pyautogui.write("gimp")


pyautogui.press("win")
time.sleep(1)

pyautogui.write("google")
time.sleep(1)

pyautogui.press("enter")
time.sleep(1)


# Clica no link com logo do instagram
posicao = pyautogui.locateOnScreen("insta-link-logo.png", confidence=0.8)

if posicao:
    # Obtenha as coordenadas do centro da imagem
    centro = pyautogui.center(posicao)
    # Clique no centro da imagem
    pyautogui.click(centro)
    print("Imagem encontrada e clicada!")
else:
    print("Imagem não encontrada.")

time.sleep(4)




# Clica na pagina inicial para ativar o cursos scroll
posicao = pyautogui.locateOnScreen("pagina-insta-inicial.png", confidence=0.8)

if posicao:
    # Obtenha as coordenadas do centro da imagem
    centro = pyautogui.center(posicao)
    # Clique no centro da imagem
    pyautogui.click(centro)
    print("Imagem encontrada e clicada!")
else:
    print("Imagem não encontrada.")

time.sleep(2)


# Clica no comentario do instagram
imagem_encontrada = False

# Define um número máximo de tentativas (opcional)
max_tentativas = 30
tentativas = 0

while not imagem_encontrada:
    try:
        # Tentar localizar a imagem na tela
        posicao = pyautogui.locateOnScreen("logo_comentario.png", confidence=0.8)
        
        # Caso a imagem seja encontrada, clique nela e saia do loop
        centro = pyautogui.center(posicao)
        pyautogui.click(centro)
        print("Imagem encontrada e clicada!")
        imagem_encontrada = True
    
    except pyautogui.ImageNotFoundException:
        # Caso a imagem não seja encontrada, role a tela para baixo e continue
        print("Rolando a tela até encontrar....")
        pyautogui.scroll(-300)
        time.sleep(3)
        
        # Incrementar contador de tentativas (opcional)
        tentativas += 1
        if max_tentativas > 0 and tentativas >= max_tentativas:
            print(f"Desistindo após {max_tentativas} tentativas")
            break




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

