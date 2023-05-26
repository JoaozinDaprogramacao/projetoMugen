from enums.PersonagensEnum import PersonagensEnum
from Models.Hashirama import Hashirama
from Models.Bils import Bils


class Logica_Escolha:
    def __init__(self, p1, drawGroup):
        self.__escolha = None
        self.__p1 = p1
        self.__drawGroup = drawGroup


    def set_escolha(self, escolha):
        self.__escolha = escolha

    def get_escolha(self):
        return self.__escolha

    def get_p1(self):
        if self.__escolha == PersonagensEnum.Hashirama.value:
            self.__p1 = Hashirama(self.__drawGroup)

        elif self.__escolha == PersonagensEnum.Sasuke.value:
            self.__p1 = Bils(self.__drawGroup)

        return self.__p1