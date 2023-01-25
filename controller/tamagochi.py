from view.templates import Templates
from model.mascot_model import Mascot_model
from services.validation import Validation
from services.helper import Helper
from services.get_pokemon import Get_pokemon
from .mascots_controller import Mascots_controller
import adivinhacao

class Tamagochi:

    def __init__(self):
        Helper.cls()
        Templates.start()
        self.username = self.start()
        self.mascots_availabe = ['bulbasaur', 'charmander', 'jigglypuff', 'pikachu', 'squirtle']
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
        if len(self.mascots_availabe) == 0:
            print(5*"\n", f"Você já adotou todos os mascotes disponíveis. Cuide deles com carinho!\n\n")
            return self.main_menu()
        
        options = Helper.counter_options(self.mascots_availabe)
        
        Templates.choice_mascot_menu(self.username, self.mascots_availabe)
        response = input("\nDigite o número correspondente para ver informações do mascote: ")
        
        if Validation.response(response, options):
            Helper.cls()
            name_chosen_mascot = self.mascots_availabe[int(response)-1]
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
                    self.mascots_availabe.remove(mascot.name.lower())
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
 
    def interection_mascot_menu(self, mascot_name):
        options = [1, 2, 3, 4, 5]
        mascot = Helper.get_mascot_by_name(mascot_name, self.adopted_mascots)
        
        Templates.interection_mascot_menu(self.username, mascot_name)
        response = input("Digite sua opção: ")
        
        if Validation.response(response, options):
            Helper.cls()
            match int(response):
                case 1:
                    Templates.show_infos_mascot(mascot)
                case 2:
                    mascot.feed()
                    print(f"{mascot_name} alimentado!")
                case 3:
                    adivinhacao.jogar()
                    mascot.play()
                    print(f"{mascot_name} se divertiu!")
                case 4:
                    mascot.sleep()
                    print(f"{mascot_name} dormindo!")
                case 5:
                    self.main_menu()

        return self.interection_mascot_menu(mascot_name)

    def invalid_option(self, option):
        Helper.cls()
        Templates.invalid_option(self.username, option)
