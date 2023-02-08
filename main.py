import pygame
from Models.Hashirama import Hashirama
from Models.Bils import Bils
from Models.life import Life


pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Game")

drawGroup = pygame.sprite.Group()

life = Life(drawGroup)
p1 = Hashirama(drawGroup)
p2 = Bils(drawGroup)

background = pygame.image.load("sprite/hCUwLQ.png")

relogio = pygame.time.Clock()
gameLoop = True

if __name__ == "__main__":
    while gameLoop:
        relogio.tick(30)
        display.blit(background, [0, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                   p1.corre()

                if event.key == pygame.K_LEFT:
                    p1.correE()

                if event.key == pygame.K_z:
                    p1.ataque1()

                if event.key == pygame.K_x:
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                        p1.ataqueEspecial()


                if event.key == pygame.K_SPACE:
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                        p1.pula()


                #*-*-*-*-* p2 *-*-*--*

                if event.key == pygame.K_d:
                   p2.corre()

                if event.key == pygame.K_a:
                    p2.correE()

                if event.key == pygame.K_j:
                    p2.ataque1()



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    p1.desacelera()
                    p1.paraDeCorrerE()

                if event.key == pygame.K_LEFT:
                    p1.desacelera()
                    p1.paraDeCorrer()

                #*-**-*-*-* p2 *-*-**-*-*-*
                if event.key == pygame.K_d:
                    p2.desacelera()
                    p2.paraDeCorrerE()

                if event.key == pygame.K_a:
                    p2.desacelera()
                    p2.paraDeCorrer()


        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()