# simple func
def hello():
    print("Hello")


hello()
hello()
hello()

print("_" * 30)


# func with parameters
def greet(name):
    print(f"Hello {name}!")


greet("Mike")
greet("Michael")

print("_" * 30)


# func with return value
def two_num_min(a, b):
    if a < b:
        return a
    else:
        return b


print(two_num_min(3, 5))
print(two_num_min(10, 7))

print("_" * 30)


def three_num_min(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c


print(three_num_min(1, 5, 2))
print(three_num_min(10, 7, 15))
print(three_num_min(8, 12, 6))


def calculate_circle_area(radius, pi=3.14):
    return pi * radius**2


print(calculate_circle_area(10))  # 314.0
print(calculate_circle_area(10, 3.14159265358979323846))  # 314.159265358979323846


def print_parameters(a, b, c=0, d=0):  # a: 1, b: 2, c: 0, d: 0
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")


print_parameters(1, 2)  # a: 1, b: 2, c: 0, d: 0
print_parameters(1, 2, 3)  # a: 1, b: 2, c: 3, d: 0
print_parameters(1, 2, 3, 4)  # a: 1, b: 2, c: 3, d: 4
print_parameters(1, 2, d=4)  # a: 1, b: 2, c: 0, d: 4
