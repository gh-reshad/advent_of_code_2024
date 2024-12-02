import copy

with open(r'input\inp_2_2024.txt', 'r') as file:
    lines = file.readlines()

def is_safe():
    num_safe = 0
    for line in lines:
        adjacents = []
        new_adjacents = []
        line = line.replace('\n', '')
        levels = line.split(' ')
        for l in range(len(levels[:-1])):
            adjacents.append(int(levels[l+1]) - int(levels[l]))
        
        if all( 1<=a<=3 for a in adjacents) or all(-3<=a<=-1 for a in adjacents):
                num_safe += 1
            
        else:
            for i in range(len(levels)):
                new_level = copy.copy(levels)
                new_level.pop(i)
                new_adjacents = []
                for nl in range(len(new_level[:-1])):
                    new_adjacents.append(int(new_level[nl+1]) - int(new_level[nl]))
                if all( 1<=a<=3 for a in new_adjacents) or all(-3<=a<=-1 for a in new_adjacents):
                    num_safe += 1
                    break


    print(num_safe)

if __name__ == "__main__":
    is_safe()