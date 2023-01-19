class Validation:
      
    @staticmethod
    def response(response, options):
        try:
            if not response or int(response) not in options: return False      
        except:
            return False
        return True

    @staticmethod
    def name(name):
        
        if len(name) >= 3 and len(name) <= 15: return True
        
        print("O nome precisa ter no mínimo 3 e no máximo 15 caracteres.", end = "\n\n")
        return False

    @staticmethod
    def limit(actual_value, limit):
        if actual_value > limit[1]:
            return limit[1]
        if actual_value < limit[0]:
            return limit[0]
        return actual_value