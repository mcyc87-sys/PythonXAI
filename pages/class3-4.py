import random

target = random.randint(0, 100)

min_val = 0
max_val = 100
while True:
    num = int(input(f"請輸入一個{min_val}到{max_val}之間的整數: "))
    if num < min_val or num > max_val:
        print("輸入錯誤，請重新輸入")
    elif num > target:
        print("太大了")
        max_val = num
    elif num < target:
        print("太小了")
        min_val = num
    else:
        print("恭喜你猜對了")
        break
