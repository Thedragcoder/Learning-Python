# python stores this data as a dictionary which is a data structure in programming
def information(**user):
    print(user)
    print(user["age"])
    print(user['name'])
    print(user['id'])


information(id=1, name='stash', age=33)
# we can access the value of each arguments using square brackets
