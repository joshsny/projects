import numpy as np

# hyperparameters
theta = 0.0001
V = np.zeros(101)
V[100] = 1
p = 0.4 # prob of heads
gamma = 1

def sum_calc(s, a):
    if a>min(s, 100-s):
        raise ValueError('Action was not permissible. Check that a is not larger than the maximum possible bet.')
    r = 1 if s+a == 100 else 0
    return 0.5*(r+gamma*V[s+a]) + 0.5*gamma*V[s-a]

delta = 1
#algo
iterations = 0
while delta > theta:
    delta = 0
    for s in range(1, 100):
        v = V[s]
        max_bet = min(s, 100-s)
        V[s] = max([sum_calc(s,a) for a in range(1,max_bet+1)])
        delta = max(delta, np.abs(v-V[s]))
    if iterations % 1000 == 0: print(delta)
    iterations+=1

pi = np.zeros(101)
for s in range(1,100):
    max_bet = min(s, 100-s)
    pi[s] = np.argmax([sum_calc(s,a) for a in range(1,max_bet+1)])

print(pi)