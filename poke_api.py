import requests
import sys 

POKE_API_URL = 'https://pokeapi.co/api/v2/'
POKE_API_POKEMON_URL = f'{POKE_API_URL}pokemon'

def main(pokemon):
    pokemon = str(sys.argv[pokemon])
    print(f'Searching for "{pokemon}" pokemon...\n', end='', flush=True)
    pokemon_info = get_pokemon_info(pokemon)
    if pokemon_info:
        print('Success')
        print(pokemon_info)
    else:
        print('Failed to retrieve pokemon information')

def get_pokemon_info(pokemon_query):
    cleaned_query = pokemon_query.strip().lower()
    url = f'{POKE_API_POKEMON_URL}/{cleaned_query}'

    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    main(pokemon)