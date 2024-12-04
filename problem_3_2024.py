import re

with open(r'input\inp_3_2024.txt', 'r') as file:
    lines = file.readlines()


def sum_of_multiplications():
    multi = 0
    for line in lines:
        pattern = r'mul\((\d+),(\d+)\)'

        matches = re.findall(pattern, line)

        for match in matches:
            print(match)
            x,y = int(match[0]), int(match[1])
            multi += x * y

    print(multi)


if __name__ == "__main__":
    sum_of_multiplications()