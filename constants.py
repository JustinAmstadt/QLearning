from dataclasses import dataclass
from enum import IntEnum
from typing import List


@dataclass
class State:
    x: int
    y: int

    def get_tuple(self):
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


class Actions(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    @classmethod
    def as_list(cls) -> List['Actions']:
        return [Actions.UP, Actions.DOWN, Actions.LEFT, Actions.RIGHT]


def update_player_position_from_action(x, y, action: int):
    if Actions.UP.value == action:
        y -= 1
    elif Actions.DOWN.value == action:
        y += 1
    elif Actions.LEFT.value == action:
        x -= 1
    elif Actions.RIGHT.value == action:
        x += 1

    return State(x, y)

def is_state_in_bounds(state: State, width, height):
    return 0 <= state.x < width and 0 <= state.y < height