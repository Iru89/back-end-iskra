import socket
import unittest
from unittest import TestCase

from Service import Service


class TestService(TestCase):
    def test_check_9_digits(self, ):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        service = Service(20, server_socket, True)
        patterns = ['0', '159263487', '0123456789', '01asd', 'asd01', 'abc', '', 'asdfghjklñ']
        expected = [True, True, False, False, False, False, False, False]
        actual = []
        for p in patterns:
            if service.check_9_digits(p):
                actual.append(True)
            else:
                actual.append(False)
        server_socket.close()
        self.assertEqual(expected, actual)

    def test_nine_digits_format(self,):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        service = Service(20, server_socket, True)
        num = '12345'
        expected = '000012345'
        actual = service.nine_digits_format(num)
        server_socket.close()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()