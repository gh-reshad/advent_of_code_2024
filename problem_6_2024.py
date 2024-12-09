with open(r'input\inp_6_2024.txt', 'r') as file:
    lines = file.read().splitlines()

def count_moves(dir, move, map):
    flag = False
    for r, line in enumerate(map):
        if flag:
            break
        else:
            for c, ch in enumerate(line):
                if ch in dir:
                    gaurd_pos = (r, c)
                    gaurd_dir = dir.index(ch)
                    flag = True
                    break
    
    
    visited_pos = set()
    rows, cols = (len(map), len(map[0]))
    while 0 <= gaurd_pos[0] < rows and 0 <= gaurd_pos[1] < cols:
       visited_pos.add(gaurd_pos)
       next_pos = (gaurd_pos[0] + move[gaurd_dir][0], gaurd_pos[1] + move[gaurd_dir][1])

       if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and map[next_pos[0]][next_pos[1]] == "#":
            gaurd_dir = (gaurd_dir + 1) % 4
       else:
           gaurd_pos = next_pos

        
    return len(visited_pos)

def get_start_pos(map, dir):
    for r, line in enumerate(map):
        for c, ch in enumerate(line):
            if ch in dir:
                return (r,c)
                 
                

def loops(inp, sr, sc):
    dr = -1
    dc = 0
    rows = len(inp)
    cols = len(inp[0])

    seen = set()

    while True:
        seen.add((sr, sc, dr, dc))
        if sr + dr < 0 or sr + dr >= rows or sc + dc < 0 or sc + dc >= cols:
            return False
        if inp[sr + dr][sc + dc] == '#':
            dc,dr = -dr, dc
        else:
            sr += dr
            sc += dc
        if (sr, sc, dr, dc) in seen:
            return True




def part_one():
    directions = ['^', '>', 'v', '<']
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total_moves = count_moves(directions, moves, lines)
    print(total_moves)
    

def part_two():
    directions = ['^', '>', 'v', '<']
    #moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid = list(map(list, lines))
    px, py = get_start_pos(grid, directions)
    count = 0
    for cr in range(len(grid)):
        for cc in range(len(grid[0])):
            if grid[cr][cc] != '.': 
                continue
            grid[cr][cc] = "#"
            if loops(grid, px, py):
                count += 1

            grid[cr][cc] = "."
    
    print(count)
                

# def part_two():
#     grid = list(map(list, lines))
#     rows = len(grid)
#     cols = len(grid[0])

#     for r in range(rows):   
#         for c in range(cols):
#             if grid[r][c] == "^":
#                 break
#         else:
#             continue
#         break

#     def loops(grid, r, c):
#         dr = -1
#         dc = 0

#         seen = set()

#         while True:
#             seen.add((r, c, dr, dc))
#             if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: return False
#             if grid[r + dr][c + dc] == "#":
#                 dc, dr = -dr, dc
#             else:
#                 r += dr
#                 c += dc
#             if (r, c, dr, dc) in seen:
#                 return True

#     count = 0

#     for cr in range(rows):
#         for cc in range(cols):
#             if grid[cr][cc] != ".": continue
#             grid[cr][cc] = "#"
#             if loops(grid, r, c):
#                 count += 1
#             grid[cr][cc] = "."

#     print(count)



if __name__ == "__main__":
    part_one()
    part_two()