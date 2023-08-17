from typing import List
from .Card import Card

class User:
    
    def __init__(self, name: str, cards: List[Card]) -> None:
        self.name: str = name
        self.inventory: List[Card] = cards