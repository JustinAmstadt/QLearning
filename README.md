# QLearning

## Overview

This is a showcase of a super basic grid environment with a q table + epsilon greedy algorithm written completely from scratch.

I also implemented an efficiency penalty to encourage the fewest amount of steps possible to the solution.

## Output

```
Total Episodes: 15
Num Timesteps: 5
Epsilon: 1.0
Cumuluative Reward: -7.0
--------------
Num Timesteps: 8
Epsilon: 0.7
Cumuluative Reward: -38.5
--------------
Num Timesteps: 6
Epsilon: 0.48999999999999994
Cumuluative Reward: -37.5
--------------
Num Timesteps: 29
Epsilon: 0.3429999999999999
Cumuluative Reward: -99.0
--------------
Num Timesteps: 8
Epsilon: 0.24009999999999992
Cumuluative Reward: -18.5
--------------
Num Timesteps: 19
Epsilon: 0.16806999999999994
Cumuluative Reward: -44.0
--------------
Num Timesteps: 5
Epsilon: 0.11764899999999995
Cumuluative Reward: 3.0
--------------
Num Timesteps: 10
Epsilon: 0.08235429999999996
Cumuluative Reward: -9.5
--------------
Num Timesteps: 5
Epsilon: 0.05764800999999997
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.04035360699999998
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.028247524899999984
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.019773267429999988
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.01384128720099999
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.01
Cumuluative Reward: 3.0
--------------
Num Timesteps: 5
Epsilon: 0.01
Cumuluative Reward: 3.0
--------------
[  0] [  0] [  5]
[  0] [-10] [-10]
[  0] [P 0] [  0]
--------------
[  0] [  0] [  5]
[  0] [-10] [-10]
[P 0] [  0] [  0]
--------------
[  0] [  0] [  5]
[P 0] [-10] [-10]
[  0] [  0] [  0]
--------------
[P 0] [  0] [  5]
[  0] [-10] [-10]
[  0] [  0] [  0]
--------------
[  0] [P 0] [  5]
[  0] [-10] [-10]
[  0] [  0] [  0]
--------------
[  0] [  0] [P 5]
[  0] [-10] [-10]
[  0] [  0] [  0]
Num Timesteps: 5
Epsilon: 0.01
Cumuluative Reward: 3.0
```