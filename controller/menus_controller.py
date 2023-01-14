from view.templates import Templates
from model.mascot_model import Mascot_model
from services.validation import Validation
from services.helper import Helper
from services.get_pokemon import Get_pokemon
from .mascots_controller import Mascots_controller

class Menu_controller:

    def __init__(self):
        Helper.cls()
        Templates.start()
        self.username = self.start()
        self.adopted_mascots = []

    def start (self):       
        username = input("Qual o seu nome? ")
        if Validation.name(username): return username.capitalize()  
        return self.start()

    def main_menu (self):
        options = [1, 2, 3]
        
        Templates.main_menu(self.username)
        response = input ("Digite o número correspondente a sua escolha: ") 
        
        if Validation.response(response, options): 
            Helper.cls()
            match int(response):
                case 1:  
                    self.choice_mascot_menu()     
                case 2:
                    Mascots_controller.get_adopted_mascots(self.adopted_mascots, self)
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
            name_chosen_mascot = mascots_availabe[int(response)-1]
            infos = Get_pokemon.get_infos(name_chosen_mascot)
           
            mascot = Mascot_model(infos)
            Templates.show_infos_mascot(mascot)
            
            self.adoption_menu(mascot)

        self.invalid_option(response)
        return self.choice_mascot_menu()

    def adoption_menu(self, mascot):
        options = [1, 2, 3]

        Templates.adoption_menu(self.username, mascot.name)
        response = input("Digite o número correspondente: """)

        if Validation.response(response, options): 
            Helper.cls()
            match int(response):
                case 1:    
                    self.adopted_mascots.append(mascot)              
                    Templates.show_adoption_egg(self.username, mascot.name)
                    input("\n\n     Aperte ENTER para continuar...")
                    Helper.cls()
                    return self.main_menu()
                case 2:
                    return self.choice_mascot_menu()
                case 3:
                    return self.main_menu()

        self.invalid_option(response)
        return self.adoption_menu(mascot)
 
    def adopted_mascots_menu(self, mascot):
        print(f'implementar menu de interaçao com mascote {mascot}')
        self.main_menu()

    def invalid_option(self, option):
        Helper.cls()
        Templates.invalid_option(self.username, option)
