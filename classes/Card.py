from typing import List
from .Player import Player
from my_types import Role

class Card:
    
    def __init__(self, points: int, champions: List[str], role: Role, player: Player) -> None:
        self.points: int = points
        self.champions: List[str] = champions
        self.role: Role = role
        self.player: Player = player

