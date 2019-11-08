import unittest

from iterator import Iterator


class TestIterator(unittest.TestCase):
    def test_return_odd_items(self):
        tt = [
            (['a', 'b', 'c', 'd'], ['a', 'c']),
            ('abababab', ['a', 'a', 'a', 'a']),
            (range(5), [0, 2, 4]),
            ((v for v in [9, 8, 7, 6, 5, 4]), [9, 7, 5]),
        ]
        for t in tt:
            data = t[0]
            wait = t[1]
            it = Iterator(data)
            self.assertEqual([v for v in it], wait,
                            'test failed with data: {}'.format(repr(t)))

    def test_return_even_items(self):
        tt = [
            (['a', 'b', 'c', 'd'], ['b', 'd']),
            ('abababab', ['b', 'b', 'b', 'b']),
            (range(5), [1, 3]),
            ((v for v in [9, 8, 7, 6, 5, 4]), [8, 6, 4]),
        ]
        for t in tt:
            data = t[0]
            wait = t[1]
            it = Iterator(data, even=True)
            self.assertEqual([v for v in it], wait,
                            'test failed with data: {}'.format(repr(t)))

    def test_is_repeatable(self):
        arr = [1, 2, 3, 4, 5, 6]
        wait = [1, 3, 5]
        it = Iterator(arr)
        self.assertEqual([v for v in it], wait, 'test failed on first call')
        self.assertEqual([v for v in it], wait, 'test failed on second call')


if __name__ == '__main__':
    unittest.main()

