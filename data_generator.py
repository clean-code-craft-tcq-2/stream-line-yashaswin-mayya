import random

class Data_Generator:

    def Parameter_Value_Generator(self, range_min, range_max):
        return round(random.uniform(range_min, range_max), 3)
