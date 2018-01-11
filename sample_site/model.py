import numpy as np

class ColorDict():
    def __init__(self):
        self.color_dict = {
        'red' : ['an apple', 'a sunburn', "Liz's water bottle", 'a firetruck', 'blood'],
        'green' : ['a Granny Smith apple', 'kale', 'rabbit food', 'an avocado'],
        'blue' : ['a rainjacket', 'an eye', 'a larkspur', 'a recycle bin', 'this website'],
        'yellow' : ['eggnog', 'mustard', 'the sun', 'a post-it note']}

    def predict(self, color):
        return np.random.choice(self.color_dict[color], 1)
