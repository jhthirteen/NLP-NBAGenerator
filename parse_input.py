import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_players(user_input):
    doc = nlp(user_input)
    player_names = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            player_names.append(ent.text)
    return player_names

def extract_statistic(user_input):
    potential_stats = [
        r"three[- ]point",
        r"two[- ]point",
        r"mid[- ]range",
        r"layup",
        r"paint",
        r"dunk",
        r"assist",
        r"steal",
        r"rebound",
        r"block",
        r"three",
        r"two"
    ]


    stat_group = ""
    for stat in potential_stats:
        match = re.search(stat, user_input, re.IGNORECASE)
        if( match ):
            stat_group = match.group(0)
            break

    if( stat_group == "" ):
        print(f"Input Error: Name of statistic could not be processed")
        exit()


extract_statistic("Create a graph for me of Shai Gilgeous-Alexander's three point during this NBA season")