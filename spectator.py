#!/usr/bin/env python
from __future__ import print_function

import argparse
from time import sleep
from vizdoom import *
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('wad')
flags = parser.parse_args()

if __name__ == '__main__':
    game = DoomGame()
    game.load_config("./content/default.cfg")
    game.set_doom_scenario_path(flags.wad)
    game.set_doom_map("map00")
    game.add_game_args("+freelook 1")
    game.set_screen_resolution(ScreenResolution.RES_640X480)
    game.set_screen_format(ScreenFormat.BGR24)
    game.set_automap_buffer_enabled(True)
    game.set_automap_mode(AutomapMode.OBJECTS_WITH_SIZE)  # NORMAL, WHOLE, OBJECTS, OBJECTS_WITH_SIZE
    game.set_window_visible(True)
    game.set_mode(Mode.SPECTATOR)
    game.init()

    episodes = 10

    for i in range(episodes):
        print("Episode #" + str(i + 1))

        game.new_episode()
        while not game.is_episode_finished():
            state = game.get_state()

            # Shows automap buffer
            map = state.automap_buffer
            if map is not None:
                cv2.imshow('ViZDoom Automap Buffer', map)
            cv2.waitKey(28)

            game.advance_action()
            last_action = game.get_last_action()
            reward = game.get_last_reward()
            print("current reward: ", reward)
        print("Episode finished!")
        print("Total reward:", game.get_total_reward())
        print("************************")
        sleep(2.0)

    game.close()
