from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
from ranking import *

# Medidas da janela
screen_width = 1280 
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Imagem de fundo
fundo = GameImage('Imagens/Play/background.png')
fundo.set_position(0, 0)

vidas = 3

nome = ''

score_anterior = score_total = 0
pontos = 50

# Inicialização da nave
spaceship = Sprite('Imagens/Play/spaceship.png')
spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)

# Definição da velocidade da nave e dos tiros
velocity_ship = 300
velocity_shot = 240
fim = False

alien_sprite = Sprite('Imagens/Play/alien.png')
max_linhas = 10
max_colunas = 10
linhas, colunas = 3, 5
linhas_1, colunas_1 = linhas, colunas
distancia = alien_sprite.width + alien_sprite.height
direcao = 1
y = 0
aliens = []
def aliens_create(aliens, linhas, colunas):
    aliens.clear()
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


aliens_create(aliens, linhas_1, colunas_1)
# Inicializa lista de tiros na tela vazia
shoots = []
temp_alien = 500 * screen.delta_time()
temp_ship = 500 * screen.delta_time()
alien_shot = [random.randint(0, linhas-1), random.randint(0, colunas-1)]

especial = 0

pisca = -1

parado = 0
pos_parado = [spaceship.x, spaceship.y]

# Função de atualização da janela
def update_screen():
    # Desenha o fundo
    fundo.draw()
    global pisca
    global vidas
    global parado
    global pos_parado

    # atualiza a posição da nave e a desenha
    if parado >= 0:
        spaceship.set_position(pos_parado[0], pos_parado[1])
        parado -= 1
    else:
        spaceship.set_position(spaceship.x, spaceship.y)
    spaceship.draw()

    if pisca % 2 != 0 and pisca >= 0:
        spaceship.hide()
        if pisca == 0:
            pisca = -1
        pisca -= 1
    else:
        spaceship.unhide()
        pisca -= 1

    colisao = False
    velocity_alien_x = 200

    global y
    global direcao
    global aliens
    global temp_alien
    global alien_shot
    global linhas_1
    global colunas_1
    global especial
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
    if temp_alien >= 1500 * screen.delta_time():
        alien_shot = [random.randint(0, linhas_1-1), random.randint(0, colunas_1-1)]
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
                score += pontos
            
            if alien[2]+alien[0].height > spaceship.y:
                return True


            if alien_shot == [l, c] and temp_alien == 0 and alien[3]:
                especial += 1
                if especial >= 3:
                    especial_shoot(alien[1], alien[2]+alien[0].width/2)
                    especial = 0
                else:
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
        if shot[0].collided(spaceship) and pisca < 0:
            if shot[3]:
                parado = 100
                pos_parado = [spaceship.x, spaceship.y]
                shoots.remove(shot)
                continue
            shoots.remove(shot)
            if vidas == 0:
                return True
            else:
                vidas -= 1
                pisca = 100
    
    shot_shot_collision()
    
    global score_anterior
    global score_total

    if score_anterior + score >= pontos * linhas_1 * colunas_1:
        score_total = score_anterior + score
        if linhas_1 < max_linhas:
            linhas_1 += 1
        if colunas_1 < max_colunas:
            colunas_1 += 1
        temp_alien -= 10 * screen.delta_time()

        restart(aliens, shoots, alien_shot)
        score_anterior = score_total

        pisca = 100
    else:
        score_total = score_anterior + score
    
    # Atualiza a tela
    screen.draw_text(str(score_anterior+score), screen_width-200, 1, 24, bold=True, color=(255, 255, 255))
    screen.draw_text(str(vidas), 72, 1, 24, bold=True, color=(255, 255, 255))

    screen.update()
    
def restart_total(spaceship, aliens, shoots, linhas_1, colunas_1):
    global score_anterior
    global temp_ship
    global temp_alien
    global vidas, nome, pontos, velocity_ship, velocity_shot, fim
    global alien_shot, pisca, especial
    vidas = 3
    nome = ''
    score_anterior = score_total = 0
    pontos = 50
    spaceship.set_position(screen_width/2 - spaceship.width/2, screen_height-spaceship.height*3)
    velocity_ship = 300
    velocity_shot = 240
    fim = False
    linhas_1, colunas_1 = linhas, colunas
    aliens.clear()
    aliens_create(aliens, linhas, colunas)
    shoots.clear()
    temp_alien = 500 * screen.delta_time()
    temp_ship = 500 * screen.delta_time()
    alien_shot = [random.randint(0, linhas-1), random.randint(0, colunas-1)]
    pisca = -1
    especial = 0

def restart(aliens, shoots, alien_shot):
    aliens.clear()
    aliens_create(aliens, linhas_1, colunas_1)
    shoots.clear()
    alien_shot = [random.randint(0, linhas_1-1), random.randint(0, colunas_1-1)]

def shot_shot_collision():
    for s1 in shoots:
        if s1[2] == -1:
            for s2 in shoots:
                if s2[2] == 1:
                    if s1[0].collided(s2[0]):
                        shoots.remove(s1)
                        shoots.remove(s2)
                        break

# Função que adiciona um tiro na lista, com o x sendo o da nave
def shoot(x, y, direcao):
    shot = Sprite('Imagens/Play/shot.png')
    shot.set_position(x, y)
    shoots.append([shot, False, direcao, False])

def especial_shoot(x, y):
    shot = Sprite('Imagens/Play/shot_2.png')
    shot.set_position(x, y)
    shoots.append([shot, False, 1, True])


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

    if (pressed.key_pressed('SPACE') and len(shoots)==0) or (pressed.key_pressed('SPACE') and temp_ship >= 700 * screen.delta_time()):
        if parado < 0:
            x = spaceship.x
            shoot(x, spaceship.y-spaceship.height, -1)
            
            temp_ship = 0

    # Voltar ao menu
    if pressed.key_pressed('ESC'):
        restart_total(spaceship, aliens, shoots, linhas_1, colunas_1)
        return 'None'
    global nome
    if fim:
        n = open('ranking.txt', 'a')
        print('O nome deve conter, no máximo, 16 caracteres')
        nome = input('Nome: ')
        n.write(nome + ',' + str(score_total)+ '\n')
        n.close()
        restart_total(spaceship, aliens, shoots, linhas, colunas)
        return Ranking()
    
    # Atualizar tela
    fim = update_screen()
    
    screen.draw_text(str(int(1/screen.delta_time())), 1, 1, 24, bold=True, color=(255, 255, 255))

    # Continuar jogando
    return Play

