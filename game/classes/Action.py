from game.classes import ActionTemplate
from my_types import Movement

class Action:

    def __init__(self, action: ActionTemplate, movement: Movement) -> None:
        self.action: ActionTemplate = action
        self.movement: Movement = movement        