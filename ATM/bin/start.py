import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import choice


def hello():
    print('\033[1;31;40m')
    print('*' * 50)
    print('\033[7;31m不是我针对谁，我只想说：在座的除了我都是垃圾！\033[1;31;40m')
    print('*' * 50)
    print('\033[0m')


if __name__ == '__main__':
    hello()
    choice.choice_user()
