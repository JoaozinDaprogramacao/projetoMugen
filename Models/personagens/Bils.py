import pygame
from Models.personagens.Personagem import Personagem

class Bils(Personagem):
    def __transforma_mult(self, indice, image):
        return pygame.transform.scale(image,
                               (image.get_width() * indice, image.get_height() * indice))

    def __transforma_div(self, indice, image):
        return pygame.transform.scale(image,
                               (image.get_width() / indice, image.get_height() / indice))
    def __init__(self, *groups):

        self.__indice = 4.5

        self.__ground = 282
        self.__indice_parado = 1

        self.__spritesParado = []
        self.__spritesAtaque1 = []
        self.__spritesCorrendo = []
        self.__spritesPulo = []
        self.__spritesEspecial = []

        for i in range(1, 4):
            image = pygame.image.load(f"sprite/bils/parado/{i}.png")
            scaled_image = self.__transforma_div(self.__indice, image)
            self.__spritesParado.append(scaled_image)

        for i in range(1, 11):
            image = pygame.image.load(f"sprite/bils/ataque1/{i}.png")
            scaled_image = self.__transforma_div(self.__indice, image)
            self.__spritesAtaque1.append(scaled_image)

        for i in range(1, 3):
            image = pygame.image.load(f"sprite/bils/correndo/{i}.png")
            scaled_image = scaled_image = self.__transforma_div(self.__indice, image)
            self.__spritesCorrendo.append(scaled_image)

        for i in range(3, 7):
            image = pygame.image.load(f"sprite/hashirama/pulo/{i}.png")
            scaled_image = scaled_image = self.__transforma_div(self.__indice, image)
            self.__spritesPulo.append(scaled_image)

        for i in range(1, 3):
            image = pygame.image.load(f"sprite/bils/explosao/{i}.png")
            scaled_image = scaled_image = self.__transforma_div(self.__indice, image)
            self.__spritesEspecial.append(scaled_image)


        super().__init__(self.__indice_parado, self.__spritesParado, self.__spritesAtaque1,
                         self.__spritesCorrendo, self.__spritesPulo, self.__spritesEspecial,
                         self.__ground, *groups)

