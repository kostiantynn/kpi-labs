from math import factorial

def main():
    # will return the biggest value of possible numbers and a number of digits.
    mx_value = max([(__validate_number(3,5), '; 3-digits number'), (__validate_number(2,4), '; 2-digits number'), (__validate_number(4,5), '; 4-digits number')])
    return str(mx_value[0]) + mx_value[1]

def __validate_number(k,n):
    return factorial(n)/factorial(n-k)

if __name__ == '__main__':
    main()
