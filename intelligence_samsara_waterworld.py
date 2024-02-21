#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

from ple import PLE
from ple.games.waterworld import WaterWorld

from perleik.experiment_setup import EXPERIMENT
            # PARAMETERS -- experiment parameters
            config['EXPERIMENT'] = {}
            fps = 50
            config['EXPERIMENT']['time_horizon'] = str(TIME_HORIZON)
            config['EXPERIMENT']['fps'] = str(fps)  # '50'
            config['EXPERIMENT']['bin_size_4_digsig'] = str(int(fps/5))  # '10'
            config['EXPERIMENT']['show_display'] = str(SHOW_DISPLAY)
            config['EXPERIMENT']['world_side_length'] = '250'
            config['EXPERIMENT']['number_of_creeps'] = str(NUMBER_OF_CREEPS)
            config['EXPERIMENT']['print_progress'] = 'False'
            config['EXPERIMENT']['forsøk_nummer_eoi'] = str(FORSØK_NUMMER_EoI)
            config['EXPERIMENT']['recursive_factor_eoi'] = str(RECURSIVE_FACTOR_EoI)
            config['EXPERIMENT']['factor_for_loke_value_function'] = str(FACTOR_FOR_Loke_VALUE_FUNCTION)



# +# Her definerer eg at 'win' ikkje fører til ekstra reward!
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

# Logger litt:
skjerm.print_init_message(EXPERIMENT['time_horizon'],
                        EXPERIMENT['world_side_length'], \
                        1, EXPERIMENT['number_of_creeps'])

file_name = 'forsøk/'

number_of_win_for_p = []
total_reward_for_p = []

N_hits_for_p = {}
N_hits_for_p['red'] = []
N_hits_for_p['green'] = []
parts_of_run_completed = 0

Q_values = []
Q_values = np.zeros(global_env.action_space_length())



def step_HAL(green_importance_override =None, red_importance_override =None):
    global Q_values, tid

    pre_pos = global_env.player_pos() #also to be used for læring ..
    pre_vel = global_env.player_velocity()

    # TODO i HAL: reset_all_pri_for(LOKE)

    # arrow_valence = 0

    # tilnærming: for kvar EoI, endre prioritet for pos til EoI til valence til EoI (dvs. plusse på denne). 


        # VIRKER SOM OM [OVC] er generellt 3X så hoeg som [PC}: hack-test: dobler PC value function:
        Q_values = np.nansum([FACTOR_FOR_Loke_VALUE_FUNCTION*Q_values_LOKE, Q_values_s], 0)
        if tid%100 == 0:
            print('\n\n_**SpeedPos*__ ', tid)


        Q_values = no.zeros(5)

        # TODO (prøv å) LESE-UT-FRA-FIL -> legge til dette i Q_values

        # OBS: Dersom alt er null, velg NOOP.  Ellers: argmax.
        if sum(Q_values) == 0 
            action_id = Q_values[5] # noop
        else:
            action_id = np.argmax(Q_values[0:4])


    # EFFECTUATE!
    # TODO  1   les ut Q-vector fra fil. HDF5. Dersom ingen fil eller oppdatering, lagre verdi [0,0,0,0,0.001] -->
                    # med at 5-eren betyr noop
    # TODO  2   velg action for denne action_id
    # TODO 3    Velg rett action til å sende til env:
        action = global_env.action_space[action_id]
    # TODO 4    Effektuer --> kun sende denne til env utan å bry seg om returverdi / reward:
        env_step_with_a(action)
    # TODO 5    Tilbakemelding for læring: skrive til fil ved HDF5 serialisering: egen posisjon og hastighet held.
            # TODO update_state_to_agent(file, state-data) ELLER NOKE

    # (loggfør reward og hits og seirar osv.)


def env_step_with_a(action):
    global tid
    reward = global_env.p.act(action)

    # INCREASE TIME
    tid += 1

def main():
    global tid
    for t in range(EXPERIMENT['time_horizon']):
        # step_PL_agent()
        step_external_Q_input()

if __name__=="__main__":
    main()
    #main_double_num_creeps_halfway()
