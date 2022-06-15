# in programming languages we have a buit in data structure called stacks which resembles a stack of items
# for an example you have a stack of books the last one you put on top is the first one you can remove it is called lifo
# in web browsers stack is used to keep the record of the sites so when the user presses the back button the browser has to browse
# the site before the current site
browsingSession = []
originalBrowsingSession = browsingSession
browsingSession.append('google.com')
browsingSession.append('instagram.com')
browsingSession.append('github.com')
browsingSession.append('python.com')
print(browsingSession)
inputUser = input('do you want to go back? y/n: ')
# if there is no item in the list disable the button
if not browsingSession:
    print('disabled')
if inputUser == 'y':
    browsingSession.pop()
    print(f'redirecting to {browsingSession[-1]}')
else:
    print(f'you are currently on {originalBrowsingSession[-1]}')
