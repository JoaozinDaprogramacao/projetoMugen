import pygame
from Models.Hashirama import Hashirama
from Models.life import Life

pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Game")

drawGroup = pygame.sprite.Group()

life = Life(drawGroup)
hashirama = Hashirama(drawGroup)

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
                if event.key == pygame.K_d:
                   hashirama.corre()

                if event.key == pygame.K_a:
                    hashirama.correE()

                if event.key == pygame.K_j:
                    hashirama.ataque1()

                if event.key == pygame.K_k:
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                        hashirama.ataqueEspecial()

                if event.key == pygame.K_SPACE:
                    keys = pygame.key.get_pressed()
                    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                        hashirama.pula()





            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    hashirama.desacelera()
                    hashirama.paraDeCorrerE()

                if event.key == pygame.K_a:
                    hashirama.desacelera()
                    hashirama.paraDeCorrer()

        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()