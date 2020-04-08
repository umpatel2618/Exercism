class Allergies:
    panel = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(Allergies.panel[item] & self.score)

    @property
    def lst(self):
        return [
            item
            for item in Allergies.panel
            if self.allergic_to(item)
        ]