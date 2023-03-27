import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, *groups, indice_parado):
        super().__init__(*groups)
        self.__ground = 270

        self.spritesParado = []
        self.spritesAtaque1 = []
        self.spritesCorrendo = []
        self.spritesPulo = []
        self.spritesEspecial = []

        self.atual = 0
        self.image = self.spritesParado[self.atual]
        self.image = pygame.transform.scale(self.image, [self.rect.x*2, self.rect.y*2])

        self.rect = pygame.Rect(50, self.__ground, 100, 100)
        self.__x_velocidade = 0
        self.__y_velocidade = 0



        self.__animacaoParado = True
        self.__animacaoAtaque1 = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False
        self.__animacaoPulo = False
        self.__animacaoEspecial = False
        self.__ultima = False

        def __exibeAnimacaoParado(self):
            if self.__animacaoParado == True:
                self.atual += 1
                if self.atual >= len(self.spritesParado):
                    self.atual = 0
                    self.image = self.spritesParado[indice_parado]
                    self.image = pygame.transform.scale(self.image, [self.rect.x * 2, self.rect.y * 2])

                    self.__ultima = True
                    self.__animacaoParado = False

                if not self.__ultima:
                    self.image = self.spritesParado[int(self.atual)]
                    self.image = pygame.transform.scale(self.image, [self.rect.x * 2, self.rect.y * 2])