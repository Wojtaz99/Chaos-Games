import matplotlib.pyplot as plt
import random
import math


class Julia_set:
    """Rysowanie Zbioru Julii"""
    def __init__(self, c=[0.044, -0.66]):
        self.fig = plt.figure("Zbior Julii", figsize=(7, 7))
        self.x2, self.y2 = [[],[],[],[]], [[],[],[],[]]
        self.c = c
        self.set_draw()

    def test_pt(self, a, b):
        zr = a
        zi = b
        color = -2
        for i in range(180):
            if i%20 == 0:
                color += 1
            tmp = zr
            zr = zr**2 - zi**2 + self.c[0]
            zi = 2*tmp*zi + self.c[1]
            if zr**2+zi**2 > 4:
                break

        if color >= 0:
            self.x2[color%4].append(a)
            self.y2[color%4].append(b)

    def set_draw(self):
        """Czysci wykres i rysuje go od nowa"""
        ax = self.fig.add_subplot(111)
        dgt = 1000
        point_size = 0.3

        for i in range(dgt):
            for j in range(dgt):
                self.test_pt(4*(i-dgt/2) / dgt, 4*(j-dgt/2) / dgt)

        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        ax.scatter(self.x2[0], self.y2[0], s=point_size, edgecolor='yellow')
        ax.scatter(self.x2[1], self.y2[1], s=point_size, edgecolor='orange') 
        ax.scatter(self.x2[2], self.y2[2], s=point_size, edgecolor='red') 
        ax.scatter(self.x2[3], self.y2[3], s=point_size, edgecolor='blue')
        plt.show()

if __name__ == "__main__":
    Julia_set()
