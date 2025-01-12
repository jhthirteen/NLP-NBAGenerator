from parse_user_input import extract_info, find_function_pointers, format_time
from data_cmds import fetch_three_point_percentage_first_games, fetch_three_point_percentage_last_games

function_pointers = {
    "fetch_three_point_percentage_first_games" : fetch_three_point_percentage_first_games,
    "fetch_three_point_percentage_last_games" : fetch_three_point_percentage_last_games
}

def main():
    user_input = input("What statistical trends would you like to analyze? ")
    json_info = extract_info(user_input)
    function_pointer_index = find_function_pointers(json_info)
    time = format_time(json_info)

    func = function_pointers[function_pointer_index]
    data = func(json_info['players'], int(time), 2025)
    print(data)


main()