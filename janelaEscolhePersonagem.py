import pygame


class Window:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((840, 480))

        self.drawGroup = pygame.sprite.Group()
        self.hashirama = pygame.sprite.Sprite()
        self.hashirama.image = pygame.image.load("sprite/selecaoPersonagem/hash.jpg")
        self.hashirama.image = pygame.transform.scale(self.hashirama.image, (self.hashirama.image.get_width() // 9,
                                                                             self.hashirama.image.get_height() // 9))
        self.hashirama.rect = pygame.Rect(50, 50, 100, 100)
        self.drawGroup.add(self.hashirama)


        self.sasuke = pygame.sprite.Sprite()
        self.sasuke.image = pygame.image.load("sprite/selecaoPersonagem/sasuke.jfif")
        self.sasuke.image = pygame.transform.scale(self.sasuke.image, (self.sasuke.image.get_width() // 9,
                                                                       self.sasuke.image.get_height() // 9))
        self.sasuke.rect = pygame.Rect(200, 50, 100, 100)
        self.drawGroup.add(self.sasuke)


        self.personagem_selecionado = None
        self.running = True

    def run(self):
        while self.running:
            self.window.fill((105, 105, 105))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.running = False

                    if self.hashirama.rect.collidepoint(mouse_pos):
                        self.personagem_selecionado = "Hashirama"
                        print('hashirama')

                    elif self.sasuke.rect.collidepoint(mouse_pos):
                        self.personagem_selecionado = "Sasuke"
                        print('sasuke')

            self.drawGroup.draw(self.window)
            pygame.display.update()

        pygame.quit()


JANELA = Window()
JANELA.run()
