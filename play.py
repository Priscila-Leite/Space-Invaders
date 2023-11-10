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
fim = False

aliens = []
alien_sprite = Sprite('Imagens/Play/alien.png')
linhas, colunas = 3, 5
distancia = alien_sprite.width + alien_sprite.height
direcao = 1
y = 0
def aliens_create():
    distancia_y = distancia
    for linha in range(linhas):
        list_linha = []
        distancia_x = distancia
        for coluna in range(colunas):
            alien = alien_sprite
            alien_x = distancia_x
            alien_y = distancia_y
            distancia_x += distancia
            list_linha.append([alien, alien_x, alien_y])
        distancia_y += distancia
        aliens.append(list_linha)


aliens_create()
# Inicializa lista de tiros na tela vazia
shoots = []

# Função de atualização da janela
def update_screen():
    # Desenha o fundo
    fundo.draw()

    # atualiza a posição da nave e a desenha
    spaceship.set_position(spaceship.x, spaceship.y)
    spaceship.draw()

    colisao = False
    perdeu = False
    velocity_alien_x = 200

    global y
    global direcao
    y = 0

    for linha in aliens:
        if colisao:
            break
        for alien in linha:
            if alien[1] < 0:
                direcao = 1
                colisao = True
                y += 1
                break

            if alien[1] > screen_width - alien[0].width:
                direcao = -1
                colisao = True
                y += 1
                break

    for linha in aliens:
        for alien in linha:
            alien[2] += y * alien[0].height
            alien[0].set_position(alien[1], alien[2])
            alien[1] += direcao * velocity_alien_x * screen.delta_time()
            alien[0].draw()
            if alien[2]+alien[0].height > spaceship.y:
                return True

    # Desenha cada tiro da lista movendo para cima
    for shot in shoots:
        shot.y -= velocity_shot * screen.delta_time()
        if shot.y <= -2*shot.height and len(shoots) > 0:
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


def Play(modo):
    global fim

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
    if (pressed.key_pressed('SPACE') and len(shoots)==0) or (pressed.key_pressed('SPACE') and shoots[-1].y <= modo):
        x = spaceship.x
        shoot(x)

    # Voltar ao menu
    if pressed.key_pressed('ESC') or fim:
        spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)
        while len(shoots) > 1:
            shoots.pop()
        return 'None'
    
    # Atualizar tela
    fim = update_screen()
    screen.draw_text(str(int(1/screen.delta_time())), 1, 1, 24, bold=True, color=(255, 255, 255))

    # Continuar jogando
    return Play

