import torch as t
import numpy as np
import pickle

# Teach a computer to add binary numbers, will reward the agent for the number of correct digits starting from the right. Will use a single 

# hyperparameters
H = 10 # number of hidden units
batch_size = 10
learning_rate = 1e-3
gamma = 0.99 #reward discount factor
decay_rate = 0.99 # decay rate for RMSProp
resume = False # load previously trained model?

number_length = 3
max_int = 1

# useful helper functions
def arrayToInt(x):
    return sum([(max_int+1)**j * x[len(x)-j-1] for j in reversed(range(len(x)))])

print(arrayToInt([0, 1, 1]))



#create list object with necessary attributes and functions
class Numbers:
    def __init__(self):
        self.n1 = np.random.randint(low =0, high = max_int+1, size = number_length)
        self.n2 = np.random.randint(low =0, high = max_int+1, size = number_length)
        self.actions = range(0, )
    



x = Numbers()

print(x.n1, x.n2)
