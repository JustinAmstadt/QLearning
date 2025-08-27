from constants import Actions, State, is_state_in_bounds, update_player_position_from_action


class Cell:
    def __init__(self, x, y, reward, is_end=False):
        self.x = x
        self.y = y
        self.reward = reward
        self.is_end = is_end

    def step_on(self) -> tuple[int, bool]:
        return (self.reward, self.is_end)

    def __str__(self):
        return f"[{self.reward}]"

class Grid:
    def __init__(self):
        self.width = 3
        self.height = 3
        self.cells: list[list[Cell]] = [
            [Cell(0, 0, 0), Cell(0, 1, 0), Cell(0, 2, 5, is_end=True)], 
            [Cell(1, 0, 0), Cell(1, 1, -10), Cell(1, 2, -10)], 
            [Cell(2, 0, 0), Cell(2, 1, 0), Cell(2, 2, 0)], 
        ]
        self.player_state = None

        self.reset()

    def render(self):
        for row in self.cells:
            print(" ".join(str(cell) for cell in row))
        print(f"Player is at ({self.player_x}, {self.player_y})")

    def reset(self):
        self.player_state = State(1, 2)

    def move(self, action: int) -> tuple[int, bool]:
        old_x = self.player_state.x
        old_y = self.player_state.y

        self.player_state = update_player_position_from_action(self.player_state.x, self.player_state.y, action)

        reward = 0
        is_done = False

        if not self._is_in_bounds(self.player_state):
            self.player_state.x = old_x
            self.player_state.y = old_y
            reward = -10
            is_done = False
        else: 
            (reward, is_done) = self.cells[self.player_state.y][self.player_state.x].step_on()

        # Don't penalize the final step to goal
        if not is_done:
            reward -= self._get_efficiency_penalty()

        return (reward, is_done)

    def _get_efficiency_penalty(self) -> float:
        return -0.5

    def _is_in_bounds(self, state: State) -> bool:
        return is_state_in_bounds(state, self.width, self.height)

    def __str__(self):
        result = []
        for y in range(len(self.cells)):
            row_str = []
            for x in range(len(self.cells[y])):
                cell = self.cells[y][x]
                if self.player_state and self.player_state.x == x and self.player_state.y == y:
                    row_str.append(f"[P{cell.reward:2}]")
                else:
                    row_str.append(f"[{cell.reward:3}]")
            result.append(" ".join(row_str))
        return "\n".join(result)

if __name__ == "__main__":
    grid = Grid()
    grid.render()