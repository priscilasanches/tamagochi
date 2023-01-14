class Templates:
    
    @staticmethod
    def start():
        print("""\n
                                ╭━━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭╮
                                ┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃
                                ╰╯┃┃┣┻━┳╮╭┳━━┳━━┳━┻╮╭╋━━┫╰━┳╮
                                ╱╱┃┃┃╭╮┃╰╯┃╭╮┃╭╮┃╭╮┃┃┃╭━┫╭╮┣┫
                                ╱╱┃┃┃╭╮┃┃┃┃╭╮┃╰╯┃╰╯┃╰┫╰━┫┃┃┃┃
                                ╱╱╰╯╰╯╰┻┻┻┻╯╰┻━╮┣━━┻━┻━━┻╯╰┻╯
                                ╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
                                ╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n""")

    @staticmethod
    def main_menu(name):
        print("\n---------------------------------MENU---------------------------------")
        print(f"""
        Oi {name}, o que você quer fazer?\n
            1- Adotar um mascote virtual
            2- Ver seus mascotes
            3- Sair\n""")

    @staticmethod
    def choice_mascot_menu(name, mascots_list):
        option = 0
        print("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        print(f"\n{name}, quem será o seu mascote?", end="\n\n")
        for mascot in mascots_list: 
            option += 1
            print(f"{option} - {mascot.capitalize()}")  

    @staticmethod
    def adoption_menu(name, mascot):
        print("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        print(f"""
        {name}, você deseja:\n
            1- Adotar {mascot.capitalize()}
            2- Ver outras opções
            3- Voltar ao menu inicial\n""")

    @staticmethod
    def interection_mascot_menu(name, mascot_name):
        print(f"---------------------------{mascot_name}---------------------------")
        print(f"""
        {name}, o que você quer fazer?\n
            1- Saber como {mascot_name} está
            2- Alimentar {mascot_name}
            3- Brincar com {mascot_name}
            4- Colocar {mascot_name} para dormir
            5- Voltar ao menu inicial\n""")
    
    @staticmethod
    def show_infos_mascot(mascot):
        print(f"---------------------------{mascot.name}---------------------------")
        print(f"""
            Nome do Pokemon: {mascot.name}
            Altura: {mascot.height} 
            Peso: {mascot.weight} 
            Tipo: {mascot.types}
            Habilidades: {mascot.abilities} 
        """)

    @staticmethod
    def show_adopted_mascots(mascots_list):
        option = 0
        print("\n--------------------------MASCOTES ADOTADOS---------------------------")
        print("\nVocê deseja saber mais sobre:\n")
        for mascot in mascots_list: 
            option += 1
            print(f"{option} - {mascot.name}")  
   
    @staticmethod
    def show_adoption_egg(name, mascot):
        print(f"""
    É isso aí, {name}, {mascot.capitalize()} foi adotado com sucesso. O ovo está chocando!
                                                           
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

    @staticmethod
    def invalid_option(name, option):
        print(f"""Poxa, {name}, a opção {option} não existe.
        \nEscolha uma das opções abaixo.\n\n""")
