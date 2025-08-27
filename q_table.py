from typing import List
from constants import State, Actions, is_state_in_bounds, update_player_position_from_action


class QTable:
    def __init__(self, actions: List[Actions], grid_width: int, grid_height: int):
        self.actions = actions
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.q_table: List[List[List[float]]] = []
        self.alpha = 0.5 # Learning rate
        self.gamma = 0.9 # Discount factor
        
        self.reset()

    def reset(self):
        self._init_q_table()

    def _init_q_table(self) -> None:
        for y in range(self.grid_width):
            self.q_table.append([])
            for x in range(self.grid_height):
                self.q_table[-1].append([])
                for action in self.actions:
                    self.q_table[-1][-1].append(0.0)

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0)

    def set_q_value(self, state, action, reward):
        self.q_table[(state, action)] = reward

    def get_best_action(self, state: State):
        """This gives the best action. If multiple q values equal each other, just take the one that shows up earlier"""
        action_q_values = self._get_action_q_values_at_state(state)
        return action_q_values.index(max(action_q_values))

    def update_q_value(self, state: State, action: int, immediate_reward: int):
        current_q_value = self.q_table[state.y][state.x][action]
        s_prime = self._get_s_prime(state, action)
        max_q_at_s_prime = self._get_best_q_at_state_s(s_prime)
        self.q_table[state.y][state.x][action] = current_q_value + self.alpha * (immediate_reward + self.gamma * max_q_at_s_prime - current_q_value)

    def _get_best_q_at_state_s(self, state: State) -> float:
        action_q_values = self._get_action_q_values_at_state(state)
        return max(action_q_values)

    def _get_action_q_values_at_state(self, state: State) -> List[float]:
        if is_state_in_bounds(state, self.grid_width, self.grid_height):
            return self.q_table[state.y][state.x]
        else:
            # I chose not to discourage the agent from going oob when choosing a move, 
            # but instead let it get a penalty for trying
            return [0.0, 0.0, 0.0, 0.0]
    
    def _get_s_prime(self, state: State, action: int) -> State:
        return update_player_position_from_action(state.x, state.y, action)

    def __str__(self):
        string = ""
        for y in range(len(self.q_table)):
            for x in range(len(self.q_table[y])):
                for k in range(len(self.q_table[y][x])):
                    string += f"({x}, {y}, {Actions(k).name}): {self.q_table[y][x][k]}, "
                string += "\n"
        return string


if __name__ == "__main__":
    q_table = QTable(Actions.as_list(), 3, 3)
    table = q_table.q_table
    print(table)
    print(q_table._get_s_prime(State(1,1), 3))

