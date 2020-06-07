from matplotlib.widgets import Slider, TextBox
import matplotlib.pyplot as plt
import random
import math


class Foremne:
    """Klasa okna chaos games dla figur foremnych"""
    def __init__(self):
        self.fig, self.axes = plt.subplots(1, 1, figsize=(8, 8),
                                           num="Figury foremne")
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_dragg)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.x, self.y = [], []
        self.text_boxes, self.sliders = [], [[]]
        self.plots, self.plots2 = [], []
        self.pp_values, self.pp = [], []
        self.colors = ["blue", "green", "red", "cyan", "magenta",
                       "yellow", "black", "orange", "gray", "purple"]
        self.current_point = None
        self.generations = 3000
        self.init_value = 3
        self.number_of_points = 0
        self.do()
        self.redraw()
        plt.show()

    def pp_mapping(self):
        """Konwertuje prawdopodobienstwo"""
        pp_sum = sum(self.pp[: self.number_of_points])
        pp_scale = 1.0 / pp_sum
        self.pp[0] = self.pp[0] * pp_scale
        for i in range(1, self.number_of_points):
            self.pp[i] = self.pp[i]*pp_scale + self.pp[i-1]

    def move(self, x2, y2, game_point):
        """Losuje punkty na wykresie"""
        random_pp = random.random()
        for i in range(self.number_of_points):
            if self.pp[i] >= random_pp:
                random_vertex = i
                break
        game_point[0] = (self.x[random_vertex] + game_point[0]) / 2
        game_point[1] = (self.y[random_vertex] + game_point[1]) / 2
        x2[random_vertex].append(game_point[0])
        y2[random_vertex].append(game_point[1])
        return x2, y2, game_point

    def is_inside(self, mX, mY, point):
        """
        Sprawdza czy myszka o wspolrzednych (mX, mY),
        jest w promieniu 2 od punktu point
        """
        return (math.sqrt((point[0] - mX) * (point[0] - mX)
                + (point[1] - mY) * (point[1] - mY)) <= 2)

    def on_press(self, event):
        """Kiedy LPM zostanie nacisniety"""
        if event.inaxes is None:
            return
        mX = event.xdata
        mY = event.ydata
        index = None
        for i in range(len(self.x)):
            if self.is_inside(mX, mY, (self.x[i], self.y[i])):
                index = i
                break
        self.current_point = index

    def on_release(self, event):
        """Kiedy LPM zostanie puszczony"""
        self.current_point = None

    def on_dragg(self, event):
        """Dziala, gdy sie wykona dragg mouse w oknie"""
        if str(event.lastevent.button) == "MouseButton.LEFT":
            mX = event.xdata
            mY = event.ydata
            if mX and mY:
                if self.current_point is not None:
                    self.x[self.current_point] = mX
                    self.y[self.current_point] = mY
                    self.redraw()

    def on_scroll(self, event):
        """Gdy scrolluje to zwieksza/zmniejsza liczbe punktow"""
        if event.button == 'up':
            self.generations += 4000
        elif event.button == 'down':
            if self.generations >= 4000:
                self.generations -= 4000
        self.redraw()

    def redraw(self):
        """Czysci wykres i rysuje go od nowa"""
        x2, y2 = [[] for i in range(len(self.x))], \
                 [[] for i in range(len(self.x))]
        game_point = [random.randint(1, 100),
                      random.randint(1, 100)]
        for i in range(self.generations):
            x2, y2, game_point = self.move(x2, y2, game_point)
        for i in range(10):  # Czyszczenie starych wykresow
            self.plots[i].set_xdata([])
            self.plots[i].set_ydata([])
            self.plots2[i].set_xdata([])
            self.plots2[i].set_ydata([])
        for i in range(len(self.x)):  # Nowe dane wykresow
            self.plots[i].set_xdata(self.x[i])
            self.plots[i].set_ydata(self.y[i])
            self.plots2[i].set_xdata(x2[i])
            self.plots2[i].set_ydata(y2[i])
        self.fig.canvas.draw_idle()

    def set_textboxes(self):
        """Konfiguracja textboxy"""
        plt.text(0.87, 0.95, 'Ustaw prawdopodobienstwo',
                 horizontalalignment='center', verticalalignment='center',
                 transform=self.axes.transAxes)
        for i in range(10):
            axbox = plt.axes([0.95, 0.90 - i*0.035, 0.03, 0.03])
            text_box = TextBox(axbox, '', initial=str(self.pp_values[i]),
                               hovercolor=self.colors[i])
            text_box.on_submit(self.on_submit)
            self.text_boxes.append(text_box)

    def set_slider(self):
        """Konfiguracja slidera"""
        axSlider = plt.axes([0.1, 0.05, 0.8, 0.02])
        slider = Slider(ax=axSlider,
                        label="",
                        valmax=10,
                        valmin=3,
                        valinit=self.init_value,
                        valstep=1,
                        closedmax=True)
        self.sliders[0].append(slider)
        slider.on_changed(self.set_starting_points)

    def do(self):
        """Formatowanie ustawien wykresu"""
        for i in range(10):
            l, = self.axes.plot([], [], "o",
                                color=self.colors[i])
            self.plots.append(l)
            m, = self.axes.plot([], [], ".", markersize=2,
                                color=self.colors[i])
            self.plots2.append(m)
        plt.xlim(1, 100)  # Sprawia, ze wykres sie nie skaluje
        plt.ylim(1, 100)
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.subplots_adjust(left=0, bottom=0.12, right=1, top=1)
        self.set_slider()
        self.set_starting_points(self.init_value)
        self.set_textboxes()

    def set_starting_points(self, number_of_points):
        """Ustawia punkty przy zmianie figur"""
        n = int(number_of_points)
        self.init_value = n
        self.number_of_points = n
        self.x, self.y = [], []
        self.pp = [1] * 10
        self.pp_values = self.pp.copy()
        self.pp_mapping()
        r = 40
        for i in range(n):
            self.x.append(50 + r*math.cos(2*math.pi * i/n))
            self.y.append(50 + r*math.sin(2*math.pi * i/n))
        for i in self.text_boxes:
            i.set_val("1")
        self.redraw()

    def on_submit(self, text):
        """
        Kiedy akcja na text boxie to sprawdzam
        ostatnie prawdopodobienstwa
        """
        self.pp = [float(i.text) for i in self.text_boxes]
        self.pp_values = self.pp.copy()
        self.pp_mapping()
        self.redraw()


if __name__ == "__main__":
    Foremne()
