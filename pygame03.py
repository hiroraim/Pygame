import sys
import pygame
from pygame.locals import QUIT

def main():
    pygame.init()
    surface = pygame.display.set_mode((300,400))
    pygame.display.set_caption("Circle move")
    clock = pygame.time.Clock()
    x = surface.get_rect().centerx
    y = 0
    go = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            surface.fill((255,255,255))
            if go:
                y += 10
                if(y == 390):
                    go = False
            elif not go:
                y -= 10
                if(y == 10):
                    go = True
                
            pygame.draw.circle(surface,(255,0,0),(x,y),10)
            pygame.display.update()
            clock.tick(100)

if __name__ == "__main__":
    main()
