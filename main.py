from PPlay.window import *
from PPlay.mouse import *
from menu import *
from play import *

# Medidas da janela
screen_width = 1280
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Inicialização da tela inicial do jogo sendo o menu principal
tipo = menu

# Inicialização do modo de jogo como fácil
modo = 3 * screen_height/5
while True:
    
    if tipo == menu or tipo == 'None':
        tipo = menu()

    if (tipo == Play) or (tipo == 'Play'):
        tipo = Play(modo)

    if tipo == Difficulty:
        tipo = Difficulty() 

        # Se a variável da tela do jogo for uma lista, inicie o jogo
        # no modo correspondente
        if type(tipo) == list:
            modo = tipo[1]
            if tipo[1] != 0: 
                if tipo[1] == 1:
                    modo = 2 * screen_height/5
                else:
                    modo = 1 * screen_height/5
            tipo = Play(modo)

    if tipo == Ranking:
        tipo = menu

    if tipo == Exit: # Fecha a janela
        break
    
    # Atualiza a janela
    screen.update()