import requests

def get_questions(url):
    """
    get_questions(url)
    requires an url, from where it takes all the data and
    """
    import requests
    print('Processing request...')
    questions = requests.get(url)
    questions = questions.json()
    return questions


class Question: