import re

with open(r'input\inp_3_2024.txt', 'r') as file:
    lines = file.read()

def enabled():
    new_line = ""
    for l in lines.split('do()'):
        new_line += l.split('don\'t()')[0]
    sum_of_multiplications(new_line)


def sum_of_multiplications(line):
    multi = 0
    pattern = r'mul\((\d+),(\d+)\)'

    matches = re.findall(pattern, line)

    for match in matches:
        #print(match)
        x,y = int(match[0]), int(match[1])
        multi += x * y

    print(multi)


if __name__ == "__main__":
    enabled()
    