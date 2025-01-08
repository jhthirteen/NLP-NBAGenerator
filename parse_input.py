import spacy

nlp = spacy.load("en_core_web_sm")

def extract_players(user_input):
    doc = nlp(user_input)
    player_name = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            player_name.append(ent.text)
    print(player_name)


extract_players("Generate a comparison of Shai Gilgeous-Alexander and De'Aron Fox of their three point shooting this season")