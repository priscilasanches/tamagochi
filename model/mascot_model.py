class Mascot_model:
    def __init__(self, infos):
        self.name = infos['name'].capitalize()
        self.height = infos['height']
        self.weight = infos['weight']
        self.types = infos['types']
        self.abilities = infos['abilities']