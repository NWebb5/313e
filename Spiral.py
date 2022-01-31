#  File: Spiral.py

#  Description: Given an input dimension and a set of numbers within the spiral, this program creates a
# spiral of dimension n (or n + 1 if n is even) and returns the sum of the adjacent numbers to a given number.

#  Student Name: Nicholas Webb

#  Student UT EID: nw6887

#  Partner Name: EJ Porras

#  Partner UT EID: ejp2488

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 1/29/2022

#  Date Last Modified: 1/31/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    if n % 2 == 0:
        n = n + 1

    x = n // 2  # spiral starting positions
    y = n // 2

    filler = 1  # This is the number we're going to start with!

    p1 = []  # this initializes the 2-d array
    for i in range(n):
        p2 = []
        for j in range(n):
            p2.append(0)
        p1.append(p2)

    p1[x][y] = filler  # Fill the first num in the center
    filler += 1  # We increment this number as we traverse the spiral

    for i in range(1, n):
        if i % 2 != 0:
            for j in range(i):  # since the spiral expands outward, we go by the increasing range of i
                y += 1
                p1[x][y] = filler
                filler += 1
            for j in range(i):
                x += 1
                p1[x][y] = filler
                filler += 1
        else:
            for j in range(i):
                y -= 1
                p1[x][y] = filler
                filler += 1
            for j in range(i):
                x -= 1
                p1[x][y] = filler
                filler += 1
    for i in range(1, n):
        p1[0][i] = p1[0][0] + i

    # return p1
    return p1


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    total_list = []

    x = 0
    y = 0

    # checks if input number is contained in spiral
    if n < 1 or n > len(spiral) ** 2:
        return 0

    # this sets location of n
    for i in range(len(spiral)):
        for j in range(len(spiral[0])):
            if spiral[i][j] == n:
                x = i
                y = j

    # given number is in the corner
    if (x == 0 and y == 0) or (x == 0 and y == len(spiral) - 1) or (x == len(spiral) - 1 and y == 0) or (
            x == len(spiral) - 1 and y == len(spiral) - 1):
        if x == 0 and y == 0:
            total_list.append(spiral[0][1])
            total_list.append(spiral[1][0])
            total_list.append(spiral[1][1])
        elif x == 0 and y == len(spiral) - 1:
            total_list.append(spiral[0][len(spiral) - 2])
            total_list.append(spiral[1][len(spiral) - 2])
            total_list.append(spiral[1][len(spiral) - 1])
        elif x == len(spiral) - 1 and y == 0:
            total_list.append(spiral[len(spiral) - 2][0])
            total_list.append(spiral[len(spiral) - 2][1])
            total_list.append(spiral[len(spiral) - 1][1])
        else:
            total_list.append(spiral[len(spiral) - 2][len(spiral) - 2])
            total_list.append(spiral[len(spiral) - 1][len(spiral) - 2])
            total_list.append(spiral[len(spiral) - 2][len(spiral) - 1])
    # given number is an edge piece
    elif (x == 0 and (0 < y < len(spiral) - 1)) or (x == len(spiral) - 1 and (0 < y < len(spiral) - 1)) or ((0 < x < len(spiral) - 1) and y == 0) or ((0 < x < len(spiral) - 1) and y == len(spiral) - 1):
        if x == 0 and (0 < y < len(spiral) - 1):
            for i in range(2):
                for j in range(y - 1, y + 2):
                    if spiral[i][j] != n:
                        total_list.append(spiral[i][j])
                    else:
                        continue
        elif x == len(spiral) - 1 and (0 < y < len(spiral) - 1):
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 2):
                    if spiral[i][j] != n:
                        total_list.append(spiral[i][j])
                    else:
                        continue
        elif (0 < x < len(spiral) - 1) and y == 0:
            for i in range(x - 1, x + 2):
                for j in range(2):
                    if spiral[i][j] == n:
                        continue
                    else:
                        total_list.append(spiral[i][j])
        else:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if spiral[i][j] == n:
                        continue
                    else:
                        total_list.append(spiral[i][j])
    # given number is in the middle of the spiral
    else:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if spiral[i][j] == n:
                    continue
                else:
                    total_list.append(spiral[i][j])

    total = sum(total_list)
    return total


def main():

    # read the input file
    input_file = open("spiral.in", "r")
    dimension = input_file.readline()

    # create the spiral
    spiral = create_spiral(int(dimension))

    line = input_file.readline()

    while line:
        # add the adjacent numbers
        temp_total = sum_adjacent_numbers(spiral, int(line))

        # print the result
        print(temp_total)
        line = input_file.readline()

    # print the result
    input_file.close()
    print()


if __name__ == "__main__":
    main()
