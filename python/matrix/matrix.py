class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for row in matrix_string.split("\n"):
            self.matrix.append([int(num) for num in row.split(" ")])

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = []
        for row in self.matrix:
            col.append(row[index - 1])
        return col
