import unittest
import math
from scientific_calculator import (
    sin, cos, tan, sqrt, log, exp, asin, acos, atan, sinh, cosh, tanh
)

class ScientificCalculatorTest(unittest.TestCase):

    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1.0)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1.0)

    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0.0)

    def test_sin_invalid_input(self):
        with self.assertRaises(ValueError):
            sin("hello")

    def test_cos_positive(self):
        self.assertAlmostEqual(cos(0), 1.0)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(180), -1.0)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos(90), 0.0)

    def test_cos_invalid_input(self):
        with self.assertRaises(ValueError):
            cos("world")

    def test_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1.0)

    def test_tan_negative(self):
        self.assertAlmostEqual(tan(-45), -1.0)

    def test_tan_zero(self):
        self.assertAlmostEqual(tan(0), 0.0)

    def test_tan_invalid_input(self):
        with self.assertRaises(ValueError):
            tan("test")

    def test_sqrt_positive(self):
        self.assertAlmostEqual(sqrt(4), 2.0)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_sqrt_invalid_input(self):
        with self.assertRaises(ValueError):
            sqrt("text")

    def test_log_positive(self):
        self.assertAlmostEqual(log(1), 0.0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_invalid_input(self):
        with self.assertRaises(ValueError):
            log("log_test")

    def test_exp_positive(self):
        self.assertAlmostEqual(exp(1), math.e)

    def test_exp_negative(self):
        self.assertAlmostEqual(exp(-1), 1 / math.e)

    def test_exp_zero(self):
        self.assertAlmostEqual(exp(0), 1.0)

    def test_exp_invalid_input(self):
        with self.assertRaises(ValueError):
            exp("exp_test")

    def test_asin_valid_input(self):
        self.assertAlmostEqual(asin(0), 0.0)

    def test_asin_invalid_input_range(self):
        with self.assertRaises(ValueError):
            asin(2)

    def test_asin_invalid_input_type(self):
        with self.assertRaises(ValueError):
            asin("text")

    def test_acos_valid_input(self):
        self.assertAlmostEqual(acos(1), 0.0)

    def test_acos_invalid_input_range(self):
        with self.assertRaises(ValueError):
            acos(-2)

    def test_acos_invalid_input_type(self):
        with self.assertRaises(ValueError):
            acos("text")

    def test_atan_valid_input(self):
        self.assertAlmostEqual(atan(1), 45.0)

    def test_atan_invalid_input_type(self):
        with self.assertRaises(ValueError):
            atan("text")

    def test_sinh_valid_input(self):
        self.assertAlmostEqual(sinh(0), 0.0)

    def test_sinh_invalid_input_type(self):
        with self.assertRaises(ValueError):
            sinh("text")

    def test_cosh_valid_input(self):
        self.assertAlmostEqual(cosh(0), 1.0)

    def test_cosh_invalid_input_type(self):
        with self.assertRaises(ValueError):
            cosh("text")

    def test_tanh_valid_input(self):
        self.assertAlmostEqual(tanh(0), 0.0)

    def test_tanh_invalid_input_type(self):
        with self.assertRaises(ValueError):
            tanh("text")

if __name__ == '__main__':
    unittest.main()
