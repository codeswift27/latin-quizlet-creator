# API from https://www.latin-is-simple.com ❤︎

import requests


def main():
    
    # Get words from user
    words = input('Input latin: ').split()
    print('\nVocab list (copy & paste into Quizlet):')

    for word in words:
        # Fetch data
        url = 'https://www.latin-is-simple.com/api/vocabulary/search/'
        params = {'query' : word, 'forms_only' : 'true'}
        data = requests.get(url, params).json()
        word = next(w for w in data if w)

        # Get full form / principle parts
        part_of_speech = word['type']['name']
        term = word['full_name'].replace('[','(').replace(']',')')
        if part_of_speech == 'verb':
            term = term.split(', ')
            term.pop(1)
            term[1] = term[1][:-2]
            term = ', '.join(term).lower()
        elif part_of_speech == 'noun':
            term = term[:-2].lower()
            
        # Get translation
        translation = word['translations_unstructured']['en'].split(', ')
        translation = ', '.join([*set(translation)])

        print(term + ' - ' + translation)

main()