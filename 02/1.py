import time
start_time = time.time()

def convert(c):
    val = ord(c)-64
    if val > 3:
        val = val - 23
    return val

with open("./02/1.txt", "r") as data:
    lines = data.read().split("\n")
    games = [list(map(convert, line.split(" "))) for line in lines]
    results = [6 + me if elf - me in [-1,2] else me if elf - me in [-2,1] else 3 + me for elf, me in games]
    print(sum(results))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
