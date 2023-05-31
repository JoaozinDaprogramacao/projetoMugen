from enums.PersonagensEnum import PersonagensEnum
from enums.Players import Players
from Models.personagens.Hashirama import Hashirama
from Models.personagens.Bils import Bils


class Logica_Escolha:
    def __init__(self, p1, p2, drawGroup):
        self.__escolha_p1 = None
        self.__escolha_p2 = None
        self.__p1 = p1
        self.__p2 = p2
        self.__drawGroup = drawGroup
        self.__press_enter = False


    def set_escolha_p1(self, escolha):
        self.__escolha_p1 = escolha

    def set_escolha_p2(self, escolha):
        self.__escolha_p2 = escolha

    def press_enter(self):
        self.__press_enter = True

    def get_escolha_p1(self):
        return self.__escolha_p1

    def get_escolha_p2(self):
        return self.__escolha_p2

    def get_p1(self):
        if self.__press_enter:
            if self.__escolha_p1 == PersonagensEnum.Hashirama.value:
                self.__p1 = Hashirama(self.__drawGroup, player = Players.p1.value)

            elif self.__escolha_p1 == PersonagensEnum.Sasuke.value:
                self.__p1 = Bils(self.__drawGroup, player = Players.p1.value)

            return self.__p1

    def get_p2(self):
        if self.__press_enter:
            if self.__escolha_p2 == PersonagensEnum.Hashirama.value:
                self.__p2 = Hashirama(self.__drawGroup, player = Players.p2.value)

            elif self.__escolha_p2 == PersonagensEnum.Sasuke.value:
                self.__p2 = Bils(self.__drawGroup, player = Players.p2.value)

            return  self.__p2

    def get_logs_p1_p2(self):
        if self.__press_enter:
            p1 = ""
            p2 = ""
            if self.__escolha_p1 == PersonagensEnum.Hashirama.value:
                p1 = "sprite/selecaoPersonagem/hashirama/FundoHashirama.jfif"
                p2 = "sprite/selecaoPersonagem/bills/FundoBills.jpg"

            elif self.__escolha_p1 == PersonagensEnum.Sasuke.value:
                p2 = "sprite/selecaoPersonagem/hashirama/FundoHashirama.jfif"
                p1 = "sprite/selecaoPersonagem/bills/FundoBills.jpg"

            return p1, p2