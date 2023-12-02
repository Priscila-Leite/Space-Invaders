from PPlay.window import *
from PPlay.gameimage import *
from string import ascii_letters

# Medidas da janela
screen_width = 1280
screen_height = 720

# Inicialização da janela
screen = Window(screen_width, screen_height)
screen.set_title('Space Invaders')

# Imagem de fundo
fundo_nome = GameImage('Imagens/Play/background.png')
fundo_nome.set_position(0, 0)
fundo_rank = GameImage('Imagens/fundo_rank.png')
fundo_rank.set_position(0, 0)

teclado = Window.get_keyboard()

ranking = open('ranking.txt', 'r')

tamanho = 50
x_nome = 20
y_nome = 20
x_rank = 320
y_rank = 230
lista = []
lista_sort = []
def Ranking():
    global lista_sort
    fundo_rank.draw()

    if teclado.key_pressed('esc'):
        ranking.close()
        return 'None'

    if len(lista) == 0:
        for linha in ranking:
            linha = linha.strip().split(',')
            lista.append([linha[0], int(linha[1])])
        ranking.close()
    if len(lista_sort) == 0:
        lista_sort = [None]
        for n in range(len(lista)):
            if lista_sort[0]== None:
                lista_sort[0] = lista[n]
                continue
            for m in range(len(lista_sort)):
                if lista[n][1] > lista_sort[m][1]:
                    lista_sort.insert(m, lista[n])
                    break
                if m == len(lista_sort)-1:
                    if lista[n][1] > lista_sort[m][1]:
                        lista_sort.insert(m, lista[n])
                    else:
                        lista_sort.append(lista[n])
            

    for nome in range(len(lista_sort)):
        if nome >= 5:
            break
        screen.draw_text(lista_sort[nome][0], x_rank, y_rank + 80 * nome, tamanho, (0, 0, 0), 'Arial', True)
        screen.draw_text(str(lista_sort[nome][1]), 820, y_rank + 80 * nome, tamanho, (0, 0, 0), 'Arial', True)

    return Ranking