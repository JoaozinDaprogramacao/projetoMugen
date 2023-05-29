import pygame
from abstracoes.personagens.logicaEscolha import Logica_Escolha
from enums.PersonagensEnum import PersonagensEnum

class Window:
    def __init__(self, logica):
        pygame.init()
        self.window = pygame.display.set_mode((840, 480))
        self.__backround = pygame.image.load("sprite/selecaoPersonagem/background.jpeg")
        self.__backround = pygame.transform.scale(self.__backround, (840, 480))
        self.drawGroup = pygame.sprite.Group()


        self.__logica: Logica_Escolha = logica

        opacidade = 128
        self.__fonte = pygame.font.Font(None, 36)

        self.__display_p1 = pygame.Surface((275, 400))
        self.__display_p1.fill((0, 0, 0))
        self.__display_p1.set_alpha(opacidade)


        self.__display_name_p1 = pygame.Surface((275, 50))
        self.__display_name_p1.fill((128, 128, 128))
        self.__display_name_p1.set_alpha(opacidade)

        self.__display_p2 = pygame.Surface((275, 400))
        self.__display_p2.fill((0, 0, 0))
        self.__display_p2.set_alpha(opacidade)

        self.__display_name_p2 = pygame.Surface((275, 50))
        self.__display_name_p2.fill((128, 128, 128))
        self.__display_name_p2.set_alpha(opacidade)


        self.hashirama = pygame.sprite.Sprite()
        self.hashirama.image = pygame.image.load("sprite/selecaoPersonagem/hash.jpg")
        self.hashirama.image = pygame.transform.scale(self.hashirama.image, (self.hashirama.image.get_width() // 9,
                                                                             self.hashirama.image.get_height() // 9))
        self.hashirama.rect = self.hashirama.image.get_rect(topleft=(300, 50))
        self.drawGroup.add(self.hashirama)

        self.hashiramaInteiro = pygame.sprite.Sprite()
        self.hashiramaInteiro.image = pygame.image.load("sprite/selecaoPersonagem/hashiramaInteiro.png")
        self.hashiramaInteiro.image = pygame.transform.scale(self.hashiramaInteiro.image, (self.hashiramaInteiro.image.get_width() // 2,
                                                                             self.hashiramaInteiro.image.get_height() // 2))

        self.hashiramaInteiro.rect = self.hashiramaInteiro.image.get_rect(topleft=(15, 400 - self.hashiramaInteiro.image.get_height()))
        self.__hashIsVisible = False

        self.sasuke = pygame.sprite.Sprite()
        self.sasuke.image = pygame.image.load("sprite/selecaoPersonagem/sasuke.jfif")
        self.sasuke.image = pygame.transform.scale(self.sasuke.image, (self.sasuke.image.get_width() // 9,
                                                                       self.sasuke.image.get_height() // 9))
        self.sasuke.rect = self.sasuke.image.get_rect(topleft=(458, 50))
        self.drawGroup.add(self.sasuke)

        self.sasukeInteiro = pygame.sprite.Sprite()
        self.sasukeInteiro.image = pygame.image.load("sprite/selecaoPersonagem/sasukeInteiro.png")
        self.sasukeInteiro.image = pygame.transform.scale(self.sasukeInteiro.image,
                                                             (self.sasukeInteiro.image.get_width() // 2,
                                                              self.sasukeInteiro.image.get_height() // 2))

        self.sasukeInteiro.rect = self.sasukeInteiro.image.get_rect(
            topleft=(15, 400 - self.sasukeInteiro.image.get_height()))

        self.__sasukehIsVisible = False


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

    def __desenha_display_escolha(self, p1_nome):
        pygame.draw.rect(self.window, (0, 0, 0), (5, 65, 285, 410), 5)
        self.window.blit(self.__display_p1, (10, 70))
        pygame.draw.rect(self.window, (0, 0, 0), (5, 0, 285, 60), 5)
        self.window.blit(self.__display_name_p1, (10, 5))

        texto_imagem = self.__fonte.render(p1_nome, True, (0, 0, 0))
        self.window.blit(texto_imagem, (15, 15))

        self.__update_display_p1(self.__logica.get_escolha())


        pygame.draw.rect(self.window, (0, 0, 0), (840 - 275 - 10 - 5, 65, 285, 410), 5)
        self.window.blit(self.__display_p2, (840 - 275 - 10, 70))
        pygame.draw.rect(self.window, (0, 0, 0), (840 - 285 - 5, 0, 285, 60), 5)
        self.window.blit(self.__display_name_p1, (840 - 275 - 10, 5))

        texto_imagem = self.__fonte.render("", True, (0, 0, 0))
        self.window.blit(texto_imagem, (200, 300))

    def __convert_enum_personagem_to_string(self, value):
        if value == PersonagensEnum.Hashirama.value:
            return "HASHIRAMA"
        elif value == PersonagensEnum.Sasuke.value:
            return "SASUKE"


    def __update_display_p1(self, value):
        if value == PersonagensEnum.Hashirama.value and not self.__hashIsVisible:
            self.drawGroup.add(self.hashiramaInteiro)
            self.__hashIsVisible = True

        elif value != PersonagensEnum.Hashirama.value and self.__hashIsVisible:
            self.drawGroup.remove(self.hashiramaInteiro)
            self.__hashIsVisible = False


        if value == PersonagensEnum.Sasuke.value and not self.__sasukehIsVisible:
            self.drawGroup.add(self.sasukeInteiro)
            self.__sasukehIsVisible = True

        elif value != PersonagensEnum.Sasuke.value and self.__sasukehIsVisible:
            self.drawGroup.remove(self.sasukeInteiro)
            self.__sasukehIsVisible = False


    def run(self):
        while self.running:
            self.window.blit(self.__backround, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.teclas_input()


            self.__desenha_display_escolha(
                self.__convert_enum_personagem_to_string(self.__logica.get_escolha())
            )

            self.drawGroup.draw(self.window)
            self.indicador_personagem()
            pygame.display.update()
