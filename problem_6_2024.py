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



def part_one():
    directions = ['^', '>', 'v', '<']
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total_moves = count_moves(directions, moves, lines)
    print(total_moves)





if __name__ == "__main__":
    part_one()