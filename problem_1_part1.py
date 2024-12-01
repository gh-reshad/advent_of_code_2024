with open(r'input\inp_1_2024.txt', 'r') as file:
    lines = file.readlines()

def tot_distance():
    l1 = []
    l2 = []
    for line in lines:
        line = line.replace('\n', '')
        numbers = line.split("   ")
        l1.append(int(numbers[0]))
        l2.append(int(numbers[1]))

    print(sum([abs(num1 - num2) for num1, num2 in zip(sorted(l1),sorted(l2))]))




if __name__ == "__main__":
    tot_distance()