import unittest

from badcode_refactored import is_funny_function


class TestIsFunnyFunction(unittest.TestCase):
    def test_data_return_true(self):
        tt = [
            [0],
            [10],
            [-1, -2],
            [1, 2, 3],
            [4, 4, 4, 4],
            [9, 8, 7, 6, 5],
            ['4', '3', '2', '1'],
            (0, 0, 0, 0, 0, 0),
            (-10, -11, -12, -13),
            ['99'] * 1000,
        ]
        for t in tt:
            self.assertTrue(is_funny_function(t),
                            'test failed with data: {}'.format(repr(t)))

    def test_data_return_false(self):
        tt = [
            [9, 6],
            [1, 3, 5],
            [4, 4, 4, 3],
            [9, 8, 7, 6, 3],
            [1] + [99] * 1000,
        ]
        for t in tt:
            self.assertFalse(is_funny_function(t),
                             'test failed with data: {}'.format(repr(t)))

    def test_raise_value_error(self):
        tt = [
            None,
            [],
        ]
        for t in tt:
            msg='test failed with data: {}'.format(repr(t))
            with self.assertRaises(ValueError, msg=msg):
                is_funny_function(t)


if __name__ == '__main__':
    unittest.main()

