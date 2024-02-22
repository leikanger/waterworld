import environment_interface as env_interface
from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame, sys

import time
import numpy as np

import h5py

run = {}
run['game_fps'] = 16
run['world_side_length'] = 550  # 550# 200
run['number_of_creeps'] = 8
run['game_time_horizon'] = 20000
run['total_parts'] = 1000
run['manual_control'] = True

log = {}
log['number_of_win_for_p'] = []
log['total_reward_for_p'] = []
log['hits_for_part_number_of_red'] = []
log['hits_for_part_number_of_green'] = []
log['parts_of_run_completed'] = 0
log['total_reward'] = 0

PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
PATH_FOR_Q_INPUT = "/tmp/new_q_value.h5"


# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
reward_scheme = {'win': 0.0}

# Create Env:
global_env = env_interface.Env(run['game_fps'], run['world_side_length'],
                               3, run['number_of_creeps'], reward_scheme, True)

def external_control(green_importance_override =None, red_importance_override =None): #{{{
    global tid

    Q_values = np.zeros(global_env.action_space_length())

    pre_pos = global_env.player_pos() #also to be used for læring ..
    pre_vel = global_env.player_velocity()

    #PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
    #PATH_FOR_Q_INPUT = "/tmp/new_q_value.h5"
    with h5py.File(PATH_FOR_SITAWARENESS, 'w') as f:
        f.create_dataset('position', data=pre_pos)
        f.create_dataset('speed', data=pre_vel)
    print(pre_pos)

    #for the_creep in ALL_EOI:
    #    f.create_dataset('eoi'NUMMER-X, data=EoI-POSISJON)  
    #}}}
    return global_env.action_space[4]

def check_divide_log_new_part(tid): #{{{
    if global_env.p.game_over():
        global_env.p.reset_game()
        log['number_of_win_for_p'][-1] += 1

    # Create new log part.
    if tid % (run['game_time_horizon']/run['total_parts']) == 0:
        # create new item in total_rew-vector: init to 0
        log['total_reward_for_p'].append(0)
        log['number_of_win_for_p'].append(0)
        log['hits_for_part_number_of_red'].append(0)
        log['hits_for_part_number_of_green'].append(0)
        log['parts_of_run_completed'] += 1
        print('{', log['parts_of_run_completed'], '}', flush=True)

    #}}} divide_log_new_part
def toggle_manual_control(): #{{{
    run['manual_control'] = not run['manual_control'];
    print("TOGGLE MANUAL CONTROL")
    time.sleep(0.1)

    #}}}
def get_key_pressed(): #{{{
    keys = pygame.key.get_pressed()
    action = 4  # noop? Er dette id eller råverdi? Id 4 er noop
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_SPACE]:
        toggle_manual_control();
    if keys[pygame.K_LEFT]:
        action = pygame.K_a
    if keys[pygame.K_RIGHT]:
        action = pygame.K_d
    if keys[pygame.K_UP]:
        action = pygame.K_w
    if keys[pygame.K_DOWN]:
        action = pygame.K_s
    return action; 

    #}}}

def main():
    global action

    Q_values = np.array([])

    game_time_horizon = run['game_time_horizon']
    total_parts = run['total_parts']
    for tid in range(game_time_horizon):
        check_divide_log_new_part(tid);

        key = get_key_pressed()

        if run['manual_control']:
            action = key;
        else:
            print(global_env.action_space);
            action = external_control();


        reward = global_env.p.act(action)

        log['total_reward'] += reward
        log['total_reward_for_p'][-1] += reward
        if reward > 0:
            log['hits_for_part_number_of_green'][-1] += 1
            print('Got ', reward, '\ttotal: ', log['total_reward'])
        elif reward < 0:
            log['hits_for_part_number_of_red'][-1] += 1
            print('Got ', reward, '\ttotal: ', log['total_reward'])



    print("FINITO:")
    input('press enter to complete...')


if __name__=='__main__':
    main()
