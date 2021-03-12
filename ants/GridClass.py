import numpy as np
import random

n,m = 25,30

class Grid():
    def __init__(self):
        self.pheremones = np.zeros((n,m),dtype=int)
        self.food = np.zeros((n,m),dtype=int)
        self.home = (random.randint(1,n),random.randint(1,m))
        
#     def degradeP():
        
        
#     def PopFood():
        
        
