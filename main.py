import pygame
from Models.personagens.life import Life
from Models.personagens.Personagem import Personagem
from janelaEscolhePersonagem import Window
from abstracoes.animacaoEntrada import anima_entrada
from abstracoes.personagens.logicaEscolha import Logica_Escolha

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("projeto mugen")

drawGroup = pygame.sprite.Group()

life = Life(drawGroup)

p1: Personagem = None
p2: Personagem = None

background = pygame.image.load("sprite/hCUwLQ.png")

relogio = pygame.time.Clock()
gameLoop = True

largura = 840

preto = (0, 0, 0)

faixa_x = -3000
faixa_y = 140

velocidade = 10

anima_entrada_value = True

if __name__ == "__main__":
    logica = Logica_Escolha(p1, p2, drawGroup)
    janelaEscola = Window(logica)
    janelaEscola.run()

    p1 = logica.get_p1()
    p2 = logica.get_p2()

    endereco_p1, endereco_p2 = logica.get_logs_p1_p2()

    img_p1_selec = pygame.image.load(endereco_p1)
    img_p1_selec = pygame.transform.scale(img_p1_selec, (img_p1_selec.get_width() // 6,
                                                         img_p1_selec.get_height() // 6))

    img_p2_selec = pygame.image.load(endereco_p2)
    img_p2_selec = pygame.transform.scale(img_p2_selec, (img_p2_selec.get_width() // 6,
                                                         img_p2_selec.get_height() // 6))


    if p1 == None:
        exit()

    pygame.init()
    while gameLoop:
        relogio.tick(60)
        display.blit(background, [0, 0])

        if not anima_entrada_value:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        p1.corre()

                    if event.key == pygame.K_LEFT:
                        p1.correE()

                    if event.key == pygame.K_z:
                        p1.ataque1()

                    if event.key == pygame.K_x:
                        keys = pygame.key.get_pressed()
                        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                            p1.ataqueEspecial()

                    if event.key == pygame.K_SPACE:
                        keys = pygame.key.get_pressed()
                        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                            p1.pula()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        p1.paraDeCorrer()

                    if event.key == pygame.K_LEFT:
                        p1.paraDeCorrerE()

        faixa_x, anima_entrada_value = anima_entrada(faixa_x, faixa_y,
                                                     anima_entrada_value, velocidade, preto, display,
                                                     img_p1_selec, img_p2_selec)

        drawGroup.update()
        drawGroup.draw(display)

        pygame.display.update()
