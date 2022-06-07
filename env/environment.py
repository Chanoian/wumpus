import random 

class WumpusEnv:
    env_size = 4
    agent = 'A'
    pit = 'P'
    wumpus = 'W'
    gold = 'G'
    breeze = 'B'
    stench = 'S'
    pit_probability = 0.2

    def __init__(self):   
        self.map = self.create_map
        self.sensors_map = self.create_map
        self.indexes = self._get_indexes
        WumpusEnv.agentless_index = self._agentless_index

    @property
    def create_map(self):
        map =list()
        for x in range(1, WumpusEnv.env_size+1):
            col = []
            for y in range(1, WumpusEnv.env_size+1):
                col.append('O')
            map.append(col)
        return map

    @property
    def _get_indexes(self):
        indexes = list()
        for x in range(1, WumpusEnv.env_size+1):
            for y in range(1, WumpusEnv.env_size+1):
                indexes.append((x,y))
        return indexes 

    @property
    def _agentless_index(self):
        #remove agent index which is (1,1)
        agentless_index =  self.indexes
        agentless_index.pop(0)
        return agentless_index

    def _set_object(self, object, index, map):
        x,y = index
        if map[WumpusEnv.env_size-x][y-1] == 'O': # when there isn't anything
            map[WumpusEnv.env_size-x][y-1] = object
        elif object in map[WumpusEnv.env_size-x][y-1] : #when there is already similar object in that field
                return
        else: # if there is another object on that index append it
            previous_object = map[WumpusEnv.env_size-x][y-1]
            map[WumpusEnv.env_size-x][y-1] = object + previous_object


    def _read_object_index(self, object):
        indexes=list()
        for x,i in enumerate(self.map):
            for y,j in enumerate(i):
                if object in j:
                    indexes.append((WumpusEnv.env_size-x,y+1))
        return indexes


    def set_agent(self):
        index = (1,1)
        self._set_object(WumpusEnv.agent, index, self.map)
    
    def set_pit(self):
        for index in WumpusEnv.agentless_index:
            if random.random() <= WumpusEnv.pit_probability:
                self._set_object(WumpusEnv.pit, index, self.map)

    def set_wumpus(self):
        random_index = random.choice(WumpusEnv.agentless_index)
        self._set_object(WumpusEnv.wumpus, random_index, self.map)
    
    
    def set_gold(self):
        random_index = random.choice(WumpusEnv.agentless_index)
        self._set_object(WumpusEnv.gold, random_index, self.map)


    def print_map(self):
        for row in self.map:
            print(*row, sep=" | ")
    
    def print_sensors_map(self):
        for row in self.sensors_map:
            print(*row, sep=" | ")

    def build_up_the_perception_map(self):
        sensors_map = self.map
        self.set_stench(sensors_map)
    
    def set_stench(self):
        wumpus_index = self._read_object_index(WumpusEnv.wumpus)
        stenchy_indexes = self.find_adjacent_indexes(wumpus_index[0])
        for index in stenchy_indexes:
            self._set_object(WumpusEnv.stench, index, self.sensors_map)


    def set_breeze(self):
        # Multiple indexes for the pit
        pit_indexes = self._read_object_index(WumpusEnv.pit)
        for pit_index in pit_indexes:
            breezy_indexes = self.find_adjacent_indexes(pit_index)
            for index in breezy_indexes:
                self._set_object(WumpusEnv.breeze, index, self.sensors_map)
    
    def set_glitter(self):
        gold_index = self._read_object_index(WumpusEnv.gold)
        glitter_index = gold_index[0]
        self._set_object(WumpusEnv.gold, glitter_index, self.sensors_map)

    def find_adjacent_indexes(self, index):
        x,y = index
        adjacent_indexes, adj_x,  adj_y = list(), list(), list()
        if x == 1:
            adj_x.append(x+1)
        elif x == WumpusEnv.env_size:
            adj_x.append(x-1)
        else:
            adj_x.append(x-1)
            adj_x.append(x+1)
        if y == 1:
            adj_y.append(y+1)
        elif y == WumpusEnv.env_size:
            adj_y.append(y-1)
        else :
            adj_y.append(y-1)
            adj_y.append(y+1)
        if len(adj_x) == 1:
            adjacent_indexes.append((adj_x[0], y))
        else:
            adjacent_indexes.append((adj_x[0], y))
            adjacent_indexes.append((adj_x[1], y))
        if len(adj_y) == 1:
            adjacent_indexes.append((x, adj_y[0]))
        else:
            adjacent_indexes.append((x, adj_y[0]))
            adjacent_indexes.append((x, adj_y[1]))
        return adjacent_indexes


# new_env = WumpusEnv()
# new_env.set_agent()
# new_env.set_wumpus()
# new_env.set_gold()
# new_env.set_pit()
# new_env.print_map()

# new_env.set_stench()
# new_env.set_breeze()
# new_env.set_glitter()
# new_env.print_sensors_map()
