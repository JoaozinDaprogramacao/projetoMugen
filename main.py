import pygame
from Models.Hashirama import Hashirama
from Models.life import Life
from janelaEscolhePersonagem import Window


def anima_entrada(faixa_x, faixa_y, anima_entrada_value, velocidade, preto, display,
                  image_p1, image_p2):
    if(anima_entrada_value):
        pos_y_image = 240

        pos_x_p1 = 200
        pos_x_p2 = 500

        pos_x_vs = 275
        pos_y_vs = 7
        vs_image = pygame.image.load("sprite/vsImg.png")

        pygame.draw.rect(display, preto, (faixa_x, faixa_y, 3000, 240))

        faixa_x += velocidade

        if faixa_x > -1500:
            zoom_factor = 1.0 - ((faixa_x * -1) / 1500)
            zoom_factor *= 4

            zoomed_image = pygame.transform.scale(image_p1, (int(image_p1.get_width() * zoom_factor),
                                                             int(image_p1.get_height() * zoom_factor)))

            if zoomed_image.get_width() > 83:
                zoomed_image = pygame.transform.scale(image_p1, (image_p1.get_width(),
                                           image_p1.get_height()))

            display.blit(zoomed_image, (pos_x_p1, pos_y_image))

            display.blit(zoomed_image, (pos_x_p1, pos_y_image))

            #*-*-*-
            zoomed_image = pygame.transform.scale(image_p2, (int(image_p2.get_width() * zoom_factor),
                                                             int(image_p2.get_height() * zoom_factor)))

            if zoomed_image.get_width() > 83:
                zoomed_image = pygame.transform.scale(image_p2, (image_p2.get_width(),
                                                                 image_p2.get_height()))

            display.blit(zoomed_image, (pos_x_p2, pos_y_image))

            #*-*-*
            zoomed_image = pygame.transform.scale(vs_image, (int(vs_image.get_width() * zoom_factor),
                                                             int(vs_image.get_height() * zoom_factor)))

            if zoomed_image.get_width() > 83:
                zoomed_image = pygame.transform.scale(vs_image, (vs_image.get_width() // 2,
                                                                 vs_image.get_height() // 2))

            display.blit(zoomed_image, (pos_x_vs, pos_y_vs))




        if (faixa_x + faixa_largura) > 0:
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

largura = 840

preto = (0, 0, 0)

faixa_x = -3000
faixa_y = 140
faixa_largura = 10

velocidade = 10

img_p1 = pygame.image.load("sprite/selecaoPersonagem/hash.jpg")
img_p1 = pygame.transform.scale(img_p1, (img_p1.get_width() // 9,
                                           img_p1.get_height() // 9))


img_p2 = pygame.image.load("sprite/selecaoPersonagem/sasuke.jfif")
img_p2 = pygame.transform.scale(img_p2, (img_p2.get_width() // 9,
                                           img_p2.get_height() // 9))

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

        faixa_x, anima_entrada_value = anima_entrada(faixa_x, faixa_y,
                                anima_entrada_value, velocidade, preto, display, img_p1, img_p2)

        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()
