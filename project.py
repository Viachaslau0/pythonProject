import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    def __init__(self, json_file):
        self.df = pd.read_json(json_file)
        self.plot_dir = 'plots'
        if not os.path.exists(self.plot_dir):
            os.makedirs(self.plot_dir)

    def draw_plots(self, columns):
        plot_paths = []
        for column in columns:
            self.df[column].plot(kind='bar')
            plt.title(column)
            plot_path = f'{self.plot_dir}/{column}.png'
            plt.savefig(plot_path)
            plot_paths.append(plot_path)
            plt.clf()
        return plot_paths

