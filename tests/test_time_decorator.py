import unittest
from unittest.mock import patch

from time_decorator import timeit


@timeit
def some_decorated_function(a, b, c=10):
    '''some doc string.'''
    return a, b, c


class TestTimeDecorator(unittest.TestCase):
    def test_save_func_name(self):
        self.assertEqual(some_decorated_function.__name__, 'some_decorated_function')

    def test_save_func_doc(self):
        self.assertEqual(some_decorated_function.__doc__, 'some doc string.')

    def test_save_func_args(self):
        x = 2
        y = 3
        z = 10
        res_x, res_y, *other = some_decorated_function(x, y)
        self.assertEqual(res_x, x, 'returned wrong first argument (x)')
        self.assertEqual(res_y, y, 'returned wrong second argument (y)')

    def test_save_func_kwargs(self):
        x = 3
        y = 6
        z = 9
        res_x, res_y, res_z = some_decorated_function(c=z, b=y, a=x)
        self.assertEqual(res_x, x, 'returned wrong first argument (x)')
        self.assertEqual(res_y, y, 'returned wrong second argument (y)')
        self.assertEqual(res_z, z, 'returned wrong third argument (z)')

    @patch('builtins.print')
    def test_correct_print_info(self, mock_print):
        some_decorated_function(1, 9, c=105)
        output = str(mock_print.call_args)
        self.assertRegex(
            output,
            r'run some_decorated_function\(1, 9, c=105\) took \d+\.?\d* ms\.',
            'incorrigible printed information')


if __name__ == '__main__':
    unittest.main()

