import os
import json 
import re
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPENAI_NLP_KEY"))

def extract_info(user_input):

    system_prompt = (
        "You are an assistant specifically designed for an application that processes information related to the NBA. "
        "Based on the given user input, you are to extract three key pieces of information: "
        "the player(s) the user wishes to search for, the statistic(s) they wish to search for, "
        "and the period of time they wish to search for. "
        "When extracting information, please respond with pure JSON only, "
        "without any extra text, markdown, or explanations. The JSON should be structured "
        "with the player's name, the statistic, and the time frame, like this: "
        '{"players": "Player Name", "stats": "Statistic", "time": "Time Period"}.'
    )

    response = client.chat.completions.create(
        messages=[
            {"role" : "system", "content" : system_prompt},
            {"role" : "user", "content" : user_input}
        ],
        model="gpt-4o",
        temperature=0.0 #for more deterministic results
    )

    response_content = response.choices[0].message.content

    try:
        parsed_response = json.loads(response_content)
    except json.JSONDecodeError as e:
        print(e)
        exit()

    return parsed_response

def format_time(extracted_json_info):

    system_prompt = (
        "You are an assistant specifically designed for an application that processes information related to the NBA. "
        "Based on the given period of time that the user is searching for, you are to format the output in one of the following ways: "
        "If the user is searching for a speciifc number of games, output that number of games and nothing more (for example: 10). "
        "If the user is searching for a specific period of time, like a specific week or month, output the range of the dates in month/day/year format (for example: 11/1/24 - 11/8/24). "
        "If the user is searching for a specific season, output the last year of that season (for example: If the user is searching for stats from the 2021-2022 season, you would output 2022)"
    )

    response = client.chat.completions.create(
        messages=[
            {"role" : "system", "content" : system_prompt},
            {"role" : "user", "content" : extracted_json_info['time']}
        ],
        model="gpt-4o",
        temperature=0.0 #for more deterministic results
    )

    response_content = response.choices[0].message.content
    return response_content


def find_function_pointers(extracted_json_info):

    system_prompt = (
        "You are an assistant specifically designed for an application that processes information related to the NBA. "
        "Based on the given statistic to search for and time frame, along with a series of function pointers, you are to determine the correct function to call. You need to match the statistic to a given statistic tag, and call the function with the correct time frame "
        "The possible tags are: "
        "Minutes Played = mp, Field Goals Made = fg, Field Goals Attempted = fga, Field Goal Percentage = fg_pct, Three Pointers = fg3, Three Point Field Goals Attempted = fg3a, Three Point Percentage = fg3_pct, Free Throws = ft, Free Throws Attempted = fta, Free Throw Percentage = ft_pct, Offensive Rebounds = orb, Defensive Rebounds = drb, Total Rebounds = trb, Assists = ast, Steals = stl, Blocks = blk, Turnovers = tov, Fouls = pf, Points = pts, Game Score = game_score, Box-Score Plus Minus = plus_minus"
        "The possible functions to call are: "
        "fetch_stat_first_games and fetch_stat_last_games"
        "Further, output if this kind of statistic that we would be looking for would be best represented by a floating point number (if there are decimals) or integers"
        "When making a decision, please respond with pure JSON only."
        "without any extra text, markdown, or explanations. The JSON should be structured "
        "with the statistic tag, and the function name, like this: "
        '{"tag": "stat_tag", "function": "function_to_call", "data_type" : "float or int"}.'
    )

    user_prompt = f"The stat is {extracted_json_info['stats']} and the time period is {extracted_json_info['time']}"

    response = client.chat.completions.create(
        messages=[
            {"role" : "system", "content" : system_prompt},
            {"role" : "user", "content" : user_prompt}
        ],
        model="gpt-4o",
        temperature=0.0 #for more deterministic results
    )

    response_content = response.choices[0].message.content

    try:
        parsed_response = json.loads(response_content)
    except json.JSONDecodeError as e:
        print(e)
        exit()

    return parsed_response