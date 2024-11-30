with open(r'input\prob2_inp.txt', 'r') as file:
    lines = file.readlines()

def check_validity():
    max_cubes = {'red':12, 'green':13, 'blue': 14}
    sum_possible_games = 0
    for line in lines:
        line = line.replace('\n', '')
        not_possible = False
        game_id, sequences = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        sequences = sequences.split("; ")
        for sequence in sequences:
            draws = sequence.split(', ')
            for cubes in draws:
                num, color = cubes.split(" ")
                if int(num) > max_cubes[color]:
                    not_possible = True
                    break
            if not_possible:
                    break
        if not not_possible:   
            sum_possible_games += game_id 


    print(sum_possible_games)


if __name__ == "__main__":
    check_validity()