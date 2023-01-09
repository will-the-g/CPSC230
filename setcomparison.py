import time
import random

L = []
S = set({})
total = 0
for i in range(100000):
    L.append(random.randint(1,500000))
    S.add(random.randint(1,500000))
start = time.time()
for i in range(20000):
    num = random.randint(1, 500000)
    if num in L or num in S:
        total += 1
stop = time.time()
elapsed_time = stop - start
print(f"{total} numbers were found in the collections in {elapsed_time} seconds")