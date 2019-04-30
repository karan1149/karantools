from collections import defaultdict

def average(arr):
    return float(sum(arr)) / len(arr)

def average_or_0(arr):
    if len(arr):
        return float(sum(arr)) / len(arr)
    else:
        return 0

class AverageStreamer(object):
    def __init__(self):
        self.count = 0
        self.total = 0.0

    def add(self, x):
        self.total += x
        self.count += 1

    def query(self):
        return self.total / self.count

def print_comment_header_block(header_string, length=70):
    print('#' * length)
    left_spaces = (length - 2 - len(header_string)) // 2
    right_spaces = length - 2 - len(header_string) - left_spaces
    print('#' + ' ' * left_spaces + header_string + ' ' * right_spaces + '#')
    print('#' * length)

######################################################################
#                              ASSERTS                               #
######################################################################

def assert_eq(a, b):
    if a != b:
        print_bold("Assert failed because the following two are unequal:")
        print(a)
        print(b)
        raise AssertionError()

def assert_float_eq(a, b, epsilon=1e-5):
    if abs(a - b) > epsilon:
        print_bold("Assert failed because the following two are unequal:")
        print(a)
        print(b)
        raise AssertionError()

def assert_neq(a, b):
    if a == b:
        print_bold("Assert failed because the following two are equal:")
        print(a)
        print(b)
        raise AssertionError()

def assert_float_neq(a, b, epsilon=1e-5):
    if abs(a - b) <= epsilon:
        print_bold("Assert failed because the following two are approximately equal:")
        print(a)
        print(b)
        raise AssertionError()

######################################################################
#                               COLORS                               #
######################################################################

class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @classmethod
    def get(cls, color):
        return getattr(cls, color)


def print_bold(string):
    print(colors.BOLD + string + colors.END)

def print_color(string, color='RED'):
    color_string = colors.get(color.upper())
    print(color_string + string + colors.END)