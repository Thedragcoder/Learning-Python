successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("sorry we were unable to send the message after three attempts")
