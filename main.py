import pygame
from Models.Hashirama import Hashirama
from Models.life import Life
from janelaEscolhePersonagem import Window
from time import sleep


def anima_entrada(faixa_x, faixa_y, anima_entrada_value, velocidade, preto, display):
    if(anima_entrada_value):
        pygame.draw.rect(display, preto, (faixa_x, faixa_y, 840, 480))

        faixa_x += velocidade

        if faixa_x + faixa_largura > 0:
            print("aqio")
            anima_entrada_value = False


    return faixa_x, anima_entrada_value





pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Game")

drawGroup = pygame.sprite.Group()

life = Life(drawGroup)

p1 = Hashirama(drawGroup)

background = pygame.image.load("sprite/hCUwLQ.png")

relogio = pygame.time.Clock()
gameLoop = True

sleep(5)
largura = 840

preto = (0, 0, 0)

faixa_x = -840
faixa_y = 0
faixa_largura = 10

velocidade = 5

anima_entrada_value = True

if __name__ == "__main__":
    Window()
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

        faixa_x, anima_entrada_value = anima_entrada(faixa_x, faixa_y, anima_entrada_value, velocidade, preto, display)

        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()
