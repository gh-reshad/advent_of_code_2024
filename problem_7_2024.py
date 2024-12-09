with open(r'input\inp_7_2024.txt', 'r') as file:
    lines = file.read()



def part_one():
    disk_dic = {}
    i = 0
    while i < len(lines):
        if i+1 > len(lines):
            break
        else:
            disk_dic[lines[i]] = lines[i+1]
            i = i+2


    
    print(disk_dic)




if __name__ == "__main__":
    part_one()