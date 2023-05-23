import pygame
from Models.Hashirama import Hashirama
from Models.life import Life

pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Game")

drawGroup = pygame.sprite.Group()

life = Life(drawGroup)

p1 = Hashirama(drawGroup)


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

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                   p1.paraDeCorrer()

                if event.key == pygame.K_LEFT:
                    p1.paraDeCorrerE()

        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()