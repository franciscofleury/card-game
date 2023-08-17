from typing import Callable, List, Tuple
from classes.Card import Card

def valid_champion(f: Callable[[any,List[Tuple[Card, str]], List[Tuple[Card, str]]],None]):
    
    def wrap(self: any,blueSide: List[Tuple[Card, str]], redSide: List[Tuple[Card, str]]):
        if len(blueSide) != 5 or len(redSide) != 5:
            print("Número de Summoners inválido")
            return
        allChamp = blueSide
        allChamp.extend(redSide)
        for champ in allChamp:
            if champ[1] not in champ[0].champions:
                print(f"Campeão {champ[1]} inexistente nos campeões da carta. [{champ[0].champions[0]},{champ[0].champions[1]}]")
                return
        f(self,blueSide,redSide)
    return wrap