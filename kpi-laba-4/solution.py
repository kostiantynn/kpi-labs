def main():
    d = int(input('Enter n: '))
    n = 1
    Sum = 0
    factorial_var = 1
    while n <= d:

        Sum += 1/factorial_var
        factorial_var = factorial_var * n
        n+=1
    return Sum

if __name__ == '__main__':
    main()
