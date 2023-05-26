import pygame

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

        faixa_largura = 10
        if (faixa_x + faixa_largura) > 0:
            anima_entrada_value = False




    return faixa_x, anima_entrada_value

