from modules.labels import label
from modules.fonts import font1
from modules.lists import list_input, list_num_functions, list_arithmetics_operations, list_sym_functions
from modules.arithmetic_operations import arithmetic_operation
# from modules.symbol_functions import stop_input
#
number = ""
flag_second_operation = False
def get_symbols(symbol):
    global number
    #
    global flag_second_operation
    if len(str(number)) != 16:
        if not flag_second_operation:
            if symbol not in list_arithmetics_operations:
                number += str(symbol) #
                label.setText(number) #
    if symbol in list_arithmetics_operations:
        if not flag_second_operation:
            list_input.append(number)
            number = ""
        print(list_input)
        if len(list_input) == 1:
            print(1)
            list_input.append(symbol)
            print(symbol)
            # if flag_second_operation:
            #     list_input.append(number)
            #     number = ""
    if len(str(number)) != 16:
        if flag_second_operation:
            if symbol not in list_arithmetics_operations:
                number = str()
                number += str(symbol)
                print(number)
                list_input.append(number)
                label.setText(number)
    if symbol == "=" and flag_second_operation:
        print(1000000000)
        list_input.append(number)
        print(list_input)
        number = arithmetic_operation()
        label.setText(str(number))
        # list_input = []
        list_input.clear()
        list_input.append(str(number))
        flag_second_operation = True

    if symbol == "=" and len(list_input) == 3:
        print(list_input)
        if not flag_second_operation:
            list_input.append(number)
        number = arithmetic_operation()
        label.setText(str(number))
        # list_input = []
        list_input.clear()
        list_input.append(str(number))
        flag_second_operation = True



def add_zero():
    get_symbols(0)

def add_one():
    get_symbols(1)

def add_two():
    get_symbols(2)

def add_three():
    get_symbols(3)

def add_four():
    get_symbols(4)

def add_five():
    get_symbols(5)

def add_six():
    get_symbols(6)

def add_seven():
    get_symbols(7)

def add_eight():
    get_symbols(8)

def add_nine():
    get_symbols(9)

def add_plus():
    get_symbols("+")

def add_minus():
    get_symbols("-")

def add_multiply():
    get_symbols("*")

def add_division():
    get_symbols("/")
    
def add_equals():
    get_symbols("=")

list_sym_functions.append(add_division)
list_sym_functions.append(add_multiply)
list_sym_functions.append(add_minus)
list_sym_functions.append(add_plus)
list_sym_functions.append(add_equals)

list_num_functions.append(add_zero)
list_num_functions.append(add_one)
list_num_functions.append(add_two)
list_num_functions.append(add_three)
list_num_functions.append(add_four)
list_num_functions.append(add_five)
list_num_functions.append(add_six)
list_num_functions.append(add_seven)
list_num_functions.append(add_eight)
list_num_functions.append(add_nine)
