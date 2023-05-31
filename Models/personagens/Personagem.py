import pygame
from enums.Players import Players

class Personagem(pygame.sprite.Sprite):
    def __init__(self, player, indice_parado, sprites_parado, sprites_ataque, sprites_correndo, sprites_pulo, sprites_especial, ground, *groups):
        super().__init__(*groups)

        self.__indice_parado = indice_parado

        self.__ground = ground
        self.spritesParado = sprites_parado
        self.spritesAtaque1 = sprites_ataque
        self.spritesCorrendo = sprites_correndo
        self.spritesPulo = sprites_pulo
        self.spritesEspecial = sprites_especial

        self._player = player

        self.atual = 0
        self.image = self.spritesParado[self.atual]
        self.rect = self.image.get_rect()

        if player == Players.p1.value:
            self.rect = pygame.Rect(50, self.__ground, 100, 100)

        elif player == Players.p2.value:
            self.rect = pygame.Rect(650, self.__ground, 100, 100)
        self.__x_velocidade = 0
        self.__y_velocidade = 0

        self._animacaoParado = True
        self._animacaoAtaque1 = False
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False
        self._animacaoPulo = False
        self._animacaoEspecial = False
        self.__ultima = False


    def update(self, *args):
        if self.rect.x <= 740 or self.rect.x >= 0:
            self.rect.x += self.__x_velocidade
            self.rect.y += self.__y_velocidade
        if self.rect.y < self.__ground:
            self.__y_velocidade = 20
        elif self.rect.y == self.__ground:
            self.__y_velocidade = 0


        self._exibeAnimacaoParado()
        self._exibeAnimacaoAtaque1()
        self._exibeAnimacaoCorrendo()
        self._exibeAnimacaoCorrendoE()
        self._exibeAnimacaoPulo()
        self._exibeAnimacaoEspecial()

    def _exibeAnimacaoParado(self):
        if self._animacaoParado == True:
            self.atual += 1
            if self.atual >= len(self.spritesParado):
                self.atual = 0
                self.image = self.spritesParado[self.__indice_parado]

                self.__ultima = True
                self._animacaoParado = False

            if not self.__ultima:
                self.image = self.spritesParado[int(self.atual)]



    def _exibeAnimacaoAtaque1(self):
        if self._animacaoAtaque1 == True:
            self.atual += 0.2
            print(self._player)
            if self._player == Players.p2.value:
                self.__x_velocidade = -3
            else:
                self.__x_velocidade = 3
            if self.atual >= len(self.spritesAtaque1):
                self.atual = 0
                self.__x_velocidade = 0

                self._animacaoAtaque1 = False
                self._animacaoParado = True
                self.__ultima = False
            self.image = self.spritesAtaque1[int(self.atual)]

    def animar_correndo(self):
        self.atual += 0.2
        if self.atual >= len(self.spritesCorrendo):
            self.atual = 0

        self.image = self.spritesCorrendo[int(self.atual)]

    def _exibeAnimacaoCorrendo(self):
        if self._animacaoCorrendo:
            self.aceleraDireita()
            self.animar_correndo()
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.flip(self.image, True, False)

    def _exibeAnimacaoCorrendoE(self):
        if self._animacaoCorrendoE:
            self.aceleraEsquerda()
            self.animar_correndo()
            self.image = pygame.transform.flip(self.image, True, False)

    def _exibeAnimacaoPulo(self):
        if self._animacaoPulo == True:
            self.atual += 0.5
            self.__y_velocidade = -20

            if self.atual >= len(self.spritesPulo):
                self.atual = 0
                self.__y_velocidade = 0

                self._animacaoParado = True
                self._animacaoPulo = False

            self.image = self.spritesPulo[int(self.atual)]

    def _exibeAnimacaoEspecial(self):
        if self._animacaoEspecial == True:
            self.atual += 0.5

            if int(self.atual == 4):
                self.__x_velocidade += 5

            if self.atual >= len(self.spritesEspecial):
                self.atual = 0
                self.__x_velocidade = 0

                self._animacaoParado = True
                self._animacaoEspecial = False

            self.image = self.spritesEspecial[int(self.atual)]

    def aceleraDireita(self):
        self.__x_velocidade = 5

    def aceleraEsquerda(self):
        self.__x_velocidade = -5

    def desacelera(self):
        self.__x_velocidade = 0

    def ataque1(self):
        print("aqui")
        self._animacaoParado = False
        self._animacaoEspecial = False
        self._animacaoAtaque1 = True
        self._animacaoParado = False
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False
        self._animacaoPulo = False

    def corre(self):
        self._animacaoParado = False
        self._animacaoAtaque1 = False
        self._animacaoParado = False
        self._animacaoEspecial = False
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False

        if self.rect.x <= 740:
            self._animacaoCorrendo = True
        self._animacaoPulo = False


    def correE(self):
        self._animacaoParado = False
        self._animacaoEspecial = False
        self._animacaoAtaque1 = False
        self._animacaoParado = False
        self._animacaoCorrendo = False

        if self.rect.x >= 0:
            self._animacaoCorrendoE = True
        self._animacaoPulo = False


    def paraDeCorrer(self):
        self._animacaoParado = False
        self._animacaoAtaque1 = False
        self._animacaoParado = True
        self._animacaoEspecial = False
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False

        self.desacelera()


    def paraDeCorrerE(self):
        self._animacaoParado = False
        self._animacaoAtaque1 = False
        self._animacaoEspecial = False
        self._animacaoParado = True
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False

        self.desacelera()

    def pula(self):
        self._animacaoParado = False
        self._animacaoAtaque1 = False
        self._animacaoEspecial = False
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False
        self._animacaoPulo = True

    def ataqueEspecial(self):
        self._animacaoParado = False
        self._animacaoAtaque1 = False
        self._animacaoEspecial = True
        self._animacaoCorrendo = False
        self._animacaoCorrendoE = False
        self._animacaoPulo = False

    def nao_esta_correndo(self):
        return self.__x_velocidade == 0
