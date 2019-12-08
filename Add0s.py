
def add_0(data_str):
    longitud = len(data_str)
    num_of_0 = 9 - longitud
    str_result = ''
    for i in range (num_of_0):
        str_result = str_result.__add__('0')
    return str_result.__add__(data_str)