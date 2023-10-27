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
spaceship = Sprite('Imagens/Play/spaceship.png')
spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)

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
    spaceship.set_position(spaceship.x, spaceship.y)
    spaceship.draw()


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
    shot.set_position(x, spaceship.y-spaceship.height)
    shoots.append(shot)

# 
def Play(modo=0):
    pressed = Window.get_keyboard()

    # Nave não ultrapassa tela do jogo
    if spaceship.x <= spaceship.width*3:
        spaceship.x = spaceship.width*3
    if spaceship.x >= screen_width-spaceship.width*3:
        spaceship.x = screen_width-spaceship.width*3

    # Movimentos da nave
    if pressed.key_pressed('RIGHT') and spaceship.x < screen_width-spaceship.width*3:
        spaceship.x += velocity_ship * screen.delta_time()
    if pressed.key_pressed('LEFT') and spaceship.x > spaceship.width*3:
        spaceship.x -= velocity_ship * screen.delta_time()
    
    # Execução de tiro se não houver tiros no terceiro quarto da altura da tela
    if pressed.key_pressed('SPACE') and (shoots[0] == None or shoots[-1].y <= 3*screen_height/4):
        x = spaceship.x
        shoot(x)

    # Voltar ao menu
    if pressed.key_pressed('ESC'):
        spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)
        while len(shoots) > 1:
            shoots.pop()
        return 'None'
    
    # Atualizar tela
    update_screen()

    # Continuar jogando
    return Play

