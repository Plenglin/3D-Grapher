class Matrix():

    def __init__(self, values):
        self.values = values

    def getWidth(self):
        return len(self.values[0])

    def getHeight(self):
        return len(self.values)

    def getRow(self, row):
        return self.values[row]

    def getCol(self, col):
        return self.transpose().values[col]

    def transpose(self):
        return Matrix(list(zip(*self.values)))

    def __getitem__(self, key):
        x, y = key
        try:
            return self.values[y][x]
        except:
            raise Exception(x, y, self.values)

    def __setitem__(self, key, val):
        x, y = key
        self.values[y][x] = val

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix([[x + y for x, y in zip(a, b)] for a, b in zip(self.values, other.values)])
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[c + other for c in r] for r in self.values])

    def __sub__(self, other):
        if isinstance(other, Matrix):
            return Matrix([[x - y for x, y in zip(a, b)] for a, b in zip(self.values, other.values)])
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[c - other for c in r] for r in self.values])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            assert self.getWidth() == other.getHeight(), '%s and %s cannot be multiplied!' % (self, other)
            new = zero(self.getHeight(), other.getWidth())
            for i in range(0, new.getWidth()):
                for j in range(0, new.getHeight()):
                    sums = []
                    for x in range(0, self.getWidth()):
                        sums.append(self[x, i] * other[j, x])
                    new[i, j] = sum(sums)
            return new.transpose()
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[c * other for c in r] for r in self.values])

    def __repr__(self):
        return 'Matrix' + str(self.values)

def zero(width, height):
    return Matrix([[0] * width for _ in range(0, height)])

def columnvec(*vals):
    m = [[v] for v in vals]
    return Matrix(m)

def identity(width):
    m = zero(width, width)
    for i in range(0, width):
        m[i, i] = 1
    return m

if __name__ == '__main__':
    print(Matrix([[1,2],[3,4]])*Matrix([[7],[8]]))
