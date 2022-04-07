import random

class data_generator:

    def parameter_value_generate(self, range_min, range_max):
        return round(random.uniform(range_min, range_max), 3)