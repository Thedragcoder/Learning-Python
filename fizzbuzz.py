from operator import mod


def fizzBuzz(usersInput):
    if (usersInput % 3 == 0) and (usersInput % 5 == 0):
        return 'fizz buzz'
    elif usersInput % 3 == 0:
        return 'fizz'
    elif usersInput % 5 == 0:
        return 'buzz'
    else:
        return usersInput


print(fizzBuzz(26))
