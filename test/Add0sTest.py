import unittest

import Add0s


class MyTestCase(unittest.TestCase):
    def test_something(self):
        num = '12345'
        expected = '000012345'
        actual = Add0s.add_0(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
