with open(r'input\inp_4_2024.txt', 'r') as file:
    lines = file.read().splitlines()

def build_new_grid(lines, n):
    new_grid = []
    len_line = len(lines[0]) + (n * 2)
    new_grid.extend(["." * len_line for i in range(n)])
    for line in lines:
        new_grid.append("." * n + line + "." * n)
    new_grid.extend(["." * len_line for i in range(n)])

    return new_grid

def find_xmas(row, col, input):
    string = []
    #forward
    if col+4 < len(input[0]):
        string.append("".join([input[row][c] for c in range(col, col+4)]))

    #backward
    if col-4 >= 0:
        string.append("".join([input[row][c] for c in range(col, col-4, -1)]))
    
    #downward
    if row+4 < len(input):
     string.append("".join([input[r][col] for r in range(row, row+4)]))

    #upward
    if row-4 >= 0:
     string.append("".join([input[r][col] for r in range(row, row-4, -1)]))

    #diag1
    if row+4 < len(input) and col+4 < len(input[0]):
     string.append("".join([input[r][c] for r,c in zip(range(row, row+4), range(col, col+4))]))

    #diag2 
    if row+4 < len(input) and col-4 >= 0:
     string.append("".join([input[r][c] for r,c in zip(range(row, row+4), range(col, col-4, -1))]))

    #diag3
    if row-4 >= 0 and col+4 < len(input[0]):
     string.append("".join([input[r][c] for r,c in zip(range(row, row-4, -1), range(col, col+4))]))

    #diag4
    if row-4 >= 0 and col-4 >= 0:
     string.append("".join([input[r][c] for r,c in zip(range(row, row-4, -1), range(col, col-4, -1))]))

    
    return string.count("XMAS")

def find_mas(row, col, input):
    string = []


    #diag1
    
    string.append("".join([input[r][c] for r,c in zip(range(row -1, row+2), range(col-1, col+2))]))

    #diag2 
    
    string.append("".join([input[r][c] for r,c in zip(range(row-1, row+2), range(col+1, col-2, -1))]))

 

    if string.count("MAS") + string.count("SAM") == 2:
       return 1
    else:
       return 0
   

def part_one():
    count_xmas = 0
    new_grid = build_new_grid(lines, 3)

    for r, line in enumerate(new_grid):
        for c, ch in enumerate(line):
            if ch == 'X':
                count_xmas += find_xmas(r, c, new_grid)  

    print(count_xmas)  

def part_two():
    count_mas = 0
    for r, line in enumerate(lines[1:-1],1):
        for c, ch in enumerate(line[1:-1],1):
            if ch == 'A':
                count_mas += find_mas(r, c, lines)  

    print(count_mas) 



if __name__ == "__main__":
    part_one()
    part_two()