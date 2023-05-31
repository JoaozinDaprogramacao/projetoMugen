import pygame
from Models.personagens.Personagem_com_Projetil import Personagem_com_Projetil
from Models.projeteis.Projeteis import Projetil
from enums.Players import Players

class Hashirama(Personagem_com_Projetil):
    def __transforma_mult(self, indice, image):
        return pygame.transform.scale(image, (image.get_width() * indice, image.get_height() * indice))

    def __transforma_div(self, indice, image):
        return pygame.transform.scale(image, (image.get_width() / indice, image.get_height() / indice))

    def __inverte_se_p2(self, lista: list):
        if self.__players == Players.p2.value:
            for index, item in enumerate(lista):
                lista[index] = pygame.transform.flip(item, True, False)

        return lista

    def __init__(self, *groups, player):

        self.__indice = 2

        self.__players = player

        self.__ground = 295
        self.__indice_parado = 6

        self.__spritesParado = []
        self.__spritesAtaque1 = []
        self.__spritesCorrendo = []
        self.__spritesPulo = []
        self.__spritesEspecial = []
        self.__sprites_explosao = []


        for i in range(1, 8):
            image = pygame.image.load(f"sprite/hashirama/parado/{i}.png")
            scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesParado.append(scaled_image)
        self.__spritesParado = self.__inverte_se_p2(self.__spritesParado)

        for i in range(1, 5):
            image = pygame.image.load(f"sprite/hashirama/ataque1/{i}.png")
            scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesAtaque1.append(scaled_image)
        self.__spritesAtaque1 = self.__inverte_se_p2(self.__spritesAtaque1)

        for i in range(1, 6):
            image = pygame.image.load(f"sprite/hashirama/correndo/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesCorrendo.append(scaled_image)

        for i in range(3, 7):
            image = pygame.image.load(f"sprite/hashirama/pulo/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesPulo.append(scaled_image)
        self.__spritesPulo = self.__inverte_se_p2(self.__spritesPulo)

        for i in range(1, 4):
            image = pygame.image.load(f"sprite/hashirama/especial/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__spritesEspecial.append(scaled_image)
        self.__spritesEspecial = self.__inverte_se_p2(self.__spritesEspecial)

        for i in range(4, 25):
            image = pygame.image.load(f"sprite/hashirama/especial/{i}.png")
            scaled_image = scaled_image = self.__transforma_mult(self.__indice, image)
            self.__sprites_explosao.append(scaled_image)
        self.__sprites_explosao = self.__inverte_se_p2(self.__sprites_explosao)

        self.__projetil = Projetil(self.__sprites_explosao,
                                   self.__ground, *groups)



        super().__init__(self.__players, self.__projetil, self.__indice_parado, self.__spritesParado, self.__spritesAtaque1,
                         self.__spritesCorrendo, self.__spritesPulo, self.__spritesEspecial,
                         self.__ground, *groups)


