import sys
from data_generator import *

Stream_Limit = 50

BMS_Temperature = {
    'min_value': 0,
    'max_value': 45
}

BMS_SOC = {
    'min_value': 20,
    'max_value': 80
}

class Sender:

    def Get_ParametersData(self):

        self.Write_To_Console(f'State of Charge(%)\t-\tBattery Temperature(C)\n')
        sampleCounter = 0
        while sampleCounter < Stream_Limit:
            temparature_data = Data_Generator().Parameter_Value_Generator(BMS_Temperature['min_value'], BMS_Temperature['max_value'])
            SOC_data = Data_Generator().Parameter_Value_Generator(BMS_SOC['min_value'], BMS_SOC['max_value'])
            self.Write_To_Console(f'{SOC_data}\t-\t{temparature_data}\n')
            sampleCounter+=1
        return sampleCounter
        

    def Write_To_Console(self, consoleMessage):
        sys.stdout.write(f'{consoleMessage}\n')
        return consoleMessage

Sender().Get_ParametersData()
