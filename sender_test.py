from sender import *
from data_generator import *
import unittest

class Sender_Test(unittest.TestCase):

    def test_Parameter_Value_Generator_Digital(self):
        #Parameter Value Generator is defined to generate random values within a range in order to simulate sensor data, hence no definite assert such as assertTrue 
        self.assertIsNotNone(Data_Generator().Parameter_Value_Generator_Digital(12))
        self.assertGreaterEqual(Data_Generator().Parameter_Value_Generator_Digital(12), 0)
        self.assertLessEqual(Data_Generator().Parameter_Value_Generator_Digital(12), 4096)
        self.assertLessEqual(Data_Generator().Parameter_Value_Generator_Digital(10), 1024)
        self.assertIsInstance(Data_Generator().Parameter_Value_Generator_Digital(12), int)

    def test_Digital_To_Analog_Converer(self):
        self.assertEqual(Data_Generator().Digital_To_Analog_Converer(12, 0, 0, 50), 0)
        self.assertEqual(Data_Generator().Digital_To_Analog_Converer(12, 1023, 0, 50), 12.491)
        self.assertEqual(Data_Generator().Digital_To_Analog_Converer(10, 511, 0, 50), 24.976)
        self.assertEqual(Data_Generator().Digital_To_Analog_Converer(10, 511, 50, 150), 99.951)

    def test_Send_Parameter_Data(self):
        pass
        self.assertIsNotNone(Data_Generator().Send_Parameter_Data(0, 50, 12))
        self.assertGreaterEqual(Data_Generator().Send_Parameter_Data(0, 50, 12), 0)
        self.assertLessEqual(Data_Generator().Send_Parameter_Data(0, 50, 12), 50)
        self.assertIsInstance(Data_Generator().Send_Parameter_Data(0, 50, 12), float)

    
    def test_Get_Parameter_To_Send(self):
        self.assertEqual(Sender().Get_ParametersData(), 50)

    def test_Write_To_Console(self):
        self.assertEqual(Sender().Write_To_Console('Test Data'), 'Test Data')
        self.assertIsInstance(Sender().Write_To_Console('Test Data'), str)

unittest.main()
