import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.__sprites = []
        for i in range(1, 7):
            self.__sprites.append(pygame.image.load(f"sprite/barraVida/{i}.png"))

        print(len(self.__sprites))
        self.atual = 5
        self.image = self.__sprites[self.atual]
        self.rect = pygame.Rect(0, 0, 247, 62)
