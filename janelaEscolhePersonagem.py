import pygame
from abstracoes.personagens.logicaEscolha import Logica_Escolha
from enums.PersonagensEnum import PersonagensEnum

class Window:
    def __init__(self, logica):
        pygame.init()
        self.window = pygame.display.set_mode((840, 480))
        self.drawGroup = pygame.sprite.Group()

        self.__logica: Logica_Escolha = logica
        self.hashirama = pygame.sprite.Sprite()
        self.hashirama.image = pygame.image.load("sprite/selecaoPersonagem/hash.jpg")
        self.hashirama.image = pygame.transform.scale(self.hashirama.image, (self.hashirama.image.get_width() // 9,
                                                                             self.hashirama.image.get_height() // 9))
        self.hashirama.rect = self.hashirama.image.get_rect(topleft=(50, 50))
        self.drawGroup.add(self.hashirama)


        self.sasuke = pygame.sprite.Sprite()
        self.sasuke.image = pygame.image.load("sprite/selecaoPersonagem/sasuke.jfif")
        self.sasuke.image = pygame.transform.scale(self.sasuke.image, (self.sasuke.image.get_width() // 9,
                                                                       self.sasuke.image.get_height() // 9))
        self.sasuke.rect = self.sasuke.image.get_rect(topleft=(170, 50))
        self.drawGroup.add(self.sasuke)


        self.running = True

    def indicador_personagem(self):
        if self.__logica.get_escolha() == PersonagensEnum.Hashirama.value:
            indicator_rect = self.hashirama.rect.inflate(10, 10)
            pygame.draw.rect(self.window, (255, 0, 0), indicator_rect, 3)
        elif self.__logica.get_escolha() == PersonagensEnum.Sasuke.value:
            indicator_rect = self.sasuke.rect.inflate(10, 10)
            pygame.draw.rect(self.window, (255, 0, 0), indicator_rect, 3)

    def teclas_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.__logica.set_escolha(PersonagensEnum.Hashirama.value)
        elif keys[pygame.K_RIGHT]:
            self.__logica.set_escolha(PersonagensEnum.Sasuke.value)
        elif keys[pygame.K_RETURN]:
            if self.__logica.get_escolha():
                print("Personagem selecionado:", self.__logica.get_escolha())
                self.running = False

    def run(self):
        while self.running:
            self.window.fill((105, 105, 105))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.teclas_input()

            self.drawGroup.draw(self.window)
            self.indicador_personagem()
            pygame.display.update()
