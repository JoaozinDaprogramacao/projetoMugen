import pygame
from Models.Personagem import Personagem

class Hashirama(Personagem):
    def __transforma_mult(self, indice, image):
        return pygame.transform.scale(image,
                               (image.get_width() * indice, image.get_height() * indice))

    def __transforma_div(self, indice, image):
        return pygame.transform.scale(image,
                               (image.get_width() / indice, image.get_height() / indice))
    def __init__(self, *groups):

        self.__indice = 2

        self.__ground = 295
        self.__indice_parado = 6

        self.__spritesParado = []
        self.__spritesAtaque1 = []
        self.__spritesCorrendo = []
        self.__spritesPulo = []
        self.__spritesEspecial = []

        for i in range(1, 8):
            image = pygame.image.load(f"sprite/hashirama/parado/{i}.png")
            scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesParado.append(scaled_image)

        for i in range(1, 5):
            image = pygame.image.load(f"sprite/hashirama/ataque1/{i}.png")
            scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesAtaque1.append(scaled_image)

        for i in range(1, 6):
            image = pygame.image.load(f"sprite/hashirama/correndo/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesCorrendo.append(scaled_image)

        for i in range(3, 7):
            image = pygame.image.load(f"sprite/hashirama/pulo/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesPulo.append(scaled_image)

        for i in range(1, 24):
            image = pygame.image.load(f"sprite/hashirama/especial/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesEspecial.append(scaled_image)


        super().__init__(self.__indice_parado, self.__spritesParado, self.__spritesAtaque1,
                         self.__spritesCorrendo, self.__spritesPulo, self.__spritesEspecial,
                         self.__ground, *groups)