from environment import WumpusEnv

class Percept(WumpusEnv):
    def __init__(self, sensors_map):
        self.right = "right"
        self.left = "left"
        self.up = "up"
        self.down = "down"
        self.sensors_map = sensors_map
    
    def sense_stench(self, current_agent_index):
        x,y = current_agent_index
        sensor_map = self.sensors_map
        if WumpusEnv.pit in sensor_map[WumpusEnv.env_size-x][y-1]:
            print("yes")
    
    def sense_breeze(self, current_agent_index):
        x,y = current_agent_index
        sensor_map = self.sensors_map
        if WumpusEnv.breeze in sensor_map[x][y]:
            print("yes")



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

new_percept = Percept(new_env.sensors_map)
new_percept.sense_stench(current_agent_index=(1,1))
new_percept.sense_breeze(current_agent_index=(1,1))
