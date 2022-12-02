import time
start_time = time.time()

with open("./01/1.txt", "r") as data:
    results = [sum(map(int, line.split("\n"))) for line in data.read().split("\n\n")]
    print(max(results))

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))