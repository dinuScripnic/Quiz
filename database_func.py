def open_file():
    import json
    try:
        return json.load(open('database.json'))
    except FileNotFoundError:
        return {}
