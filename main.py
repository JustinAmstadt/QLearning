from agent import Agent


def evaluate(agent: Agent):
    is_done = False
    while not is_done:
        print(agent.grid)
        print("--------------")
        is_done = agent.step()

    print(agent.grid)
    agent.episode_end_report()

def main():
    agent = Agent()

    total_episodes = 15
    print(f"Total Episodes: {total_episodes}\n")

    for i in range(total_episodes):
        is_done = False
        while not is_done:
            is_done = agent.step()

        agent.episode_end_report()
        agent.reset()
        agent.epsilon_strategy_decay()
        print("--------------")

    evaluate(agent)


if __name__ == "__main__":
    main()
