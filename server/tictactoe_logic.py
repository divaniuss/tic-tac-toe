class Field:
    def __init__(self):
        self.pole = [['','',''],
                     ['','',''],
                     ['','','']]
        self.count_x = 0
        self.count_y = 0
        self.is_win = 0 # - false 1 - True
        self.count_tie = 0

    def step(self, raw, col, req):
        if 3 > raw >= 0:
            if 3 > col >= 0:
                if self.pole[raw][col] == "":
                    self.pole[raw][col] = req
                    self.print_field()
                    self.count_tie += 1
                    return True
                else:
                    return False

    def IsTie(self):
        if self.count_tie < 9:
            return False
        else:
            return True

    def print_field(self):
        for row in self.pole:
            print(f"  |{row}|,")
        print("\n")

    def OutField(self):
        arr_out = ''
        for row in self.pole:
            arr_out += f"  {row}\n"
        return arr_out

    def CheckIsPeremoga(self):
        self.CheckCols()
        self.CheckRows()
        self.CheckDiagonal()
        self.CheckDiagonalReverse()

        if self.is_win == 0:
            return False
        else:
            return True




    def CheckRows(self):
        for row in self.pole:
            self.count_x = 0
            self.count_y = 0
            for elem in row:
                if elem == "x":
                    self.count_x += 1
                    if self.count_x == 3:
                        self.is_win = 1
                elif elem == "o":
                    self.count_y +=1
                    if self.count_y == 3:
                        self.is_win = 1
                else:
                    # print("net row ")
                    break


    def CheckCols(self):
        for columnIndex in range(0, len(self.pole)):
            self.count_x = 0
            self.count_y = 0
            for rowIndex in range(0, len(self.pole)):
                elem = self.pole[rowIndex][columnIndex]
                if elem == "x":
                    self.count_x += 1
                    if self.count_x == 3:
                        self.is_win = 1
                elif elem == "o":
                    self.count_y  += 1
                    if self.count_y  == 3:
                        self.is_win = 1
                else:
                    # print("net col")
                    break

    def CheckDiagonal(self):
        self.count_x = 0
        self.count_y = 0
        for Index in range(0, len(self.pole)):

            elem = self.pole[Index][Index]
            if elem == "x":
                self.count_x += 1
                if self.count_x == 3:
                    self.is_win = 1
                    # print("da diag")
            elif elem == "o":
                self.count_y += 1
                if self.count_y == 3:
                    self.is_win = 1
            else:
                # print("net diag")
                break





    def CheckDiagonalReverse(self):
        self.count_x = 0
        self.count_y = 0
        for Index in range(0, len(self.pole)):
            elem = self.pole[Index * -1][Index * -1]
            if elem == "x":
                self.count_x += 1
                if self.count_x == 3:
                    self.is_win = 1
            elif elem == "o":
                self.count_y += 1
                if self.count_y == 3:
                    self.is_win = 1
            else:
                # print("net diag rev")
                break



f = Field()

# f.CheckRows()
# print("\n")
# f.CheckCols()
# print("\n")
# f.CheckDiagonal()
# f.CheckDiagonalReverse()
# print(f.OutField())