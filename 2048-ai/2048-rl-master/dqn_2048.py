import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.core import Processor

from gym_2048.envs import Game2048

ENV_NAME = 'game-2048-v0'

class Processor2048(Processor):
    def __init__(self):
        self.powers = {2**i:i for i in range(12)} 
        self.powers[0] = 0

    def flatten(self, l):
        return [item for sublist in l for item in sublist]    

    def process_observation(self, observation):
        #return self.flatten(observation)
        obs = []
        for row in observation:
            for col in row:
                o = [0]*12
                o[self.powers[col]] = 1
                obs += o

        return obs


class LegalDQNAgent(DQNAgent):
    def __init__(self, env=None, *args, **kwargs):
        super(LegalDQNAgent, self).__init__(*args, **kwargs)
        self.env = env


    def forward(self, observation):
        # Select an action from the available moves.
        state = self.memory.get_recent_state(observation)
        q_values_t = self.compute_q_values(state)
        q_values = []
        moves_available = self.env.moves_available()
        for q, available in zip(q_values_t, moves_available):
            if available:
                q_values += [q]
            else:
                q_values += [-np.inf]
        q_values = np.array(q_values)
        assert q_values.shape[0] > 0

        if self.training:
            action = self.policy.select_action(q_values=q_values)
        else:
            action = self.test_policy.select_action(q_values=q_values)

        # Book-keeping.
        self.recent_observation = observation
        self.recent_action = action

        return action



# Get the environment and extract the number of actions.
s = 123
env = Game2048(seed=s)
np.random.seed(s)
nb_actions = env.action_space.n

# Next, we build a very simple model.
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
processor = Processor2048()
memory = SequentialMemory(limit=1000000, window_length=1)
policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1, value_min=.01, value_test=.05,
                            nb_steps=500000)
dqn = LegalDQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1,
               target_model_update=1e-2, enable_double_dqn=True, policy=policy,
               processor=processor, env=env)
dqn.compile(Adam(lr=1e-4), metrics=['mse'])

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
dqn.fit(env, nb_steps=1750000, visualize=False, verbose=2, log_interval=10000)

# After training is done, we save the final weights.
dqn.save_weights('dqn_{}_weights.h5f'.format(ENV_NAME), overwrite=True)

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=10, visualize=True)
