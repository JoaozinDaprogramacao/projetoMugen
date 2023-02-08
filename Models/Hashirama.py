import pygame





class Hashirama(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.__ground = 270

        self.spritesParado = []
        for i in range(1, 8):
            self.spritesParado.append(pygame.image.load(f"sprite/hashirama/parado/{i}.png"))

        self.spritesAtaque1 = []
        for i in range(1, 6):
            self.spritesAtaque1.append(pygame.image.load(f"sprite/hashirama/ataque1/{i}.png"))

        self.spritesCorrendo = []
        for i in range(1, 7):
            self.spritesCorrendo.append(pygame.image.load(f"sprite/hashirama/correndo/{i}.png"))

        self.spritesPulo = []
        for i in range(3, 7):
            self.spritesPulo.append(pygame.image.load(f"sprite/hashirama/pulo/{i}.png"))

        self.spritesEspecial = []
        for i in range(1, 25):
            self.spritesEspecial.append(pygame.image.load(f"sprite/hashirama/especial/{i}.png"))

        self.atual = 0
        self.image = self.spritesParado[self.atual]
        self.image = pygame.transform.scale(self.image, [36*2, 84*2])

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
                self.image = self.spritesParado[6]
                self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])

                self.__ultima = True
                self.__animacaoParado = False

            if not self.__ultima:
                self.image = self.spritesParado[int(self.atual)]
                self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])

    def __exibeAnimacaoAtaque1(self):
        if self.__animacaoAtaque1 == True:
            self.atual += 0.4
            self.__x_velocidade = 3
            if self.atual >= len(self.spritesAtaque1):
                self.atual = 0
                self.__x_velocidade = 0

                self.__animacaoAtaque1 = False
                self.__animacaoParado = True
                self.__ultima = False
            self.image = self.spritesAtaque1[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])

    def __exibeAnimacaoCorrendo(self):
        if self.__animacaoCorrendo == True:
            self.atual += 1
            self.aceleraDireita()
            if self.atual >= len(self.spritesCorrendo):
                self.atual = 0

            self.image = self.spritesCorrendo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])


    def __exibeAnimacaoCorrendoE(self):
        if self.__animacaoCorrendoE == True:
            print("aqui")
            self.atual += 1
            self.aceleraEsquerda()
            if self.atual >= len(self.spritesCorrendo):
                self.atual = 0

            self.image = self.spritesCorrendo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])
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
            self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])

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
            self.image = pygame.transform.scale(self.image, [36 * 2, 84 * 2])

    def aceleraDireita(self):
        self.__x_velocidade = 7

    def aceleraEsquerda(self):
        self.__x_velocidade = -7

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
        self.__animacaoCorrendo = True
        self.__animacaoPulo = False


    def correE(self):
        self.__animacaoParado = False
        self.__animacaoEspecial = False
        self.__animacaoAtaque1 = False
        self.__animacaoParado = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = True
        self.__animacaoPulo = False


    def paraDeCorrer(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoParado = True
        self.__animacaoEspecial = False
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False


    def paraDeCorrerE(self):
        self.__animacaoParado = False
        self.__animacaoAtaque1 = False
        self.__animacaoEspecial = False
        self.__animacaoParado = True
        self.__animacaoCorrendo = False
        self.__animacaoCorrendoE = False

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

