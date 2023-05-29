import pygame

def anima_entrada(faixa_x, faixa_y, anima_entrada_value, velocidade, preto, display,
                  image_p1_selected, image_p2_selected):
    if anima_entrada_value:
        pos_y_selected = 140
        pos_x_selected_p1 = 50
        pos_x_selected_p2 = 650

        pos_x_vs = 275
        pos_y_vs = 125
        vs_image = pygame.image.load("sprite/vsImg.png")

        pygame.draw.rect(display, preto, (faixa_x, faixa_y, 3000, 240))

        faixa_x += velocidade

        if faixa_x > -1500:
            zoom_factor = 1.0 - ((faixa_x * -1) / 1500)
            zoom_factor *= 4

            if zoom_factor > 1.0:
                display.blit(image_p1_selected, (pos_x_selected_p1, pos_y_selected))

            if zoom_factor > 1.0:
                display.blit(image_p2_selected, (pos_x_selected_p2, pos_y_selected))

            zoomed_image_vs = pygame.transform.scale(vs_image, (int(vs_image.get_width() * zoom_factor),
                                                                int(vs_image.get_height() * zoom_factor)))

            if zoomed_image_vs.get_width() > 83:
                zoomed_image_vs = pygame.transform.scale(vs_image, (vs_image.get_width() // 2,
                                                                     vs_image.get_height() // 2))

            display.blit(zoomed_image_vs, (pos_x_vs, pos_y_vs))

        faixa_largura = 10
        if (faixa_x + faixa_largura) > 0:
            anima_entrada_value = False

    return faixa_x, anima_entrada_value
