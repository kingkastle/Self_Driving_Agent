import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import QTable
import numpy as np
from collections import namedtuple
import pandas

######################################
########## Benchmark Agent ###########
######################################
debug = True
df_results = pandas.DataFrame(columns = ['Trial','Movement','Performance'])
trial = 1
nrow = 1
movement = 1

if debug:  myfile = open('rewards_smart_alpha06gamma08_09epsilon.csv', 'w')
######################################
######################################

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        State = namedtuple('State','light next_waypoint')
        self.alpha = 0.5
        self.gamma = 0.3
        self.epsilon = 0.9
        self.state = State(None,None)
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
        State = namedtuple('State','light next_waypoint')
        self.state = State(inputs['light'],self.next_waypoint)
        # TODO: Select action according to your policy
        action = QTable.get_action(self.qvalues,self.state,self.epsilon)

        # Execute action and get reward
        reward = self.env.act(self, action)
        if debug: myfile.write(str(float(reward)) + "\n")
        inputs = self.env.sense(self)
        state2 = State(inputs['light'],self.next_waypoint)
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
    sim = Simulator(e, update_delay=0.001)  # reduce update_delay to speed up simulation
    sim.run(n_trials=800)  # press Esc or close pygame window to quit
    if debug: myfile.close()


if __name__ == '__main__':
    run()