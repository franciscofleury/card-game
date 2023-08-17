from typing import List, Literal, Tuple, Dict
from classes import User, Card
from game.classes import Summoner, Local, getInitialLocals, ActionTemplate, getStandartActions, Rota
from game.wrappers.championValidator import valid_champion
from my_types import LocalType

Status = Literal[-1,0,1]


class GameManager:

    def __init__(self, blue: User, red: User) -> None:
        self.__blue: User = blue
        self.__red: User = red
        self.__locais: List[Local] = getInitialLocals()
        self.__victory: Status = 0
        self.__started = False
        self.__possibleActions: Dict[LocalType, List[ActionTemplate]] = getStandartActions()

    @valid_champion
    def setSummoners(self, blueSide: List[Tuple[Card, str]], redSide: List[Tuple[Card, str]]):
        self.__blueSide = [Summoner(x[1], x[0]) for x in blueSide]
        self.__redSide = [Summoner(x[1], x[0]) for x in redSide]

    def start_game(self):
        for champ in self.__blueSide:
            n = ["top", "jungle", "mid", "adc", "sup"].index(champ.card.role)
            champ.local = self.__locais[n]
            self.__locais[n].blueSideChampions.append(champ)
        for champ in self.__redSide:
            n = ["top", "jungle", "mid", "adc", "sup"].index(champ.card.role)
            champ.local = self.__locais[n]
            self.__locais[n].redSideChampions.append(champ)
        self.__started = True

    def get_actions(self):
        for champ in self.__blueSide:
            print(f"Escolha uma ação para {champ.champion}:")
            local = "jungle"
            if champ.local.isinstance(Rota):
                local = "rota"
            for a in self.__possibleActions[local]:
                print(a)
            action = input("Digite uma ação válida: ")
