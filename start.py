class Start:

    def __init__(self):
        print("""\n
                                ╭━━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭╮
                                ┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃
                                ╰╯┃┃┣┻━┳╮╭┳━━┳━━┳━┻╮╭╋━━┫╰━┳╮
                                ╱╱┃┃┃╭╮┃╰╯┃╭╮┃╭╮┃╭╮┃┃┃╭━┫╭╮┣┫
                                ╱╱┃┃┃╭╮┃┃┃┃╭╮┃╰╯┃╰╯┃╰┫╰━┫┃┃┃┃
                                ╱╱╰╯╰╯╰┻┻┻┻╯╰┻━╮┣━━┻━┻━━┻╯╰┻╯
                                ╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
                                ╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n""")

    def presentation(self):
        name = input("Qual o seu nome? ").capitalize()
        if len(name) < 3 or len(name) > 15: #alterar para aceitar apenas letras
            print("O nome precisa ter no mínimo 3 caracteres.", end = "\n\n")
            return self.presentation()
        return name