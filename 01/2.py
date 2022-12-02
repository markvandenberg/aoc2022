import time
start_time = time.time()

with open("./01/2.txt", "r") as data:
    results = [sum(map(int, line.split("\n"))) for line in data.read().split("\n\n")]
    print(sum(sorted(results, reverse=True)[:3]))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))