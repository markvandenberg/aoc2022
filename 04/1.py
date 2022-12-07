import time
start_time = time.time()

with open("./04/1.txt", "r") as data:
    lines = data.read().split("\n")
    count = 0
    for line in lines:
        sections = [pair.split('-') for pair in line.split(',')]
        s1 = set(range(int(sections[0][0]),int(sections[0][1])+1))
        s2 = set(range(int(sections[1][0]),int(sections[1][1])+1))
        count += 1 if s1.issubset(s2) or s2.issubset(s1) else 0
    
    print(count)

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
