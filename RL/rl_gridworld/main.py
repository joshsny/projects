import numpy as np
from time import sleep
import random

act_dict = {'UP': np.array([-1,0]), 'DOWN': np.array([1, 0]), 'LEFT': np.array([0,-1]), 'RIGHT': np.array([0,1])}
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
A = np.array([0,1])
Aprime = np.array([4,1])
B = np.array([0,3])
Bprime = np.array([2,3])
gamma = 0.9
alpha = 0.05
epsilon = 0.01
Q = np.zeros([5,5]) + 0 #optimistic starting values to encourage exploration

def step(prev_pos, action):
    i = prev_pos[0]
    j = prev_pos[1]
    
    if i == 0 and action == 'UP':
        return prev_pos, -1
    elif j==0 and action == 'LEFT':
        return prev_pos, -1
    elif i==4 and action == 'DOWN':
        return prev_pos, -1
    elif j==4 and action == 'RIGHT':
        return prev_pos, -1 
    else:
        pos = prev_pos + act_dict[action]
    
    #check if pos is one of the special positions
    if (pos == A).all():
        return Aprime, 10
    elif (pos == B).all():
        return Bprime, 5
    else:
        return  pos, 0
    

def policy(pos):
    i = pos[0]
    j = pos[1]
    greedy_action = np.argmax([Q[max(i-1,0),j], Q[min(i+1, 4), j], Q[i, max(j-1, 0)], Q[i, min(j+1,4)]])
    action = actions[greedy_action] if np.random.randn() < epsilon else random.choice(actions)
    return action

def updateQ(prev_pos,prev_action, pos, reward):
    throughA = [[[0,0], 'RIGHT'], [[0,2], 'LEFT'], [[1,1], 'UP']]
    throughB = [[[2,2], 'RIGHT'], [[2,3], 'LEFT'], [[3,3], 'UP']]
    pair = [prev_pos.tolist(),prev_action]
    if throughA.count(pair) > 0:
        i = A[0]; j = A[1]
    elif throughB.count(pair) > 0:
        i = B[0]; j = B[1]
    else:
        i = pos[0]; j = pos[1]
    greedy_reward = np.max([Q[max(i-1,0),j], Q[min(i+1, 4), j], Q[i, max(j-1, 0)], Q[i, min(j+1,4)]])
    Q[i,j] += alpha*(reward + gamma*(greedy_reward - Q[i,j]))
    

def game():
    init_pos = np.array([4,4])
    init_action = 'UP'
    pos, action = init_pos, init_action
    reward_sum = 0
    step_count = 0
    while step_count <  10**6:
        #sleep(0.2)
        prev_pos, prev_action = pos, action
        action = policy(pos)
        pos, reward = step(pos, action)
        updateQ(prev_pos,prev_action, pos, reward)
        reward_sum = 0.01*reward + 0.99*reward_sum
        #bookkeeping
        step_count += 1
        if step_count % 10**5 == 0:
            print(reward_sum)
    print(Q)
        

game()

