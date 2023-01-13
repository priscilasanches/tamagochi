import json, requests
from services.validation import Service

class Menus:

    def __init__(self, name_user):
        self.name = name_user

    def main_menu(self):
        options = {1, 2, 3}
        response = ''
       
        print("\n---------------------------------MENU---------------------------------")
        response = input(f"""
        Oi {self.name}, o que você quer fazer?\n
            1- Adotar um mascote virtual
            2- Ver seus mascotes
            3- Sair\n
            Digite o número correspondente a sua escolha: """) 
        
        if Service.valida_response(response, options): 
            match int(response):
                case 1:
                    Menus.choice(self)     
                case 2:
                    return print("\n\nNão implementado: ver mascotes.")
                case 3:
                    exit()

        self.invalid_option(response)
        return self.main_menu()
        
    def choice(self):
        pokemon_availabe = ['bulbasaur', 'charmander', 'jigglypuff', 'pikachu', 'squirtle']

        print("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        chosen = input(f"""
        {self.name}, qual será o seu mascote?\n
            1- Bulbasaur
            2- Charmander
            3- Jigglypuff
            4- Pikachu
            5- Squirtle\n
            Digite o número correspondente para ver mais informações: """)

        if Service.valida_response(chosen, {1,2,3,4,5}): 
            Menus.get_info(self, pokemon_availabe[int(chosen)-1])

        self.invalid_option(chosen)
        return self.choice()
    
    def adoption(self, mascot):
        option = input(f"""
        {self.name}, você deseja:\n
            1- Adotar {mascot}
            2- Ver outras opções
            3- Voltar ao menu inicial\n
            Digite o número correspondente: """)

        if Service.valida_response(option, {1, 2, 3}): 
            match int(option):
                case 1:
                    print(f"""
    É isso aí, {self.name}, {mascot} foi adotado com sucesso. O ovo está chocando!
                                                           
                              ████                              
                            ██░░░░██                            
                          ██░░░░░░░░██                          
                          ██░░░░░░░░██                          
                        ██░░░░░░░░░░░░██                        
                        ██░░░░░░░░░░░░██                        
                        ██░░░░░░░░░░░░██                        
                          ██░░░░░░░░██                          
                            ████████                            
""")
                    return self.main_menu()
                case 2:
                    return self.choice()
                case 3:
                    return self.main_menu()

        self.invalid_option(option)
        return self.adoption(mascot)

    def invalid_option(self, option):
        Service.cls()
        print(f"""
            Poxa, {self.name}, a opção {option} não existe.
            Escolha uma das opções abaixo.
            """)

    def get_info(self, pokemon):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        response = json.loads(response.text)
        
        name = pokemon.capitalize()
        height = response['height']
        weight = response['weight']
        types = [types['type']['name'] for types in response['types']]
        abilities = [abilities['ability']['name'] for abilities in response['abilities']]

        Menus.show_info(self, {
            'name': name,
            'height': height,
            'weight': weight,
            'type': types,
            'abilities': abilities
        })

    def show_info(self, infos):
        str_types = ''
        str_abilities = ''
        
        for types in infos['type']:
            str_types += f"{types.capitalize()} "

        for abilities in infos['abilities']:
            str_abilities += f"{abilities.capitalize()} "
        
        Service.cls()
        print(f"---------------------------{infos['name']}---------------------------")
        print(f"""
            Nome do Pokemon: {infos['name']}
            Altura: {infos['height']} metros
            Peso: {infos['weight']} quilos
            Tipo: {str_types}
            Habilidades: {str_abilities} 
        """)
        return Menus.adoption(self, infos['name'])
    

