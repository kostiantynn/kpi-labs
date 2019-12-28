def main():

    sol, length = count_same_symbvols()
    formatted_printing(sol, length)


def count_same_symbvols():
    string = input("Enter sentence: ")
    sol = [x for x in string.split() if x[0] == x[-1]]
    return sol, len(sol)

def formatted_printing(sol, length):
    print('Words: ' + ', '.join(sol))
    print('Count: ' + str(length))

if __name__ == '__main__':
    main()
