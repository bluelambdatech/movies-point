

# create a function to calculate factorial and returns the result

# 10! = 10 * 9 * 8 * 7 ...... * 1
# 3! = 3 * 2 * 1
# 100!

# 0! = 1
# 1! = 1
# 10! = 10 * 9!
# 9! = 9 * 8!
# 8! = 8 * 7!

# Recursive Function


def factorial(num):
    match num:
        case 1:
            return 1
        case 0:
            return 1
    return num * factorial(num - 1)


# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)

# 5 * 4 * 3 * 2 * 1
#
# num = input("Please, enter the value: ")
# print(factorial(int(num)))