import logging
import os

class Repository(object):
    def __init__(self,):
        self.numbers_list = []
        self.duplicated_numbers = 0
        dir_path = os.path.dirname(os.path.realpath(__file__))
        numbers_log = os.path.join(dir_path, 'numbers.log')
        logging.basicConfig(level=logging.DEBUG,
                            format='%(message)s',
                            filename=numbers_log,
                            filemode='w', )

    def save_number(self, number):
        if number not in self.numbers_list:
            self.numbers_list.append(number)
            self.write_new_number(number)
        else:
            self.duplicated_numbers = self.duplicated_numbers + 1

    @staticmethod
    def write_new_number(number):
        logging.info(number)
