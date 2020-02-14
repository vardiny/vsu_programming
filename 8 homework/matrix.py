class Matrix:
    matrix = 0

    def __init__(self):
        self.column = 0
        self.line = 0
        self.matrix = []

    def key_entry(self):
        self.column = int(input("Введите кол столбцов "))
        self.line = int(input("Введите кол строк "))
        for a in range(self.line):
            number = []
            for b in range(self.column):
                number.append(int(input()))
            self.matrix.append(number)
    
    def add(self):
        for x in self.matrix:
            print(*x)
        
    def __str__(self):
        print('Matrix:') 
        for x in self.matrix:
            x = ' '.join(str(e) for e in x)
            print(x)

matrix = Matrix()
matrix.key_entry()
#matrix.add()
matrix.__str__()
