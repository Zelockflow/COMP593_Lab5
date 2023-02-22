from pastebin_api import post_new_paste
from poke_api import get_pokemon_info
import sys

def main():
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)
    title, body_text = construct_paste_info(pokemon_info)
    paste_url = post_new_paste(title, body_text, '1M', False)
    print(f'URL of new paste: {paste_url}')

    return

def get_pokemon_name():
    if len(sys.argv) < 2:
        print("Error: No Pokémon name provided")
        sys.exit(1)
    pokemon_name = sys.argv[1]

    return pokemon_name

def construct_paste_info(pokemon_info):
    name = pokemon_info["name"]
    abilities = pokemon_info["abilities"]
    title = f"{name.capitalize()}'s Abilities"
    body = "- " + "\n- ".join([ability["ability"]["name"] for ability in abilities])
    return (title, body)

if __name__ == '__main__':
    main()
