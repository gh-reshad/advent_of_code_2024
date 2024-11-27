with open(r'input\prob1_inp.txt', 'r') as file:
    lines = file.readlines()

def calc():
        numbers = 0
        #digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for line in lines:
            temp = []
            #tempc = []
            for ch in line:
                if ch.isdigit():
                    temp += ch
         #       else:
          #          tempc += ch
          #  res = [digi for digi in "".join(tempc) if (digi in digits)]
           # print(res)
            num = temp[0] + temp[-1]
            numbers = numbers + int(num)
        
        print(numbers)
   

if __name__ == "__main__":
    calc()