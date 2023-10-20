from PPlay.window import *
from PPlay.sprite import *

screen_width = 1280
screen_height = 720

screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

player = Sprite('Imagens/Play/ship.png')

velocity_player = 180
velocity_shot = 180
shot1 = Sprite('Imagens/Play/pixel-32x35.png')
shot1.set_position(-1000, -1000)
shoots = [shot1]
def update_screen():
    screen.set_background_color((0, 0, 0))
    
    player.set_position(player.x, player.y)

    player.draw()

    if shoots[0] == None and len(shoots) > 1:
        shoots.pop(0)

    for shot in shoots:
        shot.y -= velocity_shot * screen.delta_time()
        if shot.y <= 0 and len(shoots) > 1:
            shoots.pop(0)
            continue
        shot.draw()

    screen.update()


def shoot(x):
    shot = Sprite('Imagens/Play/pixel-32x35.png')
    shot.set_position(x, player.y-player.height)
    shoots.append(shot)


def Play(modo=0):
    pressed = Window.get_keyboard()

    if player.x <= player.width*3:
        player.x = player.width*3
    if player.x >= screen_width-player.width*3:
        player.x = screen_width-player.width*3

    if pressed.key_pressed('RIGHT') and player.x < screen_width-player.width*3:
        player.x += velocity_player * screen.delta_time()
    if pressed.key_pressed('LEFT') and player.x > player.width*3:
        player.x -= velocity_player * screen.delta_time()
    
    if pressed.key_pressed('SPACE') and (shoots[0] == None or shoots[-1].y <= 3*screen_height/4):
        x = player.x
        shoot(x)

    if pressed.key_pressed('ESC'):
        return 'None'
    
    update_screen()

    return Play

