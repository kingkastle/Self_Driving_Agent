# Self-Driving Agent

## Summary
The intention of this exercise is to teach a self-driving car (Agent) to automatically drive to reach the final destination maximizing rewards. [Q learning algorithm](http://www.cse.unsw.edu.au/~cs9417ml/RL1/algorithms.html) is implemented.

## Key Factors:
#### Rewards:
Any time the agent acts, a reward is reached, the possible rewards are:
 - 10:  Agent reaches destination
 - 2:   Agent action is valid and equals the next_waypoint() policy
 - 1:   Agent action is None
 - 0.5: Agent action is valid but is not the next_waypoint() policy
 - -1:  Agent action is not valid

#### Planner:
Agent uses a planner to reach destination, this planner identifies the next waypoints agent should follow to reach destination in a grid environment. However planner is limited since the process to find the optimun waypoints firstly checks for optimal waypoints in the North-South direction and, in case None is found, then in the East-West direction. As a consequence, in cases where there are two optimal waypoints, only the waypoint in the North-South direction is reported.

### Results:
In the following graph it is represented the total number of different rewards for a simulation of 100 trials for an "intelligent" and "non intelligent" agent. The intelligent agent uses the Q equation to identify the optimum actions while non-intelligent agent simply follows those actions towards the next waypoint indicated by the Planner.

In the way rewards are defined, since an None action has a rewards of 1, while an action that is valid but not to the next_waypoint is rewarded with 0.5, it is not expected the intelligent agent to be faster than the non-trained agent reaching destination, but an overall increase of the rewards obtained, as the following graph shows:

![Rewards](rewards.png?raw=true)