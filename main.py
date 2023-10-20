from PPlay.window import *
from PPlay.mouse import *
from menu import *
from play import *

screen_width = 1280
screen_height = 720

screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')



modo = 0

player.set_position(screen_width/2 - player.width/2, screen_height-player.height*3)

tipo = menu
while True:
    if tipo == menu or tipo == 'None':
        tipo = menu()
    if tipo == Play or tipo == 'Play':
        tipo = Play(modo)
    if tipo == Difficulty:
        tipo = Difficulty()
        if type(tipo) == list:
            modo = tipo[1]
            tipo = Play(modo)
    if tipo == Ranking:
        tipo = menu
    if tipo == Exit:
        break
        
    screen.update()