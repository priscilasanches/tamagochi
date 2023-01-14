from view.templates import Templates
from services.helper import Helper
from services.validation import Validation

class Mascots_controller:

    def get_adopted_mascots(mascots_list, menu_controller):

        if len(mascots_list) == 0:
            print("Nenhum mascote foi adotado ainda =( ", end=2*"\n")
            input("Tecle ENTER para continuar...") 
            menu_controller.main_menu()  
        
        if len(mascots_list) == 1: 
            menu_controller.adopted_mascots_menu(mascots_list[0].name)
            
        Templates.show_adopted_mascots(mascots_list)
        response = input ("\nDigite o número correspondente ao mascote que você deseja ver: ")              
        
        options = Helper.counter_options(mascots_list)
        if Validation.response(response, options): 
            Helper.cls()
            menu_controller.adopted_mascots_menu(mascots_list[int(response)-1].name)
        
        menu_controller.invalid_option(response)
