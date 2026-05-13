import json

def updateUserID(user_id, steam_id, filename='users.json'):

    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[str(user_id)] = steam_id

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 4)

    
def matchID(user_id, filename='users.json'):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
        return data.get(str(user_id))
    except FileNotFoundError:
        return None