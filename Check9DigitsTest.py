import unittest
import Check9Digits


class MyTestCase(unittest.TestCase):
    def test_something(self):
        patterns = ['0', '159263487', '0123456789', '01asd', 'asd01', 'abc', '', 'asdfghjklñ']
        expected = [True, True, False, False, False, False, False, False]
        actual = []
        for p in patterns:
            if Check9Digits.match(p):
                actual.append(True)
            else:
                actual.append(False)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
