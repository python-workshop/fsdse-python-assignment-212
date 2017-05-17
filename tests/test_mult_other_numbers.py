from unittest import TestCase


class TestMult_other_numbers(TestCase):
    def test_mult_other_numbers(self):
        try:
            from build import mult_other_numbers
        except:
            self.assertFalse("No function found")

        self.assertRaises(TypeError, mult_other_numbers, None)
        self.assertEqual(mult_other_numbers([0]), [])
        self.assertEqual(mult_other_numbers([0, 1]), [1, 0])
        self.assertEqual(mult_other_numbers([0, 1, 2]), [2, 0, 0])
        self.assertEqual(mult_other_numbers([1, 2, 3, 4]), [24, 12, 8, 6])
