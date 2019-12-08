import re
from typing import Optional, Match


def match(num):
    patron = re.compile('[0-9]{1,9}$')
    check = patron.match(num)
    if check:
        return True
    else:
        return False
