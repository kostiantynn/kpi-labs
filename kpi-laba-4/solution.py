from math import factorial

def main():
    d = int(input('Enter n: '))
    n = 1
    Sum = 0
    while n <= d:
        Sum += 1/factorial(n)
        n+=1
    return Sum

if __name__ == '__main__':
    main()