from functools import cache

with open(r'input\inp_11_2024.txt', 'r') as file:
    lines = file.read()





def part_one():
    stones = [int(x) for x in lines.split(' ')]

    for _ in range(25):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
                continue
            string = str(s)   

            if len(string) % 2 == 0:
                new_stones.append(int(string[:len(string) // 2]))
                new_stones.append(int(string[len(string) // 2:]))
            else:
                new_stones.append(s * 2024)

        stones = new_stones
        

    print(len(stones))


def part_two():
    stones = [int(x) for x in lines.split(' ')]

    @cache
    def count(stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return count(1, steps - 1)

        string = str(stone)
        length = len(string)

        if length % 2 == 0:
            return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps -1)
        
        else:
            return count(stone * 2024, steps - 1)

    print(sum(count(stone, 75) for stone in stones))







if __name__ == "__main__":
    part_one()
    part_two()