from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

# Medidas da janela
screen_width = 1280
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Imagem de fundo
fundo = GameImage('Imagens/Play/background.png')
fundo.set_position(0, 0)


score = 0

# Inicialização da nave
spaceship = Sprite('Imagens/Play/spaceship.png')
spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)

# Definição da velocidade da nave e dos tiros
velocity_ship = 180
velocity_shot = 240
fim = False

alien_sprite = Sprite('Imagens/Play/alien.png')
linhas, colunas = 3, 5
distancia = alien_sprite.width + alien_sprite.height
direcao = 1
y = 0
def aliens_create():
    aliens = []
    distancia_y = distancia
    for linha in range(linhas):
        list_linha = []
        distancia_x = distancia
        for coluna in range(colunas):
            alien = alien_sprite
            alien_x = distancia_x
            alien_y = distancia_y
            distancia_x += distancia
            list_linha.append([alien, alien_x, alien_y, True])
        distancia_y += distancia
        aliens.append(list_linha)
    return aliens


aliens = aliens_create()
# Inicializa lista de tiros na tela vazia
shoots = []
temp_alien = temp_ship = 500 * screen.delta_time()
alien_shot = [random.randint(0, linhas-1), random.randint(0, colunas-1)]

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
    global aliens
    global temp_alien
    global alien_shot
    y = 0
    score = 0
    temp_alien += 1

    for linha in aliens:
        if colisao:
            break
        for alien in linha:
            if alien[3]:
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
    if temp_alien >= 500 * screen.delta_time():
        alien_shot = [random.randint(0, linhas-1), random.randint(0, colunas-1)]
        temp_alien = 0
    l = 0
    
    for linha in aliens:
        c = 0
        for alien in linha:
            alien[2] += y * alien[0].height
            alien[0].set_position(alien[1], alien[2])
            alien[1] += direcao * velocity_alien_x * screen.delta_time()

            for shot in shoots:
                # Coordenadas dos cantos do tiro
                shot_left = shot[0].x
                shot_right = shot[0].x + shot[0].width
                shot_top = shot[0].y
                shot_bottom = shot[0].y + shot[0].height

                # Coordenadas dos cantos do alien
                alien_left = alien[1]
                alien_right = alien[1] + alien[0].width
                alien_top = alien[2]
                alien_bottom = alien[2] + alien[0].height

                # Verifica se algum dos cantos do tiro está dentro do retângulo do alien
                if ((shot_left >= alien_left and shot_left <= alien_right) or (shot_right >= alien_left and shot_right <= alien_right)) and ((shot_top >= alien_top and shot_top <= alien_bottom) or (shot_bottom >= alien_top and shot_bottom <= alien_bottom)) and not shot[1] and alien[3] and shot[2] == -1:
                    shot[1] = True
                    alien[3] = False


            if alien[3]:
                alien[0].draw()
            else:
                score += 50
            
            if alien[2]+alien[0].height > spaceship.y:
                return True

            if alien_shot == [l, c] and temp_alien == 0 and alien[3]:
                shoot(alien[1], alien[2]+alien[0].width/2, 1)
            c += 1
        l += 1


    # Desenha cada tiro da lista movendo
    for shot in shoots:
        shot[0].y += shot[2] * velocity_shot * screen.delta_time()
        if shot[0].y <= -2*shot[0].height and len(shoots) > 0:
            shoots.remove(shot)
            continue
        if shot[0].y >= screen_height and len(shoots) > 0:
            shoots.remove(shot)
            continue
        if not shot[1]:
            shot[0].draw()
        if shot[0].collided(spaceship):
            shoots.remove(shot)
            return True

    
    # Atualiza a tela
    screen.draw_text(str(score), screen_width-200, 1, 24, bold=True, color=(255, 255, 255))
    screen.update()
    

# Função que adiciona um tiro na lista, com o x sendo o da nave
def shoot(x, y, direcao):
    shot = Sprite('Imagens/Play/pixel-32x35.png')
    shot.set_position(x, y)
    shoots.append([shot, False, direcao])


def Play(modo):
    global fim
    global aliens
    global temp_ship

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
    temp_ship += 1
    # Execução de tiro se não houver tiros no terceiro quarto da altura da tela
    if (pressed.key_pressed('SPACE') and len(shoots)==0) or (pressed.key_pressed('SPACE') and temp_ship >= 500 * screen.delta_time()):
        x = spaceship.x
        shoot(x, spaceship.y-spaceship.height, -1)
        
        temp_ship = 0

    # Voltar ao menu
    if pressed.key_pressed('ESC') or fim:
        spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)
        aliens = aliens_create()
        while len(shoots) > 1:
            shoots.pop()
        return 'None'
    
    # Atualizar tela
    fim = update_screen()
    screen.draw_text(str(int(1/screen.delta_time())), 1, 1, 24, bold=True, color=(255, 255, 255))

    # Continuar jogando
    return Play

