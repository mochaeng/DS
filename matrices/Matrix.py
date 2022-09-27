class Matrix:
    def __init__(self, m, n):
        self.matrix = []
        self.n = n
        self.m = m

        self.__create()

    def __create(self):
        for i in range(self.n):
            self.matrix.append([])
            for j in range(self.m):
                self.matrix[i].append(0)

    def split_by_lines(self, num_pieces):
        size = int(self.n / num_pieces)
        lists = []
        counter = 0
        for k in range(num_pieces):
            lists.append([])
            for i in range(size):
                lists[k].append(self.matrix[counter][:])
                counter += 1
        return lists
    
    def split_by_columns(self, num_pieces):
        size = int(self.n / num_pieces)
        lists = []
        counter = 0
        for k in range(num_pieces):
            lists.append([])
            for i in range(self.m):
                # lists[k].append(self.matrix[::][i][0:2])
                lists[k].append(self.matrix[::][i][counter:counter+size])
            counter += size 
        return lists

    def __str__(self):
        matrix_str = ''
        for i in range(self.n):
            for j in range(self.m):
                matrix_str += str(self.matrix[i][j]) + ' '
            matrix_str += '\n'
        return matrix_str

def create_from_lists(lists):
    if len(lists) == 0:
        return
    m = len(lists[0])
    n = len(lists[0][0])
    matrices = []
    for list in lists:
        matrix = Matrix(n, m)
        for i in range(m):
            for j in range(n):
                matrix.matrix[i][j] = list[i][j]
        matrices.append(matrix)
    return matrices

