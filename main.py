from parse_user_input import extract_info, find_function_pointers, format_time
from data_cmds import fetch_three_point_percentage_first_games, fetch_three_point_percentage_last_games

function_pointers = {
    "fetch_three_point_percentage_first_games" : fetch_three_point_percentage_first_games,
    "fetch_three_point_percentage_last_games" : fetch_three_point_percentage_last_games
}

def main():
    user_input = input("What statistical trends would you like to analyze? ")
    json_info = extract_info(user_input)
    




main()