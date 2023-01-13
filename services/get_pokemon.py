import json, requests

class Get_pokemon:
    @staticmethod
    def get_infos(pokemon):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        response = json.loads(response.text)

        name = pokemon.capitalize()
        height = response['height']
        weight = response['weight']
        
        types = [types['type']['name'] for types in response['types']]     
        str_types = ''
        for type in types: str_types += f"{type.capitalize()} "
        
        abilities = [abilities['ability']['name'] for abilities in response['abilities']]
        str_abilities = ''             
        for abilitie in abilities: str_abilities += f"{abilitie.capitalize()} "

        return {
            'name': name,
            'height': height,
            'weight': weight,
            'types': str_types,
            'abilities': str_abilities
        }
