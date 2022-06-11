from pathlib import Path
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
path = Path(SCRIPT_DIR)
parent_dir = path.parent.absolute()
env_path = os.path.join(parent_dir, 'env')
sys.path.append(env_path)

from env.environment import WumpusEnv
from env.percept import Percept

class WumpusAgent():
    def __init__(self):
        self.current_agent_index = (1,1)
    
    def move_forward(self, percept_instance):
        Percept.sense_breeze(percept_instance, self.current_agent_index)

    def move_turn_left(self):
        pass

    def move_turn_right(self):
        pass

    def grab_gold(self):
        pass

    def shoot(self):
        pass

    def climb(self):
        pass

    def sense_stinch(self):
        pass


new_env = WumpusEnv()
new_env.set_agent()
new_env.set_wumpus()
new_env.set_gold()
new_env.set_pit()
new_env.print_map()
print("======")

new_env.set_stench()
new_env.set_breeze()
new_env.set_glitter()
new_env.print_sensors_map()
print("======")

new_percept = Percept(new_env.sensors_map, new_env.game_map)

new_agent = WumpusAgent()
new_agent.move_forward(new_percept)
