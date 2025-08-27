import random
from typing import List
from constants import Actions
from q_table import QTable
from grid import Grid


class EpsilonDecay:
    def __init__(self, epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.995):
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay

        self.epsilon = epsilon_start

    def decay(self):
        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)

    def __str__(self):
        return f"{self.epsilon}"


class Agent:
    def __init__(self):
        self.grid: Grid = Grid()
        self.actions: List[int] = Actions.as_list()
        self.q_table: QTable = QTable(self.actions, self.grid.width, self.grid.height)
        self.epsilon_decay = EpsilonDecay(epsilon_decay=0.7)
        self.timestep = None
        self.cumulative_reward = None

        self.reset()

    def step(self) -> bool:
        state = self.grid.player_state
        action = self._choose_action(state)
        (reward, is_end) = self.grid.move(action)
        self.q_table.update_q_value(state, action, reward)

        self.cumulative_reward += reward

        self.timestep += 1

        return is_end

    def _choose_action(self, state) -> int:
        epsilon = self.epsilon_decay.epsilon

        action = None

        if random.random() < epsilon:
            action = random.choice(self.actions)
        else:
            action = self.q_table.get_best_action(state)

        return action

    def reset(self):
        self.grid.reset()
        self.q_table.reset()
        self.timestep = 0
        self.cumulative_reward = 0

        agent.episode_end_report()
        agent.epsilon_strategy_decay()

    def episode_end_report(self):
        print(f"Num Timesteps: {self.timestep}")
        print(f"Epsilon: {self.epsilon_decay.epsilon}")
        print(f"Cumuluative Reward: {self.cumulative_reward}")

    def epsilon_strategy_decay(self):
        self.epsilon_decay.decay()

    def __str__(self):
        return str(self.q_table)


if __name__ == "__main__":
    grid = Grid()
    agent = Agent(grid)
    print(agent)