import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self, personagem):
        super().__init__(personagem)


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
