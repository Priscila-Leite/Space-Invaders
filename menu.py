"Construção do menu do jogo"
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from play import Play
from difficulty import Difficulty
from ranking import Ranking

# Imagem de fundo
space = GameImage('Imagens/Menu/space.png')
space.set_position(0, 0)

# Imagem do título do jogo
title = GameImage('Imagens/Menu/title.png')
title.set_position(180, 87)

# Inicialização dos botões
play_button = GameImage('Imagens/Menu/play-button.png')
difficulty_button = GameImage('Imagens/Menu/difficulty-button.png')
ranking_button = GameImage('Imagens/Menu/ranking-button.png')
exit_button = GameImage('Imagens/Menu/exit-button.png')

# Listas dos botões não pressionados e pressionados
buttons_unpressed = [play_button, difficulty_button, ranking_button, exit_button]
buttons_pressed = []
for button in buttons_unpressed:
    file = str(button.file_name)
    file = 'Imagens/Menu/' + file[13:-4] + '-pressed' + '.png'
    file = GameImage(file)
    buttons_pressed.append(file)

# Opções do menu
Exit = 'exit'
options = [Play, Difficulty, Ranking, Exit]

# Função que gera o menu do jogo
def menu():
    # x e y do primeiro botão
    x_buttons = 490
    y_buttons = 270
    # Inicialização da lista dos botões
    buttons = []

    # Para cada botão existente verifique se o cursor está sobre ele
    # e adicione a lista a imagem do botão correspondente ao seu estado
    # com sua posição exata
    for button in range(len(buttons_unpressed)):
        if Mouse().is_over_area([x_buttons, y_buttons], [x_buttons + buttons_unpressed[button].width, y_buttons + buttons_unpressed[button].height]):
            button_pressed = buttons_pressed[button]
            # Se o botão esquerdo do mouse for pressionado, ative a
            # função correspondente ao botão que está sob o cursor
            if Mouse().is_button_pressed(1):
                return options[button]

        else:
            button_pressed = buttons_unpressed[button]
        button_pressed.set_position(x_buttons, y_buttons)
        buttons.append(button_pressed)
        y_buttons += 90
            
    # Desenha o fundo, o título e os botões
    space.draw()
    title.draw()
    for button in buttons:
        button.draw()

    # Retorna a própria função
    return menu