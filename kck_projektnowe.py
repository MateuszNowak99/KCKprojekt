import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 1550
WINDOW_HEIGHT = 800

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

def display_text_animation(string):
    text = ''
    for i in range(len(string)):
        DISPLAYSURF.fill(WHITE)
        text = string[i]
        font = pygame.font.Font('freesansbold.ttf', 100)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        DISPLAYSURF.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        DISPLAYSURF.fill((255, 255, 255))
        pygame.display.flip()
        pygame.time.wait(3000)



def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for i in range (50):
                        display_text_animation('ABCDEFGHIJK')


DISPLAYSURF.fill(WHITE)
font = pygame.font.Font('freesansbold.ttf', 80)
text_surface = font.render("Aby rozpocząć naciśnij spację.", True, BLACK)
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
DISPLAYSURF.blit(text_surface, text_rect)
pygame.display.flip()



main()