import matplotlib.pyplot as plt
import random
import math


class Anti_clock:
    """Rysowanie takiego krzywego kwadratu"""
    def __init__(self):
        self.fig = plt.figure("Anti-clock", figsize=(7, 7))
        self.x, self.y = [], []
        self.x2, self.y2 = [], []
        self.game_point = [0, 0]
        self.pp = [1, 1, 1, 1]
        self.last_vert = None
        self.anti_clock_redraw()

    def pp_mapping(self):
        pp_sum = sum(self.pp)
        pp_scale = 1.0 / pp_sum
        self.pp[0] = self.pp[0] * pp_scale
        for i in range (1, len(self.pp)):
            self.pp[i] = self.pp[i] * pp_scale + self.pp[i-1]

    def anti_clock(self):
        if self.last_vert != None:
            random_vertex = (self.last_vert + 1) % (len(self.pp))
            while random_vertex == (self.last_vert + 1) % (len(self.pp)):
                random_pp = random.random()
                for i in range(len(self.pp)):
                    if self.pp[i] >= random_pp:
                        random_vertex = i
                        break
        else:
            random_pp = random.random()
            for i in range(len(self.pp)):
                if self.pp[i] >= random_pp:
                    random_vertex = i
                    break
        abs1 = abs(self.x[random_vertex] - self.game_point[0]) / 2
        abs2 = abs(self.y[random_vertex] - self.game_point[1]) / 2
        if self.x[random_vertex] < self.game_point[0]:
           self.game_point[0] = self.x[random_vertex] + abs1
        else:
            self.game_point[0] = self.x[random_vertex] - abs1
        if self.y[random_vertex] < self.game_point[1]:
            self.game_point[1] = self.y[random_vertex] + abs2
        else:
            self.game_point[1] = self.y[random_vertex] - abs2
        self.x2[random_vertex].append(self.game_point[0])
        self.y2[random_vertex].append(self.game_point[1])
        self.last_vert = random_vertex  

    def anti_clock_redraw(self):
        """Czysci wykres i rysuje go od nowa"""
        ax = self.fig.add_subplot(111)
        # Konstruowanie pieciokata z wierzcholkiem w srodku
        n = 4
        r = 40
        for i in range(n):
            self.x.append(50 + r*math.cos(2*math.pi * i/n))
            self.y.append(50 + r*math.sin(2*math.pi * i/n))
        plt.subplots_adjust(left=0, bottom=0, right=1,
                            top=1)
        self.x2, self.y2 = [[] for i in range(len(self.x))], \
                            [[] for i in range(len(self.x))]
        self.game_point = [random.randint(1, 100), \
                            random.randint(1, 100)]
        self.pp_mapping()
        for i in range(10000):
                self.anti_clock()
        for i in range(len(self.x)):
            plt.scatter(self.x2[i], self.y2[i], s=0.8, edgecolor='red') 
        line = ax.plot(self.x, self.y, 'ro')
        plt.xlim(1, 100) # Sprawia, ze wykres sie nie skaluje
        plt.ylim(1, 100)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.show()


if __name__ == "__main__":
    Anti_clock()
