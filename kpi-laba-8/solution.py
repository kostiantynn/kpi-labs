from random import randint #using random module to generate random matrix

def main():

    # getting input from user
    length = int(input("length: "))

    # using self-written function to generate matrix with random values
    matrix = gen_random_matrix(length)

    # printing out matrix in porpuse of comparing it with new_matrix
    print_the_matrix(matrix)

    # printing out new matrix
    print_the_matrix(cr_matrix(matrix))


def cr_matrix(matrix):
    n = len(matrix)
    # generate new matrix with costum dimenssion
    new_matrix = gen_matrix_dimension(n)
    for i in range(n):
        for j in range(n):
            new_matrix[i].append(mid_value(matrix[i][j-1],matrix[i][j], matrix[i-1][j],
                                 skip_to_zero(matrix, i, j), skip_to_zero(matrix, i, j)))
    return new_matrix


 # self-written function to make matrix like karno diogramm:

        # a1 a2 a3 | index of (a3 + 1) ==>  a1
        # b1 b2 b3 | and so on...
        # c1 c2 c3 |

def skip_to_zero(matrix, i, j):
    n = len(matrix) - 1
    if i == n:
        return matrix[0][0] if j == n else matrix[0][j+1]
    else:
        return matrix[i+1][0] if j == n else matrix[i+1][j+1]

# random values in matrix
def gen_random_matrix(length):
    matrix = []
    for x in range(length):
        matrix.append([randint(0,100) for i in range(length)])
    return matrix

def mid_value(a, b, c ,d, e):
    return (a + b + c + d + e)/5

# dimenssion of new matrix
def gen_matrix_dimension(length):
    matrix = []
    for x in range(length):
        matrix.append([])
    return matrix

def print_the_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()
    print('-'*10)

if __name__ == '__main__':
    main()
