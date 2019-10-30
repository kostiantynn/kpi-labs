def main():

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    if a > b:
        raise Exception('An input is not satisfying for given task.')
    else:
        prime_numbers = []
        divider = 2
        for current in range(a, b+1):
            for value in range(divider, current + 1):
                if current % value == 0 and current != value:
                    break
                elif current % value == 0 and current == value:
                    prime_numbers.append(current)
        return prime_numbers

if __name__ == '__main__':
    main()
