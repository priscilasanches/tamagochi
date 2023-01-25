import random
from services.validation import Validation

class Mascot_model:
    def __init__(self, infos):
        self.name = infos['name'].capitalize()
        self.height = infos['height']
        self.weight = infos['weight']
        self.types = infos['types']
        self.abilities = infos['abilities']
        self.status = {
            "bad_mood": random.randrange(0,11),
            "hungry": random.randrange(0,11),
            "tiredness": random.randrange(0,11)
        }

    def play(self):
        self.status["bad_mood"] -= 5
        self.status["tiredness"] += 2
        self.status["hungry"] += 3
        
        for value in self.status.values():
            value = Validation.limit(value)

    def feed(self):
        self.status["tiredness"] += 1
        self.status["bad_mood"] -= 2
        self.status["hungry"] -= 5

    def sleep(self):
        self.status["tiredness"] -= 10
        self.status["bad_mood"] += 5
        self.status["hungry"] += 5