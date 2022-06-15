# in python we have very powerful data structure called dictionary which is collction of key value pairs
# real world example is phone book contactname -> number
contact = {'john': 77232323, 'joseph': 88773434, 'celiene': 8877343}
# the other way to create a dictionary is
addresses = dict(phoebe='east street', joshua='north york')
print(addresses['phoebe'])
print(contact['john'])
addresses['ron'] = 'brampton'
print(addresses)
print(addresses.get('joshua'))
if 'jubin' in contact:
    print('hello jubin ')
addresses.get('jubin', 0)
# to delete
del (addresses['ron'])
print(addresses)
