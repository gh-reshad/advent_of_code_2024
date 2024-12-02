with open(r'input\inp_2_2024.txt', 'r') as file:
    lines = file.readlines()

def is_safe():
    num_safe = 0
    for line in lines:
        adjacents = []
        line = line.replace('\n', '')
        levels = line.split(' ')
        for l in range(len(levels[:-1])):
            adjacents.append(int(levels[l+1]) - int(levels[l]))
        
        if all(a > 0 for a in adjacents) or all(a < 0 for a in adjacents):
            if all(abs(a) in range(1,4) for a in adjacents):
                num_safe += 1



    print(num_safe)

if __name__ == "__main__":
    is_safe()