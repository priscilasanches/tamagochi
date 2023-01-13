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
    def choice_menu(name):
        print("\n--------------------------ADOTAR UM MASCOTE---------------------------")
        print(f"""
        {name}, qual será o seu mascote?\n
            1- Bulbasaur
            2- Charmander
            3- Jigglypuff
            4- Pikachu
            5- Squirtle\n""")

    @staticmethod
    def invalid_option(name, option):
        print(f"""Poxa, {name}, a opção {option} não existe.
        \nEscolha uma das opções abaixo.""")