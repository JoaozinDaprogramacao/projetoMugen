import pygame

def controla_p1(event, p1):

    if event.type == pygame.KEYDOWN:
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



def controla_p2(event, p2):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            p2.corre()

        if event.key == pygame.K_a:
            p2.correE()

        if event.key == pygame.K_j:
            p2.ataque1()

        if event.key == pygame.K_k:
            keys = pygame.key.get_pressed()
            if not (keys[pygame.K_a] or keys[pygame.K_d]):
                p2.ataqueEspecial()

        if event.key == pygame.K_l:
            keys = pygame.key.get_pressed()
            if not (keys[pygame.K_a] or keys[pygame.K_d]):
                p2.pula()

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            p2.paraDeCorrer()

        if event.key == pygame.K_a:
            p2.paraDeCorrerE()