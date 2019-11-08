import unittest

from palindrome import may_be_palindrome


class TestPalindrome(unittest.TestCase):
    def test_string_is_palindrome(self):
        tt = [
            'a',
            'aa',
            'aaa',
            'abba',
            'bbaa',
            'bcaaabc',
            'xzxzyyy',
            '...::::',
            'abc' * 1000,
        ]
        for t in tt:
            self.assertTrue(may_be_palindrome(t),
                            'test failed with data: {}'.format(repr(t)))

    def test_string_is_not_palindrome(self):
        tt = [
            'ab',
            'abc',
            'bcbcbc',
            'cccbbb',
            'aaabbbccc',
            'sdfsdjfsdlkfsjdf',
            'abc' * 1001,
        ]
        for t in tt:
            self.assertFalse(may_be_palindrome(t),
                             'test failed with data: {}'.format(repr(t)))

    def test_raise_type_error(self):
        tt = [
            True,
            123,
            0.99,
            ['a', 'b', 'c'],
            (1, 2, 3),
            {'a': 1, 'b': 2},
            {'q', 'w', 'e', 'r'},
        ]
        for t in tt:
            msg='test failed with data: {}'.format(repr(t))
            with self.assertRaises(TypeError, msg=msg):
                may_be_palindrome(t)


if __name__ == '__main__':
    unittest.main()

