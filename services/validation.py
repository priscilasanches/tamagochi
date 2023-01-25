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
    def limit(actual_value):
        if actual_value > 10:
            return 10
        if actual_value < 0:
            return 0
        return actual_value