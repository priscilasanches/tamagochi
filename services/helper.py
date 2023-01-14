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