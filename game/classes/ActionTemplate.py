from typing import Dict, List
from my_types import LocalType

class ActionTemplate:

    def __init__(self, name: str, modificadores: Dict[str, float], move: bool) -> None:
        self.name: str = name
        self.modificadores: Dict[str, float] = modificadores
        self.move = move

def getStandartActions() -> Dict[LocalType, List[ActionTemplate]]:
    return {"rota": [
                ActionTemplate("puxar", {"ataque": 0.2, "defesa": -0.2, "push": 0.5}, False),
                ActionTemplate("matar", {"ataque": 0.5, "defesa": -0.2, "push": 0}, True),
                ActionTemplate("safe", {"ataque": -0.2, "defesa": 0.5, "push": -0.2}, False),
            ],
            "jungle": [
                ActionTemplate("farmar", {"ataque": 0.2, "defesa": -0.2, "push": 0.5}, False),
                ActionTemplate("matar", {"ataque": 0.5, "defesa": -0.2, "push": 0}, True),
                ActionTemplate("visao", {"ataque": -0.2, "defesa": 0.5, "push": -0.2}, False),
            ]}