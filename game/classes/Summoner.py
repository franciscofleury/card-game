from classes.Card import Card
from typing import Dict
from game.utils import getStandartModifiers
from game.classes import Local, ActionTemplate, Action
from my_types import Movement

class Summoner:

    def __init__(self, champion: str, card: Card) -> None:
        self.champion: str = champion
        self.forca: int = 60
        self.card: Card = card
        self.vivo: bool = True
        self.modificadores: Dict[str, float] = getStandartModifiers()
        self.local: Local | None = None
    
    def setAction(self, action: ActionTemplate, movement: Movement = 0):
        self.action = Action(ActionTemplate, movement)
    

        