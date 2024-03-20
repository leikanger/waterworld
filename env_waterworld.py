import environment_interface as env_interface
from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame, sys

import time
import numpy as np

import zmq

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

# Create Env:
global_env = env_interface.Env(run['game_fps'], run['world_side_length'],
                               3, run['number_of_creeps'], reward_scheme, True)

def toggle_manual_control(): #{{{
    run['manual_control'] = not run['manual_control'];
    print("TOGGLE MANUAL CONTROL")
    time.sleep(0.1)

    #}}}
def get_key_pressed(): #{{{
    keys = pygame.key.get_pressed()
    action = 4  # noop? Er dette id eller råverdi? Id 4 er noop
    if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_SPACE]:
        toggle_manual_control();
    if keys[pygame.K_UP]:
        action = pygame.K_w
        return 3;
    if keys[pygame.K_DOWN]:
        action = pygame.K_s
        return 2;
    if keys[pygame.K_LEFT]:
        action = pygame.K_a
        return 0;
    if keys[pygame.K_RIGHT]:
        action = pygame.K_d
        return 1;
    return action; 

    #}}}
def observe_situation():
    global socket_for_event_reporting;

    scaling_factor = 1/500;
    
    all_eoi = []
    pre_pos = global_env.player_pos() * scaling_factor;
    pre_vel = global_env.player_velocity() * scaling_factor;

    # av type: numpy.ndarray :
    ##>> <class 'numpy.ndarray'>
    ##>> [[291.81604577  71.62618017]
    ##>> [ 54.89175415 322.31641435]]
    positive_eoi = global_env.get_creep_positions('GOOD') * scaling_factor;
    negative_eoi = global_env.get_creep_positions('BAD') * scaling_factor;

    return {"pos": pre_pos, "vel": pre_vel, "EoI+": positive_eoi, "EoI-": negative_eoi}

def effectuate(action):
    # Report all (også NOOP) actions to channel         # TODO Treng kanalen oppe å kjøre igjen! TODO
    return global_env.p.act(global_env.action_space[action]);

def step_control(action =NOOP_id):
    if global_env.p.game_over():
        global_env.p.reset_game()
        #log['number_of_win_for_p'][-1] += 1

    key = get_key_pressed() 
    if run['manual_control']:
        action = key;

    # Act/ send action to environment:
    reward = effectuate(action);
    return action; # method for reporting what action was taken to Julia.

####### Broadcast performed action ############
#def broadcast_action(action):
#{{{ Kommentert ut
    #def broadcast_action(action):
    #    return
    #    #socket_for_event_reporting.send_string(str(action));
    #
    #def setup_comm():
    #    global context; #
    #    global socket_for_event_reporting;
    #    # setup:
    #    context = zmq.Context();
    #    socket_for_event_reporting = context.socket(zmq.PUB)
    #    socket_for_event_reporting.bind("tcp://127.0.0.1:50012")
    #    return socket_for_event_reporting;
    #
    #def destruct_comm():
    #    socket_for_event_reporting.close();
    #    context.destroy();
#}}}

# Demo-main som kjøres dersom script er kalla for seg sjølv. {{{
største_verdi = [0,0];
def main_loop():
    try:
        #setup_comm();
        for tid in range(run['game_time_horizon']):
            step_control()
            time.sleep(1/FPS)
            if tid%10==0: print("------------------------ tid: ", tid, "-------------------------")
            print(observe_situation())

            #global største_verdi;
            #x=data["pos"][0]
            #if x > største_verdi[0]:
            #    største_verdi[0] = x
            #y=data["pos"][1]
            #if y > største_verdi[1]:
            #    største_verdi[1] = y
            #print("STØRSTE: ", største_verdi)

        print("FINITO:")
        input('press enter to complete...')
    finally:
        #destruct_comm();
        print("Done");

if __name__=='__main__':
    main_loop();
#}}}
