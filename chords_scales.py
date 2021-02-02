import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)


font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



click = False
def chords():

    global click
    while True:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        draw_text('chords', font, (255, 255, 255), screen, 80, 85)
        draw_text('scales', font, (255, 255, 255), screen, 80, 180)

        button_3 = pygame.Rect(50, 100, 200, 50)
        button_4 = pygame.Rect(50, 200, 200, 50)
        if button_3.collidepoint((mx, my)):
            if click:
                chords()
        if button_4.collidepoint((mx, my)):
            if click:
                scales()
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def scales():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)