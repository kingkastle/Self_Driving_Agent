'''
Created on 24/02/2016

@author: rafaelcastillo
'''
import numpy as np

valid_actions = [None, 'forward', 'left', 'right']

def get_action(qvalues,state):
    """
    This function uses the current agent state to identify the action that maximizes Q
    In case the state is not included in the Q dictionary, it includes such state for All possible actions
    into Q.
    """
    states = [x for x in qvalues if x[0] == state]
    if len(states) > 0:
        #return getattr(state, 'next_waypoint')
        qval = [qvalues[x] for x in qvalues if x[0] == state]
        if np.max(qval) == np.min(qval): return getattr(state, 'next_waypoint') # All action have same Q, so follow the planner
        for i,stt in enumerate(states):
            if i == 0: 
                maxq = qvalues[stt]
                action = stt[1]
            if qvalues[stt] > maxq: 
                maxq = qvalues[stt]
                action = stt[1]
        return  action
    else:
        """
        In case the state wasn't included in the Q table, the state and corresponding actions are included
        and the planner action is used as final.
        """
        for action in valid_actions:
            qvalues[(state,action)] = 0
        return getattr(state, 'next_waypoint')
    
def update_qvalue(qvalues,state1,action1,state2,reward,alpha,gamma):
    action2 = get_action(qvalues,state2) # Get the best action for state2
    qvalues[(state1,action1)] += np.round(alpha*(reward + gamma*qvalues[(state2,action2)] - qvalues[(state1,action1)]),2)
    return qvalues