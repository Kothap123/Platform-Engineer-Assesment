import requests
from bs4 import BeautifulSoup
import sys

def define(word):
    # Here it makes a GET request to the Merriam website
    response = requests.get(f'https://www.merriam-webster.com/dictionary/{given word}')

    # Trying to parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    definition = soup.find('span', class_='dtText')

    if definition is not None:
        # Definition text will be extracted
        definition_text = definition.text.strip()
        # Will try to format the response
        formatted_response = f'{word.capitalize()}:\n{definition_text}\n'
        return formatted_response
    else:
        return f'unable to find a definition for "{given word}"'

if __name__ == '__main__':
    word = sys.argv[1]
    print(define(given word))
