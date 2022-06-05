import random 

class WumpusEnv:
    def __init__(self):
        self.env_size = 4
        self.agent = 'A'
        self.pit = 'P'
        self.wumpus = 'W'
        self.gold = 'G'
        self.breeze = 'B'
        self.stench = 'S'
        self.pit_probability = 0.2
        self.map = self.create_map
        self.indexes = self.get_indexes
        self.agentless_index = self.agentless_index()

    @property
    def create_map(self):
        map =list()
        for x in range(1, self.env_size+1):
            col = []
            for y in range(1, self.env_size+1):
                col.append('O')
            map.append(col)
        return map

    @property
    def get_indexes(self):
        indexes = list()
        for x in range(1, self.env_size+1):
            for y in range(1, self.env_size+1):
                indexes.append((x,y))
        return indexes 

    def agentless_index(self):
        #remove agent index which is (1,1)
        agentless_index =  self.indexes
        agentless_index.pop(0)
        return agentless_index

    def set_object(self, object, index):
        x,y = index
        #print(x,y,object)
        if self.map[self.env_size-x][y-1] == 'O': # when there isn't anything
            self.map[self.env_size-x][y-1] = object
        else: # if there is another object on that index append it
            previous_object = self.map[self.env_size-x][y-1]
            self.map[self.env_size-x][y-1] = object + previous_object


    def set_agent(self):
        index = (1,1)
        self.set_object(self.agent, index)
    
    def set_pit(self):
        for index in self.agentless_index:
            if random.random() <= self.pit_probability:
                self.set_object(self.pit, index)

    def set_wumpus(self):
        random_index = random.choice(self.agentless_index)
        self.set_object(self.wumpus, random_index)
    
    
    def set_gold(self):
        random_index = random.choice(self.agentless_index)
        self.set_object(self.gold, random_index)


    def print_map(self):
        for row in self.map:
            print(*row, sep=" | ")

new_env = WumpusEnv()
new_env.set_agent()
new_env.set_wumpus()
new_env.set_gold()
new_env.set_pit()
new_env.print_map()