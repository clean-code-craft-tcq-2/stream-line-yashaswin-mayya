from random import random

class data_generator:

    def __init__(self, min, max):
        self.minumun = min
        self.maximun = max
        self.parameter_value_generator()

    def parameter_value_generator(self):
        return round(random.uniform(self.minumun, self.maximun), 3)