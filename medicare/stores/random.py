import random

arr = ""
r = 0
for _ in range(1, 11):
    r = random.randint(0, 9)
    print(r)
    arr += str(r)
print(r)
print(int(arr))
