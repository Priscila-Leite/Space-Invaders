from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *

# Medida padrão da janela
screen_width = 1280
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Imagem de fundo
space = GameImage('Imagens/Menu/space.png')
space.set_position(0, 0)

# Imagem do título do jogo
title = GameImage('Imagens/Menu/title.png')
title.set_position(180, 87)

# Botão "Dificuldade"
difficulty_button = GameImage('Imagens/Menu/difficulty-button.png')
difficulty_button.set_position(490, 360 )

# Botões facil, médio e difícil
facil = GameImage('Imagens/Menu/facil.png')
facil_pressed = GameImage('Imagens/Menu/facil-pressed.png')
medio = GameImage('Imagens/Menu/medio.png')
medio_pressed = GameImage('Imagens/Menu/medio-pressed.png')
dificil = GameImage('Imagens/Menu/dificil.png')
dificil_pressed = GameImage('Imagens/Menu/dificil-pressed.png')
buttons_unpressed = [facil, medio, dificil]
buttons_pressed = [facil_pressed, medio_pressed, dificil_pressed]

# Função que gera o menu dificuldade
def Difficulty():
    pressed = Window.get_keyboard()
    # Se pressionar a tecla 'Esc' volte ao menu
    if pressed.key_pressed('ESC'):
        return 'None'
    
    # Posição do primeiro botão
    x_buttons = 840
    y_buttons = 270

    # Para cada botão existente verifique se o cursor está sobre ele
    # e adicione a lista a imagem do botão correspondente ao seu estado
    # com sua posição exata
    buttons = []
    for button in range(len(buttons_unpressed)):
        if Mouse().is_over_area([x_buttons, y_buttons], [x_buttons + buttons_unpressed[button].width, y_buttons + buttons_unpressed[button].height]):
            button_pressed = buttons_pressed[button]
            # Se o botão esquerdo do mouse for pressionado, a 
            # dificuldade do jogo muda para a correspondente ao
            #  botão que está sob o cursor
            if Mouse.is_button_pressed(Mouse, 1): 
                return [Difficulty, button]
        else:
            button_pressed = buttons_unpressed[button]
        button_pressed.set_position(x_buttons, y_buttons)
        buttons.append(button_pressed)
        y_buttons += 90

    # Desenha o fundo, o título, o botão de dificuldade e os botões
    # facil, médio e difícil
    space.draw()
    title.draw()
    difficulty_button.draw()

    for button in buttons:
        button.draw()

    # Retorna a própria função
    return Difficulty