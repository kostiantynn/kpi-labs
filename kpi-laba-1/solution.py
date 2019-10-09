# This is the main file for a programm

# importing subfunctions from subclasses directory
from subclasses import rect_angle
from subclasses import rect_side

# defining a main function
def main():
    # using try and except to catch none-integer type of input
    try:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        d = int(input('d: '))

        # using a list for checking whether the number is positive.
        input_list = [a, b, c, d]
        for x in input_list:
            if x < 0:
                raise Exception('Numbers should be positive.')

        # checking whether rectangle a,b in the c,d
        if a > c and b > d or a > d and b > c:
            # rising exception if not
            raise Exception('This nubers do not fit in the task.')
        else:
            # execution first grafic
            rect_angle.rect_angle(a,b,c,d)

    except ValueError:
        print('Only integer could be used.')

main()
