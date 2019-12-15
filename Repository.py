import logging
import os

class Repository(object):
    def __init__(self,):
        self.numbers_list = []
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        numbers_log = os.path.join(os.getenv('HOME'), 'numbers.log')
        logging.basicConfig(level=logging.DEBUG,
                            format='%(message)s',
                            filename=numbers_log,
                            filemode='w', )

    def save_number(self, number):
        if number not in self.numbers_list:
            self.numbers_list.append(number)
            self.write_new_number(number)

    @staticmethod
    def write_new_number(number):
        logging.info(number)
