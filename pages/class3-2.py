# Arithmetic Assignment Operators

a = 10
b = 3
a += b  # equals a=a+b
print("a+=b 的結果是:", a)  # 13

a = 10
b = 3
a -= b  # equals a-a-b
print("a-=b 的結果是:", a)  # 7

a = 10
b = 3
a *= b  # equals a=a*b
print("a*=b 的結果是:", a)  # 30

a = 10
b = 3
a /= b  # equals a=a/b
print("a/=b 的結果是:", a)  # 3.3333
a = 10
b = 3
a //= b  # equals a=a//b
print("a//=b 的結果是:", a)  # 3
a = 10
b = 3
a **= b  # equals a=a**b
print("a**=b 的結果是:", a)  # 1000

a = 10
b = 3
a %= b  # equals a=a%b
print("a%=b 的結果是:", a)  # 1

# Comparison Operators
a = 10
b = 3
print("a == b 的結果是:", a == b)  # False
print("a != b 的結果是:", a != b)  # True
print("a > b 的結果是:", a > b)  # True
print("a < b 的結果是:", a < b)  # False
print("a >= b 的結果是:", a >= b)  # True
print("a <= b 的結果是:", a <= b)  # False
# Logical Operators
a = True
b = False

# while loop break
i = 1
while i <= 6:
    if i == 3:
        break
    print("i=", i)
    i += 1

    print("-" * 30)
    # for loop break
for i in range(1, 6):
    if i == 3:
        break
    print("i=", i)
