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
        while disk_arr[-1] == -1:disk_arr.pop()
        if len(disk_arr) <= iter:break
        disk_arr[iter] = disk_arr.pop()
              
    return disk_arr


def create_updated_disk(disk):
    files = {}
    blanks = []

    fid = 0
    pos = 0
    for i, ch in enumerate(disk):
        x = int(ch)
        if i % 2 == 0:
            if x == 0:
                raise ValueError("unexpected x=0 for file")
            files[fid] = (pos, x)
            fid += 1
        else:
            if x != 0:
                blanks.append((pos, x))

        pos += x

    while fid > 0:
        fid -= 1
        pos, size = files[fid]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break 
    
    return files




def part_one():
    new_disk = create_disk(lines)
    checksum = 0
    for i in range(len(new_disk)):
        if new_disk[i] != -1:
            checksum += i * new_disk[i]
        else:
            continue

    print(checksum)

def part_two():
    new_disk = create_updated_disk(lines)

    checksum = 0
    for id, (pos, size) in new_disk.items():
        for x in range(pos, pos+size):
            checksum += id * x
    
    print(checksum)

if __name__ == "__main__":
    part_one()
    part_two()