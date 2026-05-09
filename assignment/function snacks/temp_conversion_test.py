import unittest

from temp_conversion import *


class TestTempFunctions(unittest.TestCase):
    def test_that_it_is_cold_advisory(self):
        self.assertEqual(temperature_conversion("100c",300),"Cold advisory")




