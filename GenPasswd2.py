from random import choice
import string
import time

def GenPasswd2(length=8, chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join([choice(chars) for i in range(length)])


#for i in range(10):
#    print(GenPasswd2(120))
while True:
    time.sleep(.3)
    print(GenPasswd2(120))

