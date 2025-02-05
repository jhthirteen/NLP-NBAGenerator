import matplotlib.pyplot as plt
import numpy as np

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

def clean_attempt_strings_to_int(input_data):
    output_data = [int(0)] * len(input_data)
    i = 0
    #loop through attempts --> convert to floats
    for val in input_data:
        output_data[i] = int(val)
        i += 1
    
    return output_data

# Generalized Functions to visualize a statistic either from some subset of a player's last games OR a player's first games

def line_graph_stat_last_games(cleaned_data, stat_string):
    cleaned_data.reverse()
    plt.plot(cleaned_data, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Attempts')
    plt.title(f'{stat_string} over the last {len(cleaned_data)} games')
    plt.xlabel('Games Ago')
    x_ticks = [0] * len(cleaned_data)
    for i in range(len(cleaned_data)):
        x_ticks[i] = i + 1
    x_ticks.reverse()
    plt.xticks(ticks = range(len(cleaned_data)), labels=x_ticks)
    plt.ylabel(f'{stat_string}')
    plt.legend()
    plt.show()

def line_graph_stat_first_games(cleaned_data, stat_string):
    cleaned_data.reverse()
    plt.plot(cleaned_data, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Attempts')
    plt.title(f'{stat_string} over the first {len(cleaned_data)} games')
    plt.xlabel('Games from Start of Season')
    x_ticks = [0] * len(cleaned_data)
    for i in range(len(cleaned_data)):
        x_ticks[i] = i + 1
    plt.xticks(x_ticks)
    plt.ylabel(f'{stat_string}')
    plt.legend()
    plt.show()