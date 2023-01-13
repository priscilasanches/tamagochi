from view.templates import Templates
from services.validation import Validation
from services.helper import Helper

class Tamagochi:

    def __init__(self):
        Templates.start()
        self.username = self.start()

    def start (self):       
        username = input("Qual o seu nome? ")
        if Validation.name(username): return username  
        return self.start()

    def main_menu (self):
        options = {1, 2, 3}
        
        Templates.main_menu(self.username)
        response = input ("Digite o número correspondente a sua escolha: ") 
        
        if Validation.response(response, options): 
            match int(response):
                case 1:
                    self.choice()     
                case 2:
                    Helper.cls()
                    print("\n\nVer mascotes não implementado.")
                    self.main_menu()
                case 3:
                    exit()

        self.invalid_option(response)
        return self.main_menu()

    def choice(self):
        pokemon_availabe = ['bulbasaur', 'charmander', 'jigglypuff', 'pikachu', 'squirtle']
        
        Templates.choice_menu
        response = input("Digite o número correspondente para ver mais informações: ")
        
        if Validation.response(chosen, {1,2,3,4,5}): 
            Menus.get_info(self, pokemon_availabe[int(chosen)-1])

        self.invalid_option(chosen)
        return self.choice()

    def invalid_option(self, option):
        Helper.cls()
        Templates.invalid_option(self.username, option)
