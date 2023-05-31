from Models.personagens.Personagem import Personagem
from Models.projeteis.Projeteis import Projetil

class Personagem_com_Projetil(Personagem):
    def __init__(self, player,projetil, indice_parado, sprites_parado, sprites_ataque, sprites_correndo, sprites_pulo,
                 sprites_especial, ground, *groups):
        super().__init__(player, indice_parado, sprites_parado, sprites_ataque, sprites_correndo, sprites_pulo,
                         sprites_especial, ground, *groups)


        self.__projetil: Projetil= projetil

        self.__lanca = False


    def update(self, *args):
        super().update()
        self.__projetil.update()


    def _exibeAnimacaoEspecial(self):
        if self._animacaoEspecial == True:
            self.atual += 0.5

            if self.atual >= len(self.spritesEspecial):
                self.atual = 0

                self.__projetil.set_pos((self.rect.x + self.rect.width + 20,
                                         self.rect.y - self.rect.height))

                self.__projetil.lanca()

                self._animacaoParado = True
                self._animacaoEspecial = False

            self.image = self.spritesEspecial[int(self.atual)]