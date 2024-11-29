with open(r'input\prob1_inp.txt', 'r') as file:
    lines = file.readlines()

def calc():
        numbers = 0
        digits = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        for line in lines:
            temp = []
            for i, c in enumerate(line):
                if c.isdigit():
                    temp.append(c)
                for num, val in digits.items():
                     if line[i:].startswith(val):
                          temp.append(str(num))    
                    
            num = temp[0] + temp[-1]
            numbers = numbers + int(num)
        
        print(numbers)
   

if __name__ == "__main__":
    calc()