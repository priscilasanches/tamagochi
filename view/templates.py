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
    def choice_mascot_menu(name):
        print("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        print(f"""
        {name}, qual será o seu mascote?\n
            1- Bulbasaur
            2- Charmander
            3- Jigglypuff
            4- Pikachu
            5- Squirtle\n""")

    @staticmethod
    def adoption_menu(name, mascot):
        ("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        print(f"""
        {name}, você deseja:\n
            1- Adotar {mascot.capitalize()}
            2- Ver outras opções
            3- Voltar ao menu inicial\n""")

    @staticmethod
    def show_infos_mascot(infos):
        print(f"---------------------------{infos['name']}---------------------------")
        print(f"""
            Nome do Pokemon: {infos['name']}
            Altura: {infos['height']} 
            Peso: {infos['weight']} 
            Tipo: {infos['types']}
            Habilidades: {infos['abilities']} 
        """)

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
        \nEscolha uma das opções abaixo.""")