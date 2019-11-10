from math import factorial
# rewrite function for costum input
def validate_custom_number(tuple_list):
    # tuple_list of all possible numbers with their digits numbers
    #  Example: [([array of numbers], their validation), ([...], ...), ...]

    arr_validate = []
    for elem in tuple_list:
        arr_validate.append((__validate_number(elem[1], len(elem[0])), str(elem[1])+'-digit number'))
    return print('max value-' + str(max(arr_validate)[0]) + '; ' + max(arr_validate)[1])


def __validate_number(k,n): # k-lenght of digits in custom number, n-lenght of number in given sequence
    return factorial(n)/factorial(n-k)
