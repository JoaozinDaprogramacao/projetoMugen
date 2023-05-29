import pygame

class Projetil(pygame.sprite.Sprite):
    def __init__(self, sprites_explosao, velocidade, *groups):
        super().__init__(*groups)

        self.__sprites_explosao = sprites_explosao

        self.__velocidade = velocidade

        self.atual = 0
        self.image = self.__sprites_explosao[self.atual]
        self.rect = self.image.get_rect()

        self.__pos_x = -200
        self.__pos_y = -200

        self.rect = self.image.get_rect(
            topleft=(self.__pos_x, self.__pos_y))


        self.__animar = False


    def update(self, *args):
        if self.__animar:
            self.__anima()

        print(f"x: {self.__pos_x}")
        print(f"y: {self.__pos_y}")

    def set_pos(self, pos):
        self.__pos_x = pos[0]
        self.__pos_y = pos[1] - self.rect.y
        self.rect = self.image.get_rect(
            topleft=(self.__pos_x, self.__pos_y))

    def lanca(self):
        self.__animar = True

    def __anima(self):
        if self.__animar == True:
            print(self.__sprites_explosao[int(self.atual)])
            self.atual += 0.2
            self.__pos_x += self.__velocidade
            if self.atual >= len(self.__sprites_explosao):
                self.atual = 0

                self.set_pos((-200, -200))

                self.__animar = False
            self.image = self.__sprites_explosao[int(self.atual)]
