# Write your solution here
def row_sums(matrix: list):
    for item in matrix:
        suma = 0
        for element in item:
            suma += element
        item.append(suma)


my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)
