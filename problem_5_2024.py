with open(r'input\inp_5_2024.txt', 'r') as file:
    lines = file.read()


def check_correct(nr, inp, rule):
    flag = all(item in rule for item in nr)
    if flag: 
        mid_index = len(inp) // 2 
        if len(inp) % 2 == 0: 
            return int(inp[mid_index - 1]) 
        else: 
            return int(inp[mid_index])
    return 0

def create_rule(l, r):
    new_rule = []
    middle_num = 0
    input = l.split(',')
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            new_rule.append(input[i] + '|' + input[j])  
    middle_num += check_correct(new_rule, input, r)
    return middle_num
             
        
def part_one():
    rules, up_list = lines.strip().split('\n\n')

    rules = rules.split('\n')
    up_list = up_list.split('\n')
    total_middle = 0
    for list in up_list:
        total_middle += create_rule(list, rules)

    print(total_middle)    

if __name__ == "__main__":
    part_one()