import numpy


def first_matrix():
    a = []
    row = []
    n, m = input("Enter size of matrix:").split()
    print("Enter matrix:")
    for i in range(int(n)):
        line = input().split()
        for num in line:
            if "." in num:
                row.append(float(num))
            else:
                row.append(int(num))
        a.append(row)
        row = []
    return a


def second_matrix():
    b = []
    row_2 = []
    n_2, m_2 = input("Enter size of second matrix").split()
    print("Enter second matrix:")
    for i in range(int(n_2)):
        line = input().split()
        for num in line:
            if "." in num:
                row_2.append(float(num))
            else:
                row_2.append(int(num))
        b.append(row_2)
        row_2 = []
    return b


def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("This operation cannot be performed.")
    else:
        result = [[a[x][y] + b[x][y] for y in range(len(a[0]))] for x in range(len(a))]
        return result


def mult_constant(a):
    factor = int(input("Enter constant:"))
    result = [[a[x][y] * factor for y in range(len(a[0]))] for x in range(len(a))]
    return result


def mult_matrix(a, b):
    result = [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]
    return result


def transpose(a):
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    choice = int(input("Your choice:"))
    if choice == 1:
        result = [[a[x][y] for x in range(len(a))] for y in range(len(a[0]))]
        return result
    if choice == 2:
        result = [[a[x][y] for x in range(len(a))] for y in range(len(a[0]))]
        for line in result:
            line.reverse()
        result.reverse()
        return result
    if choice == 3:
        for line in a:
            line.reverse()
        return a
    if choice == 4:
        a.reverse()
        return a


def determinant(a):
    a = numpy.array(a)
    result = numpy.linalg.det(a)
    return result


def inverse(a):
    np = numpy.array(a)
    d = numpy.linalg.det(np)
    if d == 0:
        return "This matrix doesn't have an inverse."
    return numpy.linalg.inv(np)


def start(command):
    if command == 1:
        a = first_matrix()
        b = second_matrix()
        return add_matrix(a, b)
    if command == 2:
        a = first_matrix()
        return mult_constant(a)
    if command == 3:
        a = first_matrix()
        b = second_matrix()
        return mult_matrix(a, b)
    if command == 4:
        a = first_matrix()
        return transpose(a)
    if command == 5:
        a = first_matrix()
        return determinant(a)
    if command == 6:
        a = first_matrix()
        return inverse(a)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    action = int(input("Your choice:"))
    if action == 0:
        break
    elif action == 5:
        det = start(action)
        print("The result is:")
        print(int(round(det)))
        print()
    elif action == 6:
        inv = start(action)
        if type(inv) is str:
            print(inv)
        else:
            print("The result is:")
            for r in inv:
                print(*r)
            print()
    else:
        matrix = start(action)
        print("The result is:")
        for r in matrix:
            print(*r)
        print()
