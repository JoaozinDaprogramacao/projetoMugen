import pygame
from Models.Personagem import Personagem

class Hashirama(Personagem):
    def __init__(self, *groups):

        self.__ground = 270
        self.indice_parado = 6

        self.__spritesParado = []
        self.__spritesAtaque1 = []
        self.__spritesCorrendo = []
        self.__spritesPulo = []
        self.__spritesEspecial = []

        for i in range(1, 8):
            self.__spritesParado.append(pygame.image.load(f"sprite/hashirama/parado/{i}.png"))

        for i in range(1, 6):
            self.__spritesAtaque1.append(pygame.image.load(f"sprite/hashirama/ataque1/{i}.png"))

        for i in range(1, 7):
            self.__spritesCorrendo.append(pygame.image.load(f"sprite/hashirama/correndo/{i}.png"))

        for i in range(3, 7):
            self.__spritesPulo.append(pygame.image.load(f"sprite/hashirama/pulo/{i}.png"))

        for i in range(1, 25):
            self.__spritesEspecial.append(pygame.image.load(f"sprite/hashirama/especial/{i}.png"))

        super().__init__(6, self.__spritesParado, self.__spritesAtaque1,
                         self.__spritesCorrendo, self.__spritesPulo, self.__spritesEspecial,
                         self.__ground, *groups)


