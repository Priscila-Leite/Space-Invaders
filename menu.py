from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from play import Play
from difficulty import Difficulty
from ranking import Ranking

space = GameImage('Imagens/Menu/space.png')
space.set_position(0, 0)

title = GameImage('Imagens/Menu/title.png')
title.set_position(180, 87)

play_button = GameImage('Imagens/Menu/play-button.png')
difficulty_button = GameImage('Imagens/Menu/difficulty-button.png')
ranking_button = GameImage('Imagens/Menu/ranking-button.png')
exit_button = GameImage('Imagens/Menu/exit-button.png')

buttons_unpressed = [play_button, difficulty_button, ranking_button, exit_button]
buttons_pressed = []


for button in buttons_unpressed:
    file = str(button.file_name)
    file = 'Imagens/Menu/' + file[13:-4] + '-pressed' + '.png'
    file = GameImage(file)
    buttons_pressed.append(file)

Exit = 'exit'
options = [Play, Difficulty, Ranking, Exit]

def menu():
    x_buttons = 490
    y_buttons = 270
    buttons = []

    for button in range(len(buttons_unpressed)):
        if Mouse().is_over_area([x_buttons, y_buttons], [x_buttons + buttons_unpressed[button].width, y_buttons + buttons_unpressed[button].height]):
            button_pressed = buttons_pressed[button]
            if Mouse().is_button_pressed(1):
                return options[button]

        else:
            button_pressed = buttons_unpressed[button]
        button_pressed.set_position(x_buttons, y_buttons)
        buttons.append(button_pressed)
        y_buttons += 90
            
    space.draw()
    title.draw()
    for button in buttons:
        button.draw()

    return menu