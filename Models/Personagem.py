import pygame


class Personagem(pygame.sprite.Sprite):
    def __init__(self, indice_parado, sprites_parado, sprites_ataque, sprites_correndo, sprites_pulo, sprites_especial, ground, *groups):
        super().__init__(*groups)
        self.__indice_parado = indice_parado
        print(f"indice parado: {self.__indice_parado}")
        self.__ground = ground
        self.spritesParado = sprites_parado
        self.spritesAtaque1 = sprites_ataque
        self.spritesCorrendo = sprites_correndo
        self.spritesPulo = sprites_pulo
        self.spritesEspecial = sprites_especial

        self.atual = 0
        self.image = self.spritesParado[self.atual]
        self.rect = self.image.get_rect()

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


    def update(self, *args):
        if self.rect.x <= 740 or self.rect.x >= 0:
            self.rect.x += self.__x_velocidade
            self.rect.y += self.__y_velocidade
        if self.rect.y < self.__ground:
            self.__y_velocidade = 20
        elif self.rect.y == self.__ground:
            self.__y_velocidade = 0


        self.__exibeAnimacaoParado()
        self.__exibeAnimacaoAtaque1()
        self.__exibeAnimacaoCorrendo()
        self.__exibeAnimacaoCorrendoE()
        self.__exibeAnimacaoPulo()
        self.__exibeAnimacaoEspecial()

    def __exibeAnimacaoParado(self):
        if self.__animacaoParado == True:
            self.atual += 1
            if self.atual >= len(self.spritesParado):
                self.atual = 0
                self.image = self.spritesParado[self.__indice_parado]

                self.__ultima = True
                self.__animacaoParado = False

            if not self.__ultima:
                self.image = self.spritesParado[int(self.atual)]



    def __exibeAnimacaoAtaque1(self):
        if self.__animacaoAtaque1 == True:
            self.atual += 0.2
            self.__x_velocidade = 3
            if self.atual >= len(self.spritesAtaque1):
                self.atual = 0
                self.__x_velocidade = 0

                self.__animacaoAtaque1 = False
                self.__animacaoParado = True
                self.__ultima = False
            self.image = self.spritesAtaque1[int(self.atual)]

    def animar_correndo(self):
        self.atual += 0.2
        if self.atual >= len(self.spritesCorrendo):
            self.atual = 0

        self.image = self.spritesCorrendo[int(self.atual)]

    def __exibeAnimacaoCorrendo(self):
        if self.__animacaoCorrendo:
            self.aceleraDireita()
            self.animar_correndo()
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.flip(self.image, True, False)

    def __exibeAnimacaoCorrendoE(self):
        if self.__animacaoCorrendoE:
            self.aceleraEsquerda()
            self.animar_correndo()
            self.image = pygame.transform.flip(self.image, True, False)

    def __exibeAnimacaoPulo(self):
        if self.__animacaoPulo == True:
            self.atual += 0.5
            self.__y_velocidade = -20

            if self.atual >= len(self.spritesPulo):
                self.atual = 0
                self.__y_velocidade = 0

                self.__animacaoParado = True
                self.__animacaoPulo = False

            self.image = self.spritesPulo[int(self.atual)]

    def __exibeAnimacaoEspecial(self):
        if self.__animacaoEspecial == True:
            self.atual += 0.5

            if int(self.atual == 4):
                self.__x_velocidade += 5

            if self.atual >= len(self.spritesEspecial):
                self.atual = 0
                self.__x_velocidade = 0

                self.__animacaoParado = True
                self.__animacaoEspecial = False

            self.image = self.spritesEspecial[int(self.atual)]

    def aceleraDireita(self):
        self.__x_velocidade = 5

    def aceleraEsquerda(self):
        self.__x_velocidade = -5

    def desacelera(self):
        self.__x_velocidade = 0

    def ataque1(self):
        print("aqui")
        self.__animacaoParado = False
        self.__animacaoEspecial = False
        self.__animacaoAtaque1 = True
        self.__animacaoParado = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False
        self.__animacaoPulo = False

    def corre(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoParado = False
        self.__animacaoEspecial = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False

        if self.rect.x <= 740:
            self.__animacaoCorrendo = True
        self.__animacaoPulo = False


    def correE(self):
        self.__animacaoParado = False
        self.__animacaoEspecial = False
        self.__animacaoAtaque1 = False
        self.__animacaoParado = False
        self.__animacaoCorrendo = False

        if self.rect.x >= 0:
            self.__animacaoCorrendoE = True
        self.__animacaoPulo = False


    def paraDeCorrer(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoParado = True
        self.__animacaoEspecial = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False

        self.desacelera()


    def paraDeCorrerE(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoEspecial = False
        self.__animacaoParado = True
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False

        self.desacelera()

    def pula(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoEspecial = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False
        self.__animacaoPulo = True

    def ataqueEspecial(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoEspecial = True
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False
        self.__animacaoPulo = False