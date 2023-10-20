from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

# Medidas da janela
screen_width = 1280
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Imagem de fundo
fundo = GameImage('Imagens/Play/background.png')
fundo.set_position(0, 0)

# Inicialização da nave
ship = Sprite('Imagens/Play/ship.png')
ship.set_position(screen_width/2 - ship.width/2, screen_height-ship.height*3)

# Definição da velocidade da nave e dos tiros
velocity_ship = 180
velocity_shot = 180

# Inicializa lista de tiros na tela com 1 tiro fora da tela
shot1 = Sprite('Imagens/Play/pixel-32x35.png')
shot1.set_position(-1000, -1000)
shoots = [shot1]

# Função de atualização da janela
def update_screen():
    # Desenha o fundo
    fundo.draw()

    # atualiza a posição da nave e a desenha
    ship.set_position(ship.x, ship.y)
    ship.draw()


    # Desenha cada tiro da lista movendo para cima
    for shot in shoots:
        shot.y -= velocity_shot * screen.delta_time()
        if shot.y <= 0 and len(shoots) > 1:
            shoots.pop(0)
            continue
        shot.draw()

    # Atualiza a tela
    screen.update()

# Função que adiciona um tiro na lista, com o x sendo o da nave
def shoot(x):
    shot = Sprite('Imagens/Play/pixel-32x35.png')
    shot.set_position(x, ship.y-ship.height)
    shoots.append(shot)

# 
def Play(modo=0):
    pressed = Window.get_keyboard()

    if ship.x <= ship.width*3:
        ship.x = ship.width*3
    if ship.x >= screen_width-ship.width*3:
        ship.x = screen_width-ship.width*3

    if pressed.key_pressed('RIGHT') and ship.x < screen_width-ship.width*3:
        ship.x += velocity_ship * screen.delta_time()
    if pressed.key_pressed('LEFT') and ship.x > ship.width*3:
        ship.x -= velocity_ship * screen.delta_time()
    
    if pressed.key_pressed('SPACE') and (shoots[0] == None or shoots[-1].y <= 3*screen_height/4):
        x = ship.x
        shoot(x)

    if pressed.key_pressed('ESC'):
        return 'None'
    
    update_screen()

    return Play

