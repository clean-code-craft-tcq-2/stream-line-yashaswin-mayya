from receiver import *
import unittest
import sys

class Receiver_Test(unittest.TestCase):

    # def test_getRawValuesFromConsole(self):
    #     sys.stdout.writelines("5\n8\n2\n10\n37\n55")
    #     self.assertEqual(Receiver().getRawValuesFromConsole(), [5,8,2,10,37,55])
    
    def test_processInput(self):
        self.assertEqual(Receiver().processInput(['Temperature Data','1','3','5','SOC Data','7','11','18']), ([1,3,5],[7,11,18]))
        self.assertIsInstance(Receiver().processInput(['Temperature Data','1','3','5','SOC Data','7','11','18']), tuple)

    def test_getMinAndMaxData(self):
        self.assertEqual(Receiver().getMinAndMaxData(([1,3,5],[7,11,18])), [1,18])
        self.assertIsInstance(Receiver().getMinAndMaxData(([1,3,5],[7,11,18])), list)

    def test_getSimpleMovingAverage(self):
        self.assertEqual(Receiver().getSimpleMovingAverage(3, ([1,7,5,7,8,4],[8,13,21,43,67,12])), (['-','-',4.33,6.33,6.67,6.33],['-','-',14,25.67,43.67,40.67]))
        self.assertIsInstance(Receiver().getSimpleMovingAverage(3, ([1,7,5,7,8,4],[8,13,21,43,67,12])), (['-','-',4.33,6.33,6.67,6.33],['-','-',14,25.67,43.67,40.67]), tuple)

    def test_calculateSimpleMovingAverage(self):
        self.assertEqual(Receiver().calculateSimpleMovingAverage(3, [1,7,5,7,8,4]), ['-','-',4.33,6.33,6.67,6.33])
        self.assertEqual(Receiver().calculateSimpleMovingAverage(5, [1,7,5,7,8,4]), ['-','-','-','-',5.60,6.20])
        self.assertIsInstance(Receiver().calculateSimpleMovingAverage(5, [1,7,5,7,8,4,6,4,8,5]), list)

    def test_printToConsole(self):
        self.assertEqual(Receiver().printToConsole('Test Data'), 'Test Data')
        self.assertIsInstance(Receiver().printToConsole('Test Data'), str)

    # def test_main(self):
    #     self.assertTrue(Receiver().main())

unittest.main()