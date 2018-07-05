import gym

env = gym.make('FrozenLake-v0')
# env.reset()
# env.render()
#
# print(env.action_space)
#env.render()
score = 0

for x in range(10000):
    env.reset()
    for _ in range (100):
        # obs, rew, done, info = env.step(env.action_space.sample())
        # env.render()
        obs, rew, done, info = env.step(1)
        obs, rew, done, info = env.step(3)

        if done:
            if rew != 0:
                score = score + rew
            # else:
                # print('loser')
            break

print(score)