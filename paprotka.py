import matplotlib.pyplot as plt
import random
import math


class Fern:
    """Rysowanie Paproci Barnsleya"""
    def __init__(self):
        self.fig = plt.figure("Paproć Barnsleya", figsize=(7, 7))
        self.x2, self.y2 = [], []
        self.game_point = [0, 0]
        self.fern_redraw()

    def barnsley_fern(self):
        r = random.uniform(0, 100)
        if r < 1.0: # trzon paprotki
            self.game_point[0] = 0
            self.game_point[1] = 0.16*self.game_point[1]
        elif r < 86.0: # maly lisc
            self.game_point[0] = 0.85*self.game_point[0] + 0.04*self.game_point[1]
            self.game_point[1] = -0.04*self.game_point[0] + 0.85*self.game_point[1] + 1.6
        elif r < 93.0: #duzy lisc
            self.game_point[0] = 0.2*self.game_point[0] - 0.26*self.game_point[1]
            self.game_point[1] = 0.23*self.game_point[0] + 0.22*self.game_point[1] + 1.6
        else:
            self.game_point[0] = -0.15*self.game_point[0] + 0.28*self.game_point[1]
            self.game_point[1] = 0.26*self.game_point[0] + 0.24*self.game_point[1] + 0.44
        self.x2.append(self.game_point[0])
        self.y2.append(self.game_point[1])

    def fern_redraw(self):
        """Czysci wykres i rysuje go od nowa"""
        ax = self.fig.add_subplot(111)
        for i in range(10000):
            self.barnsley_fern()
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        plt.scatter(self.x2, self.y2, s=0.2, edgecolor='green') 
        plt.show()

if __name__ == "__main__":
    Fern()
