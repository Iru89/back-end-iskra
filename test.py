import unittest
import socket

class MyTestCase(unittest.TestCase):
    def test_something(self):
        ipActual = '192.168.1.38'
        hostname = socket.gethostname()
        ipHost = socket.gethostbyname(hostname)
        self.assertEqual(ipActual, ipHost)


if __name__ == '__main__':
    unittest.main()
