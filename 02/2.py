import time
start_time = time.time()

def convert(c):
    val = ord(c)-64
    if val > 3:
        val = (val - 24) * 3
    return val

with open("./02/2.txt", "r") as data:
    lines = data.read().split("\n")
    games = [list(map(convert, line.split(" "))) for line in lines]
    results = [3 + result if elf + result in [1,6,8] else 1 + result if elf + result in [2,4,9] else 2 + result for elf, result in games]
    print(sum(results))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
