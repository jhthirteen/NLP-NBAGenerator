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

def line_graph_three_point_percentages_last_games(percentages):
    percentages.reverse()
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Percentage')
    plt.title(f'3-Point Shooting Percentage over the last {len(percentages)} games')
    plt.xlabel('Games Ago')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i + 1
    x_ticks.reverse()
    plt.xticks(ticks = range(len(percentages)), labels=x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_three_point_percentages_first_games(percentages):
    percentages.reverse()
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Percentage')
    plt.title(f'3-Point Shooting Percentage over the first {len(percentages)} games')
    plt.xlabel('Games from Start of Season')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i + 1
    plt.xticks(x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_fieldgoal_point_percentages_last_games(percentages):
    percentages.reverse()
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='Field Goal Percentage')
    plt.title(f'Field Goal Percentage over the last {len(percentages)} games')
    plt.xlabel('Games Ago')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i + 1
    x_ticks.reverse()
    plt.xticks(ticks = range(len(percentages)), labels=x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_fieldgoal_point_percentages_first_games(percentages):
    percentages.reverse()
    plt.plot(percentages, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='Field Goal Percentage')
    plt.title(f'Field Goal Shooting Percentage over the first {len(percentages)} games')
    plt.xlabel('Games from Start of Season')
    x_ticks = [0] * len(percentages)
    for i in range(len(percentages)):
        x_ticks[i] = i + 1
    plt.xticks(x_ticks)
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()

def line_graph_three_point_attempts_last_games(attempts):
    attempts.reverse()
    plt.plot(attempts, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Attempts')
    plt.title(f'3-Point Shooting Attempts over the last {len(attempts)} games')
    plt.xlabel('Games Ago')
    x_ticks = [0] * len(attempts)
    for i in range(len(attempts)):
        x_ticks[i] = i + 1
    x_ticks.reverse()
    plt.xticks(ticks = range(len(attempts)), labels=x_ticks)
    plt.ylabel('Attempts')
    plt.legend()
    plt.show()

def line_graph_three_point_attempts_first_games(attempts):
    attempts.reverse()
    plt.plot(attempts, linewidth=2.5, color='red', marker='o', markersize=10, markeredgecolor='black', markeredgewidth=1, label='3-Point Attempts')
    plt.title(f'3-Point Shooting Attempts over the first {len(attempts)} games')
    plt.xlabel('Games from Start of Season')
    x_ticks = [0] * len(attempts)
    for i in range(len(attempts)):
        x_ticks[i] = i + 1
    plt.xticks(x_ticks)
    plt.ylabel('Attempts')
    plt.legend()
    plt.show()