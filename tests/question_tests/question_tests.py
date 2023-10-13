#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

from src.question_a.question_a import reverse_string

from src.question_b.question_b import get_sum_of_evens

from src.question_c.question_c import get_bonus_pay_amount

from src.question_d.question_d import get_random_number

import random

class Test_Config(unittest.TestCase):

   def test_reverse_string(self):
        self.assertEqual('dlrow olleh', reverse_string("hello world"))

   def test_get_sum_of_evens(self):
       self.assertEqual(30, get_sum_of_evens(11))
       self.assertEqual(30, get_sum_of_evens(10))
       self.assertEqual(20, get_sum_of_evens(8))

   def test_get_bonus_pay_amount(self):
       self.assertEqual("Invalid Argument", get_bonus_pay_amount(-1))
       self.assertEqual(10, get_bonus_pay_amount(200))
       self.assertEqual(36, get_bonus_pay_amount(600))
       self.assertEqual(70, get_bonus_pay_amount(1000))
       self.assertEqual(120, get_bonus_pay_amount(1500))
       self.assertEqual("Invalid Argument", get_bonus_pay_amount(2000))
