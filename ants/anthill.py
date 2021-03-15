"""Anthill class used in ant simulation Spring 2021"""
import time

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

DIRECTIONS = ['up', 'left', 'down', 'right']


class Ant():
    """Class designating the Ant object"""
    loc = [0, 0]
    hasfood = False
    home = [0, 0]

    def __init__(self, r=1, c=1, hr=0, hc=0):
        """Inicialize ant with start location and home location"""
        self.loc = [r, c]
        self.home = [hr, hc]

    def gohome(self):
        """Calculates direction towards the ants home and moves
        randomly in that direction"""
        homedir = np.array(self.home) - np.array(self.loc)
        
        # Write a script here that sets direction to be one of the strings 
        # 'left', 'right', 'up', 'down'
        
        #--------YOUR CODE HERE-----------------#
        
        return direction

    def findfood(self, neighbors):
        """Passed list of neighbors (up, left, down right) that have smell
        and removes directions toward home. If no directions are left, it picks
        a random direction"""
        homedir = np.array(self.home) - np.array(self.loc)
        
        # Add your code here to get rid of directions that go towards home, and returns a 
        # one of those randomly, or a random direction if no available directions
        
        #--------YOUR CODE HERE-----------------#

        return directionToGo

    def plot(self):
        """Puts down a dot for this ant. Red means it has food,
        green means it does not"""
        if self.hasfood:
            color = 'red'
        else:
            color = 'green'
        plt.scatter(self.loc[1], self.loc[0], color=color)

    def move(self, neighbors):
        """Move ant:
                Home: if has food
                Away From Home: If it smells something
                otherwise: random
        """
        if self.hasfood:
            
            direction = self.gohome()
        else:
            direction = self.findfood(neighbors)

        # Write code here to update self.loc to move
        # the ant in one of the four directions.
        
        #--------YOUR CODE HERE-----------------#
            
        # Drop the food if we made it home
        if self.loc == self.home:
            self.hasfood = False


class Anthill():
    """Class designating the anthill which contains ants."""
    Ants = []
    smells = np.array(1)
    food = np.array(1)

    def __init__(self, food='', numants=100):
        """Initialize anthill with either a food aray and number of ants."""

        if food == '':
            self.food = np.zeros((20, 100))
            self.food[5:15, 5:15] = 10
        else:
            self.food = food

        worldshape = self.food.shape
        for _ in range(numants):
            row = int(np.random.rand() * worldshape[0])
            col = int(np.random.rand() * worldshape[1])
            self.Ants.append(Ant(row, col, 10, 80))
        self.smells = np.zeros(worldshape)

    def show(self):
        "Show the location of the food and the Ants"
        plt.imshow(self.food)
        for ant in self.Ants:
            ant.plot()

    def getneighbors(self, loc):
        "Return directions of smells around specific location."
        worldshape = self.food.shape
        neighbors = []
        row = loc[0]
        col = loc[1]
        if row > 0:
            if self.smells[row-1, col] > 0:
                neighbors.append('down')
        if col > 0:
            if self.smells[row, col-1] > 0:
                neighbors.append('left')
        if row < worldshape[0]-1:
            if self.smells[row+1, col] > 0:
                neighbors.append('up')
        if col < worldshape[1]-1:
            if self.smells[row, col+1] > 0:
                neighbors.append('right')
                

        return neighbors

    def simulate(self, iterations=1):
        """Run the simulation an input number of iterations (default 1)"""
        worldshape = self.food.shape
        fig, _ = plt.subplots(figsize=(10, 20))
        for _ in range(iterations):

            for ant in self.Ants:
                ant.move(self.getneighbors(ant.loc))
                if ant.loc[0] < 0:
                    ant.loc[0] = 0
                if ant.loc[0] == worldshape[0]:
                    ant.loc[0] = worldshape[0]-1
                if ant.loc[1] < 0:
                    ant.loc[1] = 0
                if ant.loc[1] == worldshape[1]:
                    ant.loc[1] = worldshape[1]-1

                if ant.hasfood:
                    self.smells[ant.loc[0], ant.loc[1]] += 10

                if self.food[ant.loc[0], ant.loc[1]] > 0:
                    if not ant.hasfood:
                        self.food[ant.loc[0], ant.loc[1]] -= 1
                        ant.hasfood = True

            self.show()

            # Animation part (doesn't change)
            clear_output(wait=True) # Clear output for dynamic display
            display(fig)            # Reset display
            fig.clear()             # Prevent overlapping and layered plots
            time.sleep(0.0001)      # Sleep to allow animation to catch up
