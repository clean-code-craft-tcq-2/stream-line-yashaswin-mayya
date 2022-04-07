import sys
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

    def getParametersData(self):

        self.writeToConsole(f'State of Charge(%)\t-\tBattery Temperature(C)\n')

        for sample in range(limit_samples):
            temparature_data = data_generator().parameter_value_generate(BMS_temperature['min_value'], BMS_temperature['max_value'])
            SOC_data = data_generator().parameter_value_generate(BMS_SOC['min_value'], BMS_SOC['max_value'])
            self.writeToConsole(f'{SOC_data}\t-\t{temparature_data}\n')
        

    def writeToConsole(self, consoleMessage):
        sys.stdout.write(f'{consoleMessage}\n')

sender().getParametersData()
