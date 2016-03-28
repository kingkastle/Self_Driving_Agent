'''
Created on 24/02/2016

@author: rafaelcastillo
'''
import numpy as np
import random

valid_actions = [None, 'forward', 'left', 'right']

def get_action(qvalues,state,epsilon):
    """
    This function uses the current agent state to identify the action that maximizes Q. 
    According to the greedy policy, the final action is selected.
    In case the state is not included in the Q dictionary, it includes such state for All possible actions
    into Q.
    """
    states = [x for x in qvalues if x[0] == state]
    if len(states) > 0:
        qval = [qvalues[x] for x in qvalues if x[0] == state]
        if np.max(qval) != np.min(qval):
            for i,stt in enumerate(states):
                if i == 0: 
                    maxq = qvalues[stt]
                    action = stt[1]
                if qvalues[stt] > maxq: 
                    maxq = qvalues[stt]
                    action = stt[1]
            return action if random.random() < epsilon else random.choice([x for x in valid_actions if x != action])
        else:
            return random.choice(valid_actions)
        
    else:
        """
        In case the state wasn't included in the Q table, the state and corresponding actions are included
        and a random action is used as final.
        """
        for action in valid_actions:
            qvalues[(state,action)] = 0
        return random.choice(valid_actions)
    
def update_qvalue(qvalues,state1,action1,state2,reward,alpha,gamma):
    action2 = get_action(qvalues,state2,1) # Get the best action for state2
    qvalues[(state1,action1)] += np.round(alpha*(reward + gamma*qvalues[(state2,action2)] - qvalues[(state1,action1)]),2)
    return qvalues
