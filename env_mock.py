import random
rand = random.random

#import environment_interface as env_interface
#import pygame, sys


import time
import numpy as np

run = {}
run['game_fps'] = 0 # ved FPS satt til 0, itererer WaterWorld kun etter kall til effectuate(action)
FPS = 50
run['world_side_length'] = 550  # 550# 200
run['number_of_creeps'] = 3
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

NOOP_id = 4;

# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
reward_scheme = {'win': 0.0}

def toggle_manual_control():
    run['manual_control'] = not run['manual_control'];

def get_key_pressed(): 
    return random.choice(rand(4))

def rand_2d_coord():
    return [rand(), rand()]

def observe_situation():
    all_eoi = []
    pre_pos = np.array(rand_2d_coord());
    pre_vel = np.array(rand_2d_coord());

    positive_eoi = np.array([rand_2d_coord(), rand_2d_coord()]);                   # lagar 2 EoI positive
    negative_eoi = np.array([rand_2d_coord(), rand_2d_coord(), rand_2d_coord()]);  # lagar 3 EoI negative

    return {"pos": pre_pos, "vel": pre_vel, "EoI+": positive_eoi, "EoI-": negative_eoi}

def effectuate(action):
    # Report all (også NOOP) actions to channel         # TODO Treng kanalen oppe å kjøre igjen! TODO
    broadcast_action(action);
    return 0.0; # REWARD... # global_env.p.act(global_env.action_space[action]);

def step_control(action =NOOP_id):
    if action != NOOP_id:
        # Act/ send action to environment:
        effectuate(action);
    return observe_situation();

####### Broadcast performed action ############
def broadcast_action(action):
    return

# Demo-main som kjøres dersom script er kalla for seg sjølv. {{{
def main_loop():
    try:
        #setup_comm();
        print("Main loop")
        for tid in range(run['game_time_horizon']):
            step_control()
            time.sleep(1/FPS)
            if tid%10==0: print("------------------------ tid: ", tid, "-------------------------")
            print(observe_situation())

        print("FINITO:")
        input('press enter to complete...')
    finally:
        #destruct_comm();
        print("Done");

if __name__=='__main__':
    main_loop();
#}}}
