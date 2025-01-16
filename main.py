from parse_user_input import extract_info, find_function_pointers, format_time
from data_cmds import fetch_three_point_percentage_first_games, fetch_three_point_percentage_last_games, fetch_fieldgoal_point_percentage_first_games, fetch_fieldgoal_point_percentage_last_games
from data_visualizations import clean_percentage_strings_to_float, line_graph_three_point_percentages_last_games, line_graph_three_point_percentages_first_games, line_graph_fieldgoal_point_percentages_last_games, line_graph_fieldgoal_point_percentages_first_games

function_pointers_for_data = {
    "fetch_three_point_percentage_first_games" : fetch_three_point_percentage_first_games,
    "fetch_three_point_percentage_last_games" : fetch_three_point_percentage_last_games,
    "fetch_fieldgoal_point_percentage_first_games" : fetch_fieldgoal_point_percentage_first_games,
    "fetch_fieldgoal_point_percentage_last_games" : fetch_fieldgoal_point_percentage_last_games
}

data_function_params = {
    "fetch_three_point_percentage_first_games" : 3,
    "fetch_three_point_percentage_last_games" : 3,
    "fetch_fieldgoal_point_percentage_first_games" : 3,
    "fetch_fieldgoal_point_percentage_last_games" : 3
}

function_pointers_for_visualizations = {
    "fetch_three_point_percentage_first_games" : line_graph_three_point_percentages_first_games,
    "fetch_three_point_percentage_last_games" : line_graph_three_point_percentages_last_games,
    "fetch_fieldgoal_point_percentage_first_games" : line_graph_fieldgoal_point_percentages_first_games,
    "fetch_fieldgoal_point_percentage_last_games" : line_graph_fieldgoal_point_percentages_last_games
}

def main():
    user_input = input("What statistical trends would you like to analyze? ")
    json_info = extract_info(user_input)
    function_pointer_index = find_function_pointers(json_info)
    time = format_time(json_info)

    func = function_pointers_for_data[function_pointer_index]
    data = func(json_info['players'], int(time), 2025)
    visual = function_pointers_for_visualizations[function_pointer_index]
    visual(clean_percentage_strings_to_float(data))


main()