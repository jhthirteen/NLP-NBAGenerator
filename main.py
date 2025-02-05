from parse_user_input import extract_info, format_time, find_function_pointers_v2
from data_cmds import fetch_stat_first_games, fetch_stat_last_games
from data_visualizations import clean_percentage_strings_to_float, clean_attempt_strings_to_int, line_graph_stat_first_games, line_graph_stat_last_games

function_pointers_for_data = {
    'fetch_stat_first_games' : fetch_stat_first_games,
    'fetch_stat_last_games' : fetch_stat_last_games
}

function_pointers_for_visualizations = {
    "fetch_stat_first_games" : line_graph_stat_first_games,
    'fetch_stat_last_games' : line_graph_stat_last_games
}

data_clean_function = {
    "float" : clean_percentage_strings_to_float,
    "int" : clean_attempt_strings_to_int,
}

def main():
    user_input = input("What statistical trends would you like to analyze? ")
    json_info = extract_info(user_input)
    stat_string = json_info['stats']
    function_pointer_index_v2 = find_function_pointers_v2(json_info)
    data_type = function_pointer_index_v2['data_type']
    function_to_call = function_pointer_index_v2['function']
    func = function_pointers_for_data[function_to_call]
    stat_tag = function_pointer_index_v2['tag']
    player = json_info['players']
    time = format_time(json_info)
    data = func(player, int(time), 2025, stat_tag)
    
    clean = data_clean_function[data_type]
    visual = function_pointers_for_visualizations[function_to_call]
    
    visual(clean(data), stat_string)

    


main()