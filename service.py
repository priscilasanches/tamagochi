class Service:
      
    @staticmethod
    def cls(): print ("\n" * 20)

    @staticmethod
    def valida_response(response, options):
        try:
            if not response or int(response) not in options: return False      
        except:
            return False
        return True
    