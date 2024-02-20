#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

from ple import PLE
from ple.games.waterworld import WaterWorld

import pygame

# TODO Ta vekk herfra. Finnes i misc_funcitons.py (som skal brukes -- rydd
# opp alle plasser env_interface.limit_to_range brukes)
def limit_to_range(arg, min_val, max_val):
    # Hakkish proof of concept:
    for i in [0, 1]:
        if arg[i] >= max_val:
            arg[i] = max_val-0.01
        if arg[i] <= min_val:
            arg[i] = min_val
    return arg

class Env():
    def __init__(self, game_fps, world_square_len, axis_discretization_N, number_of_creeps, reward_dict, display):
        """ Make an instance of WaterWorld env. Standardized interface for
        env, making it easier to port shepherd to other envs"""
        self.game = WaterWorld(width=world_square_len, \
            height=world_square_len, \
            num_creeps=number_of_creeps)

        self.world_side_length = world_square_len
        #Koblar ut å sende inn fps=??. Defaulter til default heller! (?)
        self.p = PLE(self.game, fps=game_fps, force_fps=False, reward_values=reward_dict, display_screen=display)  # HAR VORE force_fps=False for alle forsøka!!
        #self.p = PLE(self.game, force_fps=False, display_screen=display)  # HAR VORE force_fps=False for alle forsøka!!
        self.p.init()
        # When saving it is important that actions are sorted, to have the
        # right shape for the saved Q table (and avoid stupid behaviour)
        action_space = self.p.getActionSet()
        self.action_space = sorted(action_space, key=lambda x: (x is None, x))

        # previous step's number_of_creeps_green
        self.previous_number_of = {"GOOD":0, "BAD":0}
        self.previous_number_of["GOOD"] = self.get_number_of_creep("GOOD")
        self.previous_number_of["BAD"] = self.get_number_of_creep("BAD")

    """
    def draw_Q_vector(self, Q_vector):
        player_pos = self.player_pos()
        origo = player_pos # (player_pos[0], player_pos[1])
        screen = self.p.game.screen #self.p.game.screen
        print(screen)
        end = np.add(origo, [10, 10])
        print(origo, ' ' ,end)
        pygame.draw.line(screen, (255,255,255), origo, end)
        pygame.draw.rect(
            screen, (10, 10, 10), [
                10, 10, 5, 7], 0)
        pygame.draw.line(screen, (0,0,0), origo, end)
        pygame.draw.line(screen, (255,255,255), (5,5), (10,10),1)
        pygame.display.update()
    """
    def action_space_length(self):
        return len(self.action_space)

    def get_creep_positions(self, good_or_bad):
        if not good_or_bad in ['GOOD','BAD']:
            raise TypeError('get_creep_pos: arg supposed to be "GOOD" or "BAD"')
        game_state = self.game.getGameState()
        creep_vector = game_state['creep_pos']
        return np.array(creep_vector[good_or_bad])

    def get_number_of_creep(self, GOOD_or_BAD):
        return len(self.get_creep_positions(GOOD_or_BAD))

    def change_in_number_of(self, GOOD_or_BAD):
        current_number = self.get_number_of_creep(GOOD_or_BAD)
        diff_creep = current_number - self.previous_number_of[GOOD_or_BAD]
        self.previous_number_of[GOOD_or_BAD] = current_number
        return diff_creep


    def player_velocity(self):
        game_state = self.game.getGameState()
        velocity = np.array([game_state['player_velocity_x'], \
                        game_state['player_velocity_y']])
        return velocity

    def player_pos(self):
        game_state = self.game.getGameState()
        player_pos = np.array([game_state['player_x'],
                        game_state['player_y']])
        return player_pos
