import environment_interface as env_interface
from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame, sys

import time
import numpy as np

import h5py
import zmq
import asyncio


run = {}
run['game_fps'] = 16
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

q_string = "";
continue_listening = True;


#PATH_FOR_SITAWARENESS =     "/tmp/neoRL/updated_situation.h5"
#PATH_FOR_Q_CHANNEL =        "/tmp/neoRL/channel_for_q_value.h5"
#PATH_FOR_EVENT_REPORTING =  "/tmp/neoRL/new_event.h5"
NOOP_id = 4;
# Set opp ZMQ for kommunisering:
    #context = zmq.Context()
    #socket_for_event_reporting = context.socket(zmq.PUB)
    #socket_for_event_reporting.bind("tcp://127.0.0.1:50007")
    #
    # NY: socket_for_sitaw 
    #socket_for_q_value_broadcast = context.socket(zmq.SUB);
    #socket_for_q_value_broadcast.connect("tcp://localhost:50008")

# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
reward_scheme = {'win': 0.0}

# Create Env:
global_env = env_interface.Env(run['game_fps'], run['world_side_length'],
                               3, run['number_of_creeps'], reward_scheme, True)

"""
    def external_control()
        
returnerer en action som definert av Q-vector overført gjennom PATH_FOR_Q_CHANNEL fra ekstern kontroll.
"""
def external_control(green_importance_override =None, red_importance_override =None):
    global tid;
    global q_string;

    the_action_id = 4; #=noop
    print("The Q:" + q_string)
        # TODO Motta signalet gjennom SOCKET
        # s = socket_for_q_transfer.recv_string()
        # each_part = s.split(', ')
        # for it in each_part:
        #     print((it))
        # print(s)
    #{{{ Løysing med filer:
    #    try: 
    #        with h5py.File(PATH_FOR_Q_CHANNEL, 'r') as file:
    #            Q_values = file['q_vector']
    #            print("read Q-vector: ", Q_values[:])
    #            the_action_id = np.argmax(Q_values)
    #            print("id: ", the_action_id)
    #    except:
    #        print("klarte ikkje lese Q-vector fra fil ", PATH_FOR_Q_CHANNEL)
    #       #}}}

    #print("id: ", the_action_id)
    #print("SELECTING action : \t", the_action_id)
    return the_action_id

def check_divide_log_new_part(tid): #{{{
    # Create new log part.
    if tid % (run['game_time_horizon']/run['total_parts']) == 0:
        # create new item in total_rew-vector: init to 0
        log['total_reward_for_p'].append(0)
        log['number_of_win_for_p'].append(0)
        log['hits_for_part_number_of_red'].append(0)
        log['hits_for_part_number_of_green'].append(0)
        log['parts_of_run_completed'] += 1
        print('{', log['parts_of_run_completed'], '}', flush=True)

    if global_env.p.game_over():
        global_env.p.reset_game()
        log['number_of_win_for_p'][-1] += 1
        print("Board reset")


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
    
    all_eoi = []
    pre_pos = global_env.player_pos() #also to be used for læring ..
    pre_vel = global_env.player_velocity()

    positive_eoi = global_env.get_creep_positions('GOOD');

    negative_eoi = global_env.get_creep_positions('BAD');

    return (positive_eoi, negative_eoi)

def effectuate(action):
    # Report all (også NOOP) actions to channel
    socket_for_event_reporting.send_string(str(action));

    return global_env.p.act(global_env.action_space[action]);

def step_env(action):
    check_divide_log_new_part(tid);

    report_situation();

    key = get_key_pressed() 

    if run['manual_control']:
        action = key;
    else:
        action = external_control();

    # Act/ send action to environment:
    reward = effectuate(action);

async def run_env():
    global action
    print("starting run_env()")

    Q_values = np.array([])

    game_time_horizon = run['game_time_horizon']
    total_parts = run['total_parts']
    for tid in range(game_time_horizon):
        step_env(action)
        log['total_reward'] += reward
        log['total_reward_for_p'][-1] += reward
        if reward > 0:
            log['hits_for_part_number_of_green'][-1] += 1
            print('Got ', reward, '\ttotal: ', log['total_reward'])
        elif reward < 0:
            log['hits_for_part_number_of_red'][-1] += 1
            print('Got ', reward, '\ttotal: ', log['total_reward'])
        await asyncio.sleep(0.1);

    print("FINITO:")
    input('press enter to complete...')


async def listener_for_q_message():
    print("FAEN")
    global context, socket_for_q_value_broadcast;
    global q_string;
    global continue_listening;
    print("Starting listener");
    try:
        print("før")
        while continue_listening:
            print("f")
            q_string = await socket_for_q_value_broadcast.recv_string();
            print("etter")
            print(q_string)
            await asyncio.sleep(0.1);

    except asyncio.CancelledError:
        print("etter")



async def main():
    global context; #
    context = zmq.Context()
    global socket_for_event_reporting;
    # global socket_for_sitaw;
    global socket_for_q_value_broadcast;
    # setup:
    context = zmq.Context();
    socket_for_event_reporting = context.socket(zmq.PUB)
    socket_for_event_reporting.bind("tcp://127.0.0.1:50012")
    #socket_for_sitaw = context.socket(zmq.PUB)
    #socket_for_sitaw.bind("tcp://127.0.0.1:50013")
    socket_for_q_value_broadcast = context.socket(zmq.SUB);
    socket_for_q_value_broadcast.connect("tcp://localhost:50014")
    #socket_for_q_value_broadcast.setsockopt_string(zmq.SUBSCRIBE, "");

    try:
        # FORSØK 4:
        #listener_for_q_message()
        #async with asyncio.TaskGroup() as tg:
        #    runner = tg.create_task( run_env() );
        #    listener = tg.create_task( listener_for_q_message() );
        #
        #    print(f"started at {time.strftime('%X')}");
        #print(f"finished at {time.strftime('%X')}")

        # FORSØK 1:
    #        print("Opprettar test")
    #        test_t = asyncio.create_task(test());
    #        print("Opprettar igang runner")
    #        run_task = asyncio.create_task(run_env());
    #        print("Opprettar igang listener")
    #        listener_task = asyncio.create_task(listener_for_q_message());
    
        # FORSØK 2:
        print("Venter på runner og listener.")
        #L = await asyncio.gather(
        #        test(),
        #        listener_for_q_message(),
        #        run_env()
        #);
        #print(L);

        while True:
            await print(socket_for_q_value_broadcast.recv_string());

        #print("Venter på runner.")
        #await run_task;
        #print("Venter på listener.")
        #await listener_task;
    except KeyboardInterrupt:
        print("sigterm eller anna user termination");
        await(listener_task)
    finally:
        socket_for_event_reporting.close();
        #socket_for_sitaw.close()
        socket_for_q_value_broadcast.close();
        context.destroy();

if __name__=='__main__':
    asyncio.run(main());
