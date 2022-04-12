import random

class Data_Generator:

    def Parameter_Value_Generator_Digital(self, sensor_bits):
        #return round(random.uniform(range_min, range_max), 3)
        digital_range_min = 0
        digital_range_max = (2**sensor_bits)-1
        return random.randint(digital_range_min, digital_range_max)
    
    def Digital_To_Analog_Converer(self, sensor_bits, sensor_digital_value, range_min, range_max):
        scale = range_max - range_min
        max_digital_value_permissible = (2**sensor_bits)-1
        offset = 0 - range_min
        sensor_analog_value = round(((scale*sensor_digital_value/max_digital_value_permissible)-offset), 3)
        return sensor_analog_value

    def Send_Parameter_Data(self, range_min, range_max, sensor_bits):
        sensor_digital_value = self.Parameter_Value_Generator_Digital(sensor_bits)
        sensor_analog_value = self.Digital_To_Analog_Converer(sensor_bits, sensor_digital_value,range_min, range_max)
        return sensor_analog_value
