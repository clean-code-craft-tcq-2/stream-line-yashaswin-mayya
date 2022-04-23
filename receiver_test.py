from receiver import *
import unittest
import sys

class Receiver_Test(unittest.TestCase):

    def test_getRawValuesFromConsole(self):
        sys.stdout.writelines("5\n8\n2\n10\n37\n55\n")
        Receiver().getRawValuesFromConsole()
    
    def test_processInput(self):
        self.assertEqual(Receiver().processInput(['Temperature Data','1','3','5','SOC Data','7','11','18']), ([1,3,5],[7,11,18]))

    def test_getMinAndMaxData(self):
        self.assertEqual(Receiver().getMinData(([1,3,5],[7,11,18])), 1)
        self.assertEqual(Receiver().getMaxData(([1,3,5],[7,11,18])), 18)

    def test_getSimpleMovingAverage(self):
        self.assertEqual(Receiver().getSimpleMovingAverage(3, ([1,7,5,7,8,4],[8,13,21,43,67,12])), (['-','-',4.33,6.33,6.67,6.33],['-','-',14,25.67,43.67,40.67]))
        
    def test_calculateSimpleMovingAverage(self):
        self.assertEqual(Receiver().calculateSimpleMovingAverage(3, [1,7,5,7,8,4]), ['-','-',4.33,6.33,6.67,6.33])
        self.assertEqual(Receiver().calculateSimpleMovingAverage(5, [1,7,5,7,8,4]), ['-','-','-','-',5.60,6.20])

    def test_printToConsole(self):
        self.assertEqual(Receiver().printToConsole('All is Well!'), 'All is Well!')


unittest.main()
