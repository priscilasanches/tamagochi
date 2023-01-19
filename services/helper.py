import os

class Helper():

    @staticmethod
    def cls(): os.system('cls')

    @staticmethod
    def counter_options(list):
        option = 0
        list_options = []
        for _ in list: 
            option+=1
            list_options.append(option)
        return list_options

    @staticmethod
    def info_hungry(value):
        if value >= 6:
            return ("Está faminto!")
        if value >= 1:
            return ("Está com fome.")
        return ("Está cheinho.")

    @staticmethod
    def info_tiredness(value):
        if value >= 8:
            return ("Está exausto!")
        if value >= 5:
            return ("Está cansado.")
        return ("Está cheio de energia.")

    @staticmethod
    def info_bad_mood(value):
        if value >= 8:
            return ("Está estressado!")
        if value >= 5:
            return ("Está mal humorado.")
        if value >= 2:
            return ("Está contente")
        return ("Está só alegria e felicidade.")
