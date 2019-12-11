import os
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
numbers_log = os.path.join(os.getenv('HOME'), 'numbers.log')
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    filename=numbers_log,
                    filemode='w', )

# logging.debug('Comienza el programa')
# logging.info('Procesando con normalidad')
# logging.warning('Advertencia')

def writeNewNumber(num):
    logging.info(num)
