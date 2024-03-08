import environment_interface as env_interface
from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame, sys

import time
import numpy as np

import h5py
import zmq

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

PATH_FOR_SITAWARENESS =     "/tmp/neoRL/updated_situation.h5"
PATH_FOR_Q_CHANNEL =        "/tmp/neoRL/channel_for_q_value.h5"
PATH_FOR_EVENT_REPORTING =  "/tmp/neoRL/new_event.h5"
NOOP_id = 4;
# Set opp ZMQ for kommunisering:
context = zmq.Context()
#socket_for_event_reporting = context.socket(zmq.PUSH)
#socket_for_event_reporting.bind("tcp://*:5555")
socket_for_q_transfer = context.socket(zmq.PULL)
socket_for_q_transfer.connect("tcp://localhost:5555")

# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
reward_scheme = {'win': 0.0}

# Create Env:
global_env = env_interface.Env(run['game_fps'], run['world_side_length'],
                               3, run['number_of_creeps'], reward_scheme, True)

"""
    def external_control()
        
returnerer en action som definert av Q-vector overført gjennom PATH_FOR_Q_CHANNEL fra ekstern kontroll.
"""
def external_control(green_importance_override =None, red_importance_override =None): #{{{
    global tid

    the_action_id = 4; #=noop
        # TODO Motta signalet gjennom SOCKET
        # s = socket_for_q_transfer.recv_string()
        # each_part = s.split(', ')
        # for it in each_part:
        #     print((it))
        # print(s)
    #{{{ Løysing med filer:
    try: 
        with h5py.File(PATH_FOR_Q_CHANNEL, 'r') as file:
            Q_values = file['q_vector']
            print("read Q-vector: ", Q_values[:])
            the_action_id = np.argmax(Q_values)
            print("id: ", the_action_id)
    except:
        print("klarte ikkje lese Q-vector fra fil ", PATH_FOR_Q_CHANNEL)
       #}}}

    print("id: ", the_action_id)

    print("SELECTING action : \t", the_action_id)
    return the_action_id
    #}}}

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
    if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_SPACE]:
        toggle_manual_control();
        return;
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
def report_situation():
    #PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
    #PATH_FOR_Q_CHANNEL = "/tmp/channel_for_q_value.h5"
    
    all_eoi = []
    pre_pos = global_env.player_pos() #also to be used for læring ..
    pre_vel = global_env.player_velocity()

    positive_eoi = global_env.get_creep_positions('GOOD');

    negative_eoi = global_env.get_creep_positions('BAD');

    #for the_creep in ALL_EOI:
    #    f.create_dataset('eoi'NUMMER-X, data=EoI-POSISJON)  

    with h5py.File(PATH_FOR_SITAWARENESS, 'w') as f:
        f.create_dataset('position', data=pre_pos)
        f.create_dataset('speed', data=pre_vel)
        f.create_dataset('positive_eoi', data=positive_eoi)
        f.create_dataset('negative_eoi', data=negative_eoi)
        # f.create_dataset('all_eoi', data=all_eoi)
        f.flush()

def effectuate(action):
    #PATH_FOR_EVENT_REPORTING = "/tmp/neoRL/new_event.h5"
    global NOOP_id

    # TODO Sjekk 
        # => 'a' slik [with h5py.File(PATH_FOR_EVENT_REPORTING, 'a') as f:]

    # Report all (other than NOOP) actions to channel PATH_FOR_EVENT_REPORTING
    if action != NOOP_id: # avkommenterer den: tester med noop også.
        #print("sender event: ", str(action))
        ## socket_for_event_reporting.send_string("eventID:"+str(action));
        #print("ferdig sendt")
        # HDF5: --------------------------------------------------------------
        with h5py.File(PATH_FOR_EVENT_REPORTING, 'w') as f:
            f.create_dataset('new_event', data=action)
            previous_event_was_noop = (action == NOOP_id);
            f.flush();

    return global_env.p.act(global_env.action_space[action]);

def main():
    global action

    Q_values = np.array([])

    game_time_horizon = run['game_time_horizon']
    total_parts = run['total_parts']
    for tid in range(game_time_horizon):
        check_divide_log_new_part(tid);
    
        report_situation();

        key = get_key_pressed()

        if run['manual_control']:
            action = key;
        else:
            action = external_control();

        # Act/ send action to environment:
        reward = effectuate(action);

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
