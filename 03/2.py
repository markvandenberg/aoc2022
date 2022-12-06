import time
start_time = time.time()

def convert(c):
    val = ord(c)-38
    if val > 52:
        val = val - 58
    return int(val)

with open("./03/1.txt", "r") as data:
    lines = data.read().split("\n")
    i = iter(lines)
    groups = list(zip(i, i, i))
    
    prios = [list(map(convert, set(group[0]).intersection(set(group[1]),set(group[2]))))[0] for group in groups]
    print(sum(prios))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
