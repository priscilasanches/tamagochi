from view.templates import Templates
#from model.mascot_model import Mascot
from services.validation import Validation
from services.helper import Helper
from services.get_pokemon import Get_pokemon

class Tamagochi:

    def __init__(self):
        Helper.cls()
        Templates.start()
        self.username = self.start()

    def start (self):       
        username = input("Qual o seu nome? ")
        if Validation.name(username): return username.capitalize()  
        return self.start()

    def main_menu (self):
        options = [1, 2, 3]
        
        Templates.main_menu(self.username)
        response = input ("Digite o número correspondente a sua escolha: ") 
        
        if Validation.response(response, options): 
            match int(response):
                case 1:
                    Helper.cls()
                    self.choice_mascot_menu()     
                case 2:
                    Helper.cls()
                    print("\n\nVer mascotes não implementado.")
                    self.main_menu()
                case 3:
                    exit()

        self.invalid_option(response)
        return self.main_menu()

    def choice_mascot_menu(self):
        mascots_availabe = ['bulbasaur', 'charmander', 'jigglypuff', 'pikachu', 'squirtle']
        options = [1, 2, 3, 4, 5]
        
        Templates.choice_mascot_menu(self.username)
        response = input("Digite o número correspondente para ver informações do mascote: ")
        
        if Validation.response(response, options):
            Helper.cls()
            chosen_mascot = mascots_availabe[int(response)-1]
            infos = Get_pokemon.get_infos(chosen_mascot)
            Templates.show_infos_mascot(infos)
            self.adoption_menu(chosen_mascot)

        self.invalid_option(response)
        return self.choice_mascot_menu()

    def adoption_menu(self, mascot):
        options = [1, 2, 3]

        Templates.adoption_menu(self.username, mascot)
        response = input("Digite o número correspondente: """)

        if Validation.response(response, options): 
            Helper.cls()
            match int(response):
                case 1:
                    Templates.show_adoption_egg(self.username, mascot)
                    input("     Aperte ENTER para continuar...")
                    Helper.cls()
                    return self.main_menu()
                case 2:
                    return self.choice_mascot_menu()
                case 3:
                    return self.main_menu()

        self.invalid_option(response)
        return self.adoption(mascot)

    def invalid_option(self, option):
        Helper.cls()
        Templates.invalid_option(self.username, option)
