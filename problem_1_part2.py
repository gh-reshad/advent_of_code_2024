with open(r'input\inp_1_2024.txt', 'r') as file:
    lines = file.readlines()

def similarity_score():
    l1 = []
    l2 = []
    for line in lines:
        line = line.replace('\n', '')
        numbers = line.split("   ")
        l1.append(int(numbers[0]))
        l2.append(int(numbers[1]))

    print(sum([num*l2.count(num) for num in l1]))

 



if __name__ == "__main__":
    similarity_score()