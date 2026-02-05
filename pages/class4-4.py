# global variable and local variable

length = 5


def calculate_square_area1():
    area = length * length  # local variable
    print(f"The area of the square is", area)


calculate_square_area1()

print("_" * 30)

length = 5  # global variable


def calculate_square_area2():
    area = length * length  # local variable
    print(f"The area of the square is", area)


length = 10  # global variable
calculate_square_area2()

# print("_" * 30)

# length = 5  # global variable


# def calculate_square_area3():
#   area = length * length  # local variable


# length = 10  # global variable
# calculate_square_area3()
# print("The area of the square is", area)

print("_" * 30)

length = 5  # global variable
area = 3.14 * 10**2  # global variable


def calculate_square_area4():
    area = length * length


calculate_square_area4()
print("The area of the square is", area)

# print("_" * 30)

# length = 5  # global variable
# area = 3.14 * 10**2  # global variable


# def calculate_square_area5():
#     print("The area of the square is", area)
#     area = length * length
#     print("The area of the square is", area)


# calculate_square_area5()

print("_" * 30)

length = 5  # global variable
area = 3.14 * 10**2  # global variable


def calculate_square_area6():
    area = length * length
    return area


area = calculate_square_area6()
print("The area of the square is", area)

print("_" * 30)

length = 5  # global variable
area = 3.14 * 10**2  # global variable


def calculate_square_area7():
    global area
    area = length * length


calculate_square_area7()
print("The area of the square is", area)
