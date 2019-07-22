from  Simple_calculator import Calculator
from Simple_calculator import Animal

import unittest

class CalcTest(unittest.TestCase): #TestCase is superclass
    type_of_calc = "Standard"
    calc = Calculator(type_of_calc)

    def test_Add(self):
        self.assertEqual(self.calc.Add(2,2),4) # AssertEqual is the subclass

    def test_Divide(self):
        self.assertEqual(self.calc.Divide(10,10),1)
    #
    # def test_Mulitple(self):
    #     self.assertNotIsInstance()

    def test_Instance(self):
        self.assertNotIsInstance(self.calc, Animal, msg = "Are you nuts ")




if __name__ == "__main__":
    unittest.main()