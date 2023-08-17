from typing import Optional, List
from game.classes import Summoner
from game.classes import Objetivo

class Local:

    def __init__(self, name: str, upperViz: Optional['Local'], lowerViz: Optional['Local']) -> None:
        self.name: str = name
        self.upperViz: Optional[Local] = upperViz
        self.lowerViz: Optional[Local] = lowerViz
        self.blueSideChampions: List[Summoner] = []
        self.redSideChampions: List[Summoner] = []

class Rota(Local):

    def __init__(self, name: str, upperViz: Local | None, lowerViz: Local | None) -> None:
        super().__init__(name, upperViz, lowerViz)
        self.blueTurrets: List[int] = [5,5,5,5,5]
        self.redTurrets: List[int] = [5,5,5,5,5]
        self.wave: int = 0

class Jungle(Local):

    def __init__(self, name: str, upperViz: Local | None, lowerViz: Local | None) -> None:
        super().__init__(name, upperViz, lowerViz)
        self.objetivo: Objetivo | None = None
        self.visao: int = 0

def getInitialLocals() -> List[Local]:
    top = Rota("top", None, None)
    jungle_top = Jungle("jg_top", top, None)
    mid = Rota("mid", jungle_top, None)
    jungle_bot = Jungle("jg_bot", mid, None)
    bot = Rota("bot", jungle_bot, None)
    top.lowerViz = jungle_bot
    jungle_top.lowerViz = mid
    mid.lowerViz = jungle_bot
    jungle_bot.lowerViz = bot
    return [top,jungle_bot,mid,jungle_bot,bot]  