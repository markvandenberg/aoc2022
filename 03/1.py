import time
start_time = time.time()

def convert(c):
    val = ord(c)-38
    if val > 52:
        val = val - 58
    return int(val)

with open("./03/1.txt", "r") as data:
    lines = data.read().split("\n")

    prios = [list(map(convert, set(line[:len(line)//2]).intersection(line[len(line)//2:])))[0] for line in lines]
    print(sum(prios))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
