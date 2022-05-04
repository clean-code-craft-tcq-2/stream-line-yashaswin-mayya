import sys
from data_generator import *

Stream_Limit = 50

Sensor_Bits = 12

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
        
        
        self.Write_To_Console(f'State of Charge(%), Battery Temperature(°C)')

        sampleCounter = 0
        while sampleCounter < Stream_Limit:
            temparature_data = Data_Generator().Send_Parameter_Data(BMS_Temperature['min_value'], BMS_Temperature['max_value'], Sensor_Bits)
            SOC_data = Data_Generator().Send_Parameter_Data(BMS_SOC['min_value'], BMS_SOC['max_value'], Sensor_Bits)
            self.Write_To_Console(f'{SOC_data}, {temparature_data}')
            sampleCounter+=1

        return sampleCounter
        

    def Write_To_Console(self, consoleMessage):
        sys.stdout.write(f'{consoleMessage}\n')
        return consoleMessage

Sender().Get_ParametersData()
