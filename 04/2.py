import time
import numpy as np
from functools import reduce
from collections import Counter

start_time = time.time()

with open("./04/1.txt", "r") as data:
    lines = data.read().split("\n")
    counter = 0
    for line in lines:
        sections = [pair.split('-') for pair in line.split(',')]
        s1 = set(range(int(sections[0][0]),int(sections[0][1])+1))
        s2 = set(range(int(sections[1][0]),int(sections[1][1])+1))
        if len(s1.intersection(s2)) > 0 or len(s2.intersection(s1)) > 0:
            counter += 1
    
    print(counter)

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
