# matrix is a 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# call items from matrix by printing their matrix coordinate
print(matrix[0][0])
# will return item 1 on list 1
print(matrix[0][1])
# will return item 2 on list 1
print(matrix[2][2])
# will return item 3 on list 3

matrix[0][2] = 30
# will update value in list one item 3 from 3 to 30
print(matrix[0][2])
# returns new value for list 1 item 3

for row in matrix:
    for item in row:
        print(item)


