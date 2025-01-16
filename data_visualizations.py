import matplotlib.pyplot as plt
import numpy as np

#test_data = ['.250', '1.000', '.167', '.500', '.667']
"""
TODO: Idea --> add functionality to create labels for each data point when the user hovers / clicks on it
"""

def clean_percentage_strings_to_float(input_data):
    output_data = [float(0)] * len(input_data)
    i = 0
    #loop through percentages --> convert to floats
    for val in input_data:
        output_data[i] = float(val) * 100
        i += 1

    return output_data

def line_graph_three_point_percentages_last_games(percentages):
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Percentage')
    plt.title(f'3-Point Shooting Percentage over the last {len(percentages)} games')
    plt.xlabel('Games')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i
    plt.xticks(x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_three_point_percentages_first_games(percentages):
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Percentage')
    plt.title(f'3-Point Shooting Percentage over the first {len(percentages)} games')
    plt.xlabel('Games')
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_fieldgoal_point_percentages_last_games(percentages):
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='Field Goal Percentage')
    plt.title(f'Field Goal Percentage over the last {len(percentages)} games')
    plt.xlabel('Games')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i
    plt.xticks(x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_fieldgoal_point_percentages_first_games(percentages):
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='Field Goal Percentage')
    plt.title(f'Field Goal Shooting Percentage over the first {len(percentages)} games')
    plt.xlabel('Games')
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()