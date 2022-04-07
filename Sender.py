import sys
import time
from Data_Generator import *

limit_samples = 50

BMS_temperature = {
    'min_value': 0,
    'max_value': 45
}

BMS_SOC = {
    'min_value': 20,
    'max_value': 80
}

class sender:

    def consoleWrite(self):

        sys.stdout.write('State of Charge(%)\t\tBatteryTemperature(C)')
        
        for sample in range(limit_samples):
            temparature_data = data_generator(BMS_temperature['min_value'], BMS_temperature['max_value'])
            SOC_data = data_generator(BMS_SOC['min_value'], BMS_SOC['max_value'])
            sys.stdout.write(f'{SOC_data}\t\t{temparature_data}')
            print(f'{SOC_data}\t\t{temparature_data}')
            time.sleep(1)
