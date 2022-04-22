from receiver import *
import unittest

class Receiver_Test(unittest.TestCase):

    def test_calculateSimpleMovingAverage(self):
        self.assertEqual(Receiver().calculateSimpleMovingAverage(3, [1,7,5,7,8,4]), ['-','-',4.33,6.33,6.67,6.33])
        self.assertEqual(Receiver().calculateSimpleMovingAverage(5, [1,7,5,7,8,4]), ['-','-','-','-',5.60,6.20])
        self.assertIsInstance(Receiver().calculateSimpleMovingAverage(5, [1,7,5,7,8,4,6,4,8,5]), list)

    def test_printToConsole(self):
        self.assertEqual(Receiver().printToConsole('Test Data'), 'Test Data')
        self.assertIsInstance(Receiver().printToConsole('Test Data'), str)

unittest.main()