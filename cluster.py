import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# seed random number generator
np.random.seed(int(time.time()))

# colmap returns a color string to be consumed by
# matplotlib, where n distinct, and equally separate
# colors are chosen from the the domain of possible colors
def colmap(i, n, mincolor, maxcolor):
    interval = (maxcolor-mincolor)/n
    return "#" + hex(int(mincolor+i*interval)).upper().strip("0X")

class ClusterBuilder:
    def __init__(self, k, x_range, y_range):
        if len(x_range) != 2:
            raise ValueError("invalid x axis range")
        if len(y_range) != 2:
            raise ValueError("invalid y axis range")
        self.x_vals = []
        self.y_vals = []
        self.x_range = x_range
        self.y_range = y_range
        self.stable = True
        self.centroids = {
            i+1: [np.random.randint(x_range[0], x_range[1]), np.random.randint(y_range[0], y_range[1])]
            for i in range(k)
        }

    def feed(self, x_vals, y_vals):
        if len(x_vals) != len(y_vals):
            raise ValueError("disctinct amount of (x, y) values")
        self.stable = False
        self.x_vals.extend(x_vals)
        self.y_vals.extend(y_vals)

    def stable():
        return self.stable

    def step():
        print("not implemented")
        # TODO: implement k-means algorithm step 

    def build(self):
        while not stable(self):
            self.step()
    
    def plot(self):
        df = pd.DataFrame({'x': self.x_vals, 'y': self.y_vals})
        fig = plt.figure(figsize=(5, 5))

        plt.scatter(df['x'], df['y'], color='k')
        for k in self.centroids:
            plt.scatter(*self.centroids[k], color=colmap(k, len(self.centroids), 0x000000, 0xffffff))

        plt.xlim(self.x_range[0], self.x_range[1])
        plt.ylim(self.y_range[0], self.y_range[1])
        plt.show()

x = ClusterBuilder(3, (0, 80), (0, 80))
x.feed([12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72], [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24])
x.plot()
