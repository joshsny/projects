import gym
import numpy as np
import pickle

from time import sleep


def policy(x):
    return x

env = gym.make("Blackjack-v0")

observation = env.reset()
running_reward = None
reward_sum = 0
episode_number = 0