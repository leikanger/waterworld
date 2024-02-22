#!/usr/bin/python
# -*- coding: utf-8 -*-
import environment_interface as env_interface

from ple import PLE
from ple.games.waterworld import WaterWorld

import numpy as np

import h5py

PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
PATH_FOR_Q_INPUT = "/tmp/new_q_value.h5"

TIME_HORIZON = 10000
NUMBER_OF_CREEPS = 4
PRINT_PROGRESS = False
# from perleik.experiment_setup import EXPERIMENT
# PARAMETERS -- experiment parameters
EXPERIMENT = {}  # Lagar ein dict, Python style.
EXPERIMENT['number_of_creeps'] = 4
EXPERIMENT['time_horizon'] = 10000
EXPERIMENT['fps'] = 50
EXPERIMENT['bin_size_4_digsig'] = int(EXPERIMENT['fps']/5)  # '10'
EXPERIMENT['show_display'] = True
EXPERIMENT['world_side_length'] = 250
EXPERIMENT['print_progress'] = False

# +# Her omdefinerer eg reward scheme: 'win' gir ingen ekstra reward!
reward_scheme = {'win': 0.0}

## Create Env:
global_env = env_interface.Env(EXPERIMENT['fps'],\
                int(EXPERIMENT['world_side_length']), \
                3, EXPERIMENT['number_of_creeps'],\
                reward_scheme,
                EXPERIMENT['show_display'])
print('actions: ', global_env.action_space)

# DETTE SKAL MED VIDARE :::::

# Global time variabel: tid
tid = 0

number_of_win_for_p = []
total_reward_for_p = []

N_hits_for_p = {}
N_hits_for_p['red'] = []
N_hits_for_p['green'] = []
parts_of_run_completed = 0

Q_values = []
Q_values = np.zeros(global_env.action_space_length())

def step_external_control(green_importance_override =None, red_importance_override =None):
    global Q_values, tid

    pre_pos = global_env.player_pos() #also to be used for læring ..
    pre_vel = global_env.player_velocity()

    #PATH_FOR_SITAWARENESS = "/tmp/updated_situation.h5"
    #PATH_FOR_Q_INPUT = "/tmp/new_q_value.h5"
    with h5py.File(PATH_FOR_SITAWARENESS, 'w') as f:
        f.create_dataset('position', data=pre_pos)
        f.create_dataset('speed', data=pre_vel)

    #for the_creep in ALL_EOI:
    #    f.create_dataset('eoi'NUMMER-X, data=EoI-POSISJON)  


# {{{   
#   # TODO i HAL: reset_all_pri_for(LOKE)

#   # arrow_valence = 0

#   # tilnærming: for kvar EoI, endre prioritet for pos til EoI til valence til EoI (dvs. plusse på denne). 

#       Q_values = np.zeros(5)

#       # TODO (prøv å) LESE-UT-FRA-FIL -> legge til dette i Q_values

#       # OBS: Dersom alt er null, velg NOOP.  Ellers: argmax.
#       if sum(Q_values) == 0 
#           action_id = Q_values[5] # noop
#       else:
#           action_id = np.argmax(Q_values[0:4])


#   # EFFECTUATE!
#   # TODO  1   les ut Q-vector fra fil. HDF5. Dersom ingen fil eller oppdatering, lagre verdi [0,0,0,0,0.001] -->
#                   # med at 5-eren betyr noop
#   # TODO  2   velg action for denne action_id
#   # TODO 3    Velg rett action til å sende til env:
#       action = global_env.action_space[action_id]
#   # TODO 4    Effektuer --> kun sende denne til env utan å bry seg om returverdi / reward:
#       env_step_with_a(action)
#   # TODO 5    Tilbakemelding for læring: skrive til fil ved HDF5 serialisering: egen posisjon og hastighet held.
#           # TODO update_state_to_agent(file, state-data) ELLER NOKE

#   # (loggfør reward og hits og seirar osv.)
#}}}

def print_init_message( game_time_horizon, \
                        world_side_length, \
                        number_of_creeps):
    print('')
    print('#Starting game with:')
    print('#    -> game_time_horizon: ', game_time_horizon, \
        ' iterations')
    print('#    -> board size (each axis): ', world_side_length)
    print('#    -> and ', number_of_creeps, ' mumber of creeps):')


def env_step_with_a(action):
    global tid
    reward = global_env.p.act(action)

    # INCREASE TIME
    tid += 1


def main():
    # Logger litt:
    print_init_message(EXPERIMENT['time_horizon'],
                    EXPERIMENT['world_side_length'], \
                    EXPERIMENT['number_of_creeps'])

    global tid
    for t in range(EXPERIMENT['time_horizon']):
        # step_PL_agent()
        step_external_control()

    #HUGS : funksjonen log_overview_message(number_of_win_for_p, total_reward_for_p, game_time_horizon, world_side_length, number_of_creeps, N_hits_for_p):


if __name__=="__main__":
    main()
    #main_double_num_creeps_halfway()
