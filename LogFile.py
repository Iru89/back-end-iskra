import os
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
numbersLog = os.path.join(os.getenv('HOME'), 'numbers.log')
print('Archivo Log en ', numbersLog)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = numbersLog,
                    filemode = 'w',)

# logging.debug('Comienza el programa')
# logging.info('Procesando con normalidad')
# logging.warning('Advertencia')

def writeNewNumber(num):
    logging.info(num)
