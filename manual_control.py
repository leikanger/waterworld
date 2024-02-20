import environment_interface as env_interface
from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame

import time
import numpy as np

game_fps = 16
world_side_length = 550  # 550# 200
number_of_creeps = 8

# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
reward_scheme = {'win': 0.0}

# Create Env:
global_env = env_interface.Env(game_fps, world_side_length,
                               3, number_of_creeps, reward_scheme, True)

game_time_horizon = 20000
total_parts = 1000
action = 4  # noop? Er dette id eller råverdi? Id 4 er noop
total_reward = 0

def main():
    global action, total_reward
    number_of_win_for_p = []
    total_reward_for_p = []
    N_hits_for_p = {}
    N_hits_for_p['red'] = []
    N_hits_for_p['green'] = []
    parts_of_run_completed = 0

    Q_values = np.array([])

    for tid in range(game_time_horizon):

        if tid % (game_time_horizon/total_parts) == 0:
            # create new item in total_rew-vector: init to 0
            total_reward_for_p.append(0)
            number_of_win_for_p.append(0)
            N_hits_for_p['red'].append(0)
            N_hits_for_p['green'].append(0)
            parts_of_run_completed += 1
            print('{', parts_of_run_completed, '}', flush=True)

        if global_env.p.game_over():
            global_env.p.reset_game()
            number_of_win_for_p[-1] += 1


        keys = pygame.key.get_pressed()
        action = 4
        if keys[pygame.K_LEFT]:
            action = pygame.K_a
        if keys[pygame.K_RIGHT]:
            action = pygame.K_d
        if keys[pygame.K_UP]:
            action = pygame.K_w
        if keys[pygame.K_DOWN]:
            action = pygame.K_s

        #action = global_env.action_space[action_id]

        reward = global_env.p.act(action)

        total_reward += reward
        total_reward_for_p[-1] += reward
        if reward > 0:
            N_hits_for_p['green'][-1] += 1
            print('Got ', reward, '\ttotal: ', total_reward)
        elif reward < 0:
            N_hits_for_p['red'][-1] += 1
            print('Got ', reward, '\ttotal: ', total_reward)



    file_name = 'manual_control'
    import analysis as a
    a.plotSmooth(total_reward_for_p, 'R for part')
    a.plotSmooth(N_hits_for_p['red'],   'red   hits at part')
    a.plotSmooth(N_hits_for_p['green'], 'green hits at part')
    a.title(file_name)
    a.show()
    input('press enter to complete...')


if __name__=='__main__':
    main()
