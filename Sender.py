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

        sys.stdout.write(f'State of Charge(%)\tBatteryTemperature(C)\n')
        
        for sample in range(limit_samples):
            temparature_data = data_generator(BMS_temperature['min_value'], BMS_temperature['max_value']).parameter_value_generate()
            SOC_data = data_generator(BMS_SOC['min_value'], BMS_SOC['max_value']).parameter_value_generate()
            sys.stdout.write(f'{SOC_data}\t\t\t{temparature_data}\n')
            #print(f'{SOC_data}\t\t{temparature_data}')
            #time.sleep(1)

if __name__ == '__main__':
    sender().consoleWrite()
