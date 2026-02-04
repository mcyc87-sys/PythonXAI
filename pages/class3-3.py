# random practice

import random

# randrange 1 parameter
R1 = random.randrange(6)  # 0-5 whole number
print("R1 =", R1)

# randrange 2 parameters
R2 = random.randrange(1, 11)  # 1-10 whole number
print("R2 =", R2)

# randrange 3 parameters
R3 = random.randrange(1, 11, 2)  # 1-10 odd whole number
print("R3 =", R3)

# statistics randrange return value
num = 1000
count = [0, 0, 0, 0, 0]  # record the number of appearances of 0,1,2,3,4,5
for i in range(num):
    R = random.randrange(1, 6)
    count[R - 1] += 1
for i in range(1, 6):
    print(f"{i}出現次數: {count[i-1]})")
    
print("_"*30)

# randrange 2 parameters
R4 = random.randrange(1, 5)  # 1-10 whole number
print("R4", R4)

#end
num = 1000
count = [0, 0, 0, 0, 0]  # record the number of appearances of 0,1,2,3,4,5
for i in range(num):
    R = random.randrange(1, 5)
    count[R - 1] += 1
for i in range(1, 6):
    print(f"{i}出現次數: {count[i-1]})")
