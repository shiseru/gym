import gym
import sys
from gym.envs.registration import register
"""
the fastest steps to reach goal in game ForzenIce
"""

env = gym.make('FrozenLake-v0') 

try:
    register(
        id='FrozenLakeNotSlippery-v0',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name' : '4x4', 'is_slippery': False}
    )
except gym.error.Error:
    pass

env = gym.make('FrozenLakeNotSlippery-v0') 
env.reset() 
env.render()

actions = [1, 1, 2, 1, 2, 2] # left=0、down=1、right=2、up=3

for action in actions:
    step=env.step(action)
    print(step)
    env.render()
