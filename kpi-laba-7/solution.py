from random import randint #using random module to generate list with random values

def main():
    size = int(input("Size of lists: "))
    a = [randint(0,100) for x in range(size)]
    b = [randint(0,100) for x in range(size)]

    print(replaced_value(a,b))

def sum_of_multiplication(arr1,arr2):
    sum = 0
    for x in range(len(arr1)):
        sum += arr1[x] * arr2[x]
    return sum

def replaced_value(arr1,arr2):
    sum = sum_of_multiplication(arr1,arr2)
    arr1[0], arr2[-1] = sum, sum
    return arr1, arr2

if __name__ == '__main__':
    main()
