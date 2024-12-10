from itertools import repeat

with open(r'input\inp_9_2024.txt', 'r') as file:
    lines = file.read()


def create_disk(disk):
    disk_arr = []
    fid = 0
    for i, ch in enumerate(disk):
        if i % 2 == 0:
            disk_arr.extend(repeat(fid, int(ch)))
            fid += 1
        else:
            disk_arr.extend(repeat(-1, int(ch)))

    iter = 0
    #print(disk_arr)
    free_space = [i for i, x in enumerate(disk_arr) if x == -1]

    for iter in free_space:
        while disk_arr[-1] == -1: disk_arr.pop()
        if len(disk_arr) <= iter:break
        disk_arr[iter] = disk_arr.pop()
    
    
    return disk_arr

def part_one():
    new_disk = create_disk(lines)
    #print(new_disk)
    checksum = 0
    for i in range(len(new_disk)):
        if new_disk[i] != -1:
            checksum += i * new_disk[i]
        else:
            continue

    print(checksum)



if __name__ == "__main__":
    part_one()