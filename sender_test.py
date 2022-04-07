#import sys
from sender import *
from data_generator import *
import unittest

class Sender_Test(unittest.TestCase):

    # def test_data(self):
    #     sys.stdin.readlines()

    def test_Parameter_Value_Generator(self):
        self.assertIsNotNone(Data_Generator().Parameter_Value_Generator(0,50))
        self.assertGreaterEqual(Data_Generator().Parameter_Value_Generator(0,50), 0)
        self.assertLessEqual(Data_Generator().Parameter_Value_Generator(0,50), 50)
        self.assertIsInstance(Data_Generator().Parameter_Value_Generator(0,50), float)
    
    def test_Get_Parameter_To_Send(self):
        self.assertEqual(Sender().Get_ParametersData(), 50)

    def test_Write_To_Console(self):
        self.assertEqual(Sender().Write_To_Console('Test Data'), 'Test Data')
        self.assertIsInstance(Sender().Write_To_Console('Test Data'), str)

unittest.main()