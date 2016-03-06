# Self-Driving Agent

## Summary
The intention of this exercise is to teach a self-driving to automatically drive to reach the final destination maximizing rewards. [Q learning algorithm](http://www.cse.unsw.edu.au/~cs9417ml/RL1/algorithms.html) is implemented.

## Key Factors:
#### Rewards:
Any time the agent acts, a reward is reached, the possible rewards are:
 - 10: Agent reaches destination
 - 2: Agent action is valid and equals the next_waypoint() policy
 - 1: Agent action is None
 - 0.5: Agent action is valid but is not the next_waypoint() policy
 - -1: Agent action is not valid

#### Planner:
Agent uses a planner to reach destination, this planner identifies the next waypoints agent should follow to reach destination in a grid environment. However planner is limited since the process to find the optimun waypoints first checks for optimal waypoints in the North-South direction and, in case None is found, then in the East-West direction. As a consequence, in cases where there are two optimal waypoints, only the waypoint situated in the North-South direction is reported.

### Results:
In the following graph it is represented the total number of different rewards for a simulation of 100 trials for an "intelligent" and "non intelligent" agent. The intelligent agent uses the Q equation to identify the best actions while non-intelligent agent simply follows those actions towards the next waypoint.

In the way rewards are defined, it just depend of the nature of the movement and in both cases, intelligent and non-intelligent, follows the planner for the next waypoint, so it is not expect the intelligent agent to be faster than the non-trained agent reaching destination, but an overall increase of the rewards obtained, as the following graph shows:

![Rewards](rewards.png?raw=true)