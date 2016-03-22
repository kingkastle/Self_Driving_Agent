import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import QTable
import numpy as np
from collections import namedtuple

######################################
########## Benchmark Agent ###########
######################################
debug = False

if debug:
    import csv
    myfile = open('rewards_smart.csv', 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    reward_per_action = []
#times_reaches_destination = []
#reward_per_trial = []
######################################
######################################

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        State = namedtuple('State','light oncoming left right next_waypoint')
        self.alpha = 0.4
        self.gamma = 0.6
        self.state = State(None,None,None,None,None)
        self.qvalues = {}

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        State = namedtuple('State','light oncoming left right next_waypoint')
        self.state = State(inputs['light'],inputs['oncoming'],inputs['left'],inputs['right'],self.next_waypoint)
        # TODO: Select action according to your policy
        action = QTable.get_action(self.qvalues,self.state)

        # Execute action and get reward
        reward = self.env.act(self, action)
        if debug: reward_per_action.append(float(reward))
        inputs = self.env.sense(self)
        state2 = State(inputs['light'],inputs['oncoming'],inputs['left'],inputs['right'],self.next_waypoint)
        self.qvalues = QTable.update_qvalue(self.qvalues,self.state,action,state2,reward,self.alpha,self.gamma)
        # TODO: Learn policy based on state, action, reward
        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]

def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # set agent to track

    # Now simulate it
    sim = Simulator(e, update_delay=0.01)  # reduce update_delay to speed up simulation
    sim.run(n_trials=100)  # press Esc or close pygame window to quit
    if debug: wr.writerow(reward_per_action)


if __name__ == '__main__':
    run()
