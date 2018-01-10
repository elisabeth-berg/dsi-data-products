import numpy as np

class ColorDict():
    def __init__(self):
        self.color_dict = {
        'red' : ['an apple', 'some chair', 'a water bottle', 'a firetruck'],
        'green' : ['an apple', 'kale', 'rabbit food', 'an avocado'],
        'blue' : ['a rainjacket', 'an eye', 'a larkspur', 'a recycle bin'],
        'yellow' : ['eggnog', 'mustard', 'some sweater', 'the sun']}

    def predict(self, color):
        return np.random.choice(self.color_dict[color], 1)
