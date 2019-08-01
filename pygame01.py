import sys
import pygame
from pygame.locals import QUIT

def main():
    pygame.init()
    surface = pygame.display.set_mode((300,300))
    pygame.display.set_caption("Hello pygame!?#")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    text = font.render('Hello pygame', True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = surface.get_rect().centerx
    textpos.centery = surface.get_rect().centery
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill((220, 220, 220))
        surface.blit(text, textpos)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
