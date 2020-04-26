# Creado por Jesus Imitola
# GitHub User: jgimitola
# Fecha: del 19 de Abril de 2020 hasta el 22 de Abril de 2020.

import os
import pygame
from Game import Game
import matplotlib.pyplot as plt
from PIL import Image


def simulate(n, N, M, preferredSize):
    class Cell:
        x = 0
        y = 0
        side = 0

        def __init__(self, x, y, s):
            self.x = x
            self.y = y
            self.side = s

        def paint(self, vivo):
            if vivo:
                pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, self.side, self.side])
            else:
                pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.side, self.side])

    def paintGrid(g, grid):
        for j in range(n):
            row = grid[j]
            for i in range(n):
                row[i].paint(g.elementos[(i, j)]["vivo"])

    def paintGrid2(gen, grid):
        for j in range(n):
            row = grid[j]
            for i in range(n):
                row[i].paint(gen[(i, j)]["vivo"])

    # Definimos que centraremos la pantalla.
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Iniciamos pygame.
    pygame.init()

    # Damos el tamaño de pantalla, titulo e icono.
    screen = pygame.display.set_mode((preferredSize, preferredSize))
    pygame.display.set_caption("Conway's Game of Life")
    icon = pygame.image.load('imgs/cell.png')
    pygame.display.set_icon(icon)

    # Variables para ajustar GUI.
    SPACING = 2
    BLOCK_SIZE = preferredSize // n - SPACING
    CENTERING = (preferredSize - n * (BLOCK_SIZE + SPACING)) // 2

    # Creamos la grilla.
    grid = []
    for j in range(n):
        row = []
        for i in range(n):
            row.append(Cell(i * (BLOCK_SIZE + SPACING) + CENTERING, j * (BLOCK_SIZE + SPACING) + CENTERING, BLOCK_SIZE))
        grid.append(row)

    clock = pygame.time.Clock()

    di = {}

    # Si se desean escoger las celulas iniciales.
    if N == 0:
        for i in range(n):
            for j in range(n):
                di[(i, j)] = {
                    "vivo": False,
                    "vecinos": 0
                }
        escogido = False
        while not escogido:
            screen.fill((88, 137, 184))
            pos = pygame.mouse.get_pos()
            posI = ((pos[0] - CENTERING) // (BLOCK_SIZE + SPACING))
            posJ = ((pos[1] - CENTERING) // (BLOCK_SIZE + SPACING))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= posI < n and 0 <= posJ < n:
                        if event.button == 1:
                            if (posI, posJ) in di:
                                vecis = [(posI, posJ - 1), (posI, posJ + 1), (posI - 1, posJ), (posI + 1, posJ),
                                         (posI - 1, posJ - 1), (posI + 1, posJ - 1),
                                         (posI - 1, posJ + 1),
                                         (posI + 1, posJ + 1)]
                                if not di[(posI, posJ)]["vivo"]:
                                    di[(posI, posJ)]["vivo"] = True
                                    for vecino in vecis:
                                        if 0 <= vecino[0] < n and 0 <= vecino[1] < n:
                                            di[vecino]["vecinos"] += 1
                                else:
                                    di[(posI, posJ)]["vivo"] = False
                                    for vecino in vecis:
                                        if 0 <= vecino[0] < n and 0 <= vecino[1] < n:
                                            di[vecino]["vecinos"] -= 1
                        elif event.button == 3:
                            escogido = True

            paintGrid2(di, grid)
            clock.tick(30)
            pygame.display.update()
        game = Game(n, N, di.copy())
    else:
        game = Game(n, N)

    # GUI
    posBotones = (preferredSize // 2 - 62, preferredSize - 64)
    font = pygame.font.Font('fonts/Roboto-Medium.ttf', 16)
    pausa = pygame.image.load('imgs/controles-pausa.png')
    play = pygame.image.load('imgs/controles-play.png')

    # Controladores
    cont = 1
    delay = 0
    desvan = 0
    FPS = 25
    FramesDelay = FPS // 2
    esPausa = False
    adelantar = False

    # Iterator
    vivos = []
    naci = []
    muer = []
    g = game.inicio

    vivos.append(len(g.vivos()))
    naci.append(len(g.nacimientos()))
    muer.append(len(g.muertes()))

    xAnt = 0
    yAnt = 0
    while True:
        h = iter(game)
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        screen.fill((88, 137, 184))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejeX = range(1, cont + 1)
                plt.title("Estadísticas por generación")
                plt.plot(ejeX, vivos, label="Vivos")
                plt.plot(ejeX, naci, label="Nacerán")
                plt.plot(ejeX, muer, label="Morirán")
                plt.legend()
                plt.savefig('runs/run.png')
                img = Image.open('runs/run.png')
                img.show()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Backend botones.
                    if not esPausa:
                        if (preferredSize // 2) - 15 < x < (
                                preferredSize // 2) + 15 and preferredSize - 64 < y < preferredSize - 32:
                            esPausa = True
                    else:
                        if (preferredSize // 2) - 15 < x < (
                                preferredSize // 2) + 15 and preferredSize - 64 < y < preferredSize - 32:
                            esPausa = False
                        elif (preferredSize // 2) + 30 < x < (
                                preferredSize // 2) + 64 and preferredSize - 64 < y < preferredSize - 32:
                            adelantar = True

        if adelantar:
            if cont < M:
                try:
                    g = next(h)
                except:
                    pass
                cont += 1
                vivos.append(len(g.vivos()))
                naci.append(len(g.nacimientos()))
                muer.append(len(g.muertes()))
            adelantar = False

        if delay >= FramesDelay:
            if cont < M and not esPausa:
                try:
                    g = next(h)
                except:
                    pass
                cont += 1
                vivos.append(len(g.vivos()))
                naci.append(len(g.nacimientos()))
                muer.append(len(g.muertes()))
            delay = 0
        else:
            delay += 1

        paintGrid(g, grid)

        screen.blit(font.render('Generacion: ' + str(cont), True, (0, 255, 26)), (0, 0))

        # Despliegue de controles.
        if xAnt == x and yAnt == y:
            desvan += 1
        else:
            desvan = 0

        if desvan <= FPS or esPausa:
            if esPausa:
                screen.blit(pausa, posBotones)
            else:
                screen.blit(play, posBotones)

        xAnt = x
        yAnt = y
        clock.tick(FPS)
        pygame.display.update()
