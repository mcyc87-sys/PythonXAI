# 這是單行註解
"""
#這是單行註解
"""

n1 = 3  # 這是整數
n2 = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196  # 這是浮點數
b1 = True  # 這是布林值
s1 = "hello"  # 這是字串

print(3)
print(
    3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196
)
print(True)
print("hello")

a = 10
b = 20
print(a + b)  # plus
print(a - b)  # minus
print(a * b)  # multiplication
print(a % b)  # division
print(a**2)  # complete division
print(a // b)  # remainder
print(a / b)  # square

print("hello" + "world")  # String
print("hello" + " " + "world")  # String
print("hello" * 3)  # String Repeat
print("hello" + "world" * 3)  # String Connection and repetation
name = "Python"
age = 31
new_str = f"My name is (Python), and I am (31) years old."  # f-string
print(new_str)

print(len(""))  # 0
print(len("hi"))  # 2
print(len("hello"))  # 5
print(type(10))
print(type(3.14))
print(type(True))
print(type("hello"))
print(int(True))  # 1
print(int(False))  # 0
print(int("1234"))  # 1234
print(float("3.14"))  # 3.14
print(float(10))  # 10.0

print(bool(1))  # True
print(bool(0))  # False
print(bool(-2))  # True
print(bool(""))  # False
print(bool("Hello"))  # True

print(str(1234))  # "1234"
print(str(3.14))  # "3.14"
print(str(True))  # "True"
print(str(False))  # "False"
print(str(True))  # "True"

# in1 = input("your name:")
# print("hello," + in1)
# print(type(in1))  # str

in2 = int(input("your age:"))
print(in2**2 * 3.14)

# Calculate Circle Are
# a
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius**2
print("The area of the circle is:", area)
