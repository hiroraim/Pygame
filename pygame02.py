import sys
import pygame
from pygame.locals import QUIT


def main():
    pygame.init()
    surface = pygame.display.set_mode((300,300))
    pygame.display.set_caption("Pygame draw")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill((255,255,255))
        """
        rect(画面,(R,G,B),(左上の座標,横の幅,たての幅),線の太さ)
        """
        #pygame.draw.rect(surface,(0,0,0),(10,10,260,40),1)
        #pygame.draw.rect(surface,(0,255,255),(15,10,80,40),5)
        
        """
        circle(画面,(R,G,B),(中心の座標),直線,線の太さ)
        """
        #pygame.draw.circle(surface,(255,0,0),(100,200),100,1)
        #pygame.draw.circle(surface,(0,255,0),(200,200),100,1)
        #pygame.draw.circle(surface,(0,0,255),(150,100),100,1)
        #pygame.draw.circle(surface,(255,0,255),(200,100),10)

        """
        ellipse(画面,(R,G,B),(中心の座標,楕円の長形(横の長さ),楕円の短径(たての長さ)))
        """
        pygame.draw.ellipse(surface,(100,100,100),(50,100,200,200),2)
        #pygame.draw.ellipse(surface,(200,200,200),(150,150,80,40),)

        #pygame.draw.line(surface, (0,100,200), (8,220),(200,340),3)

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
