from asyncio import current_task
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

class WumpusAgent(Percept):
    def __init__(self) -> None:
        pass
        

    def move_forward(self):
        current_agent_index = (1,1)
        Percept.sense_breeze(current_agent_index=current_agent_index)

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

new_percept = Percept(new_env.sensors_map)
new_percept.sense_stench(current_agent_index=(1,1))
new_percept.sense_breeze(current_agent_index=(1,1))
new_percept.gold_found(current_agent_index=(1,1))

new_agent = WumpusAgent()
new_agent.move_forward()
