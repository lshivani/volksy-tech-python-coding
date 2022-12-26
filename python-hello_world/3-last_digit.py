<<<<<<< HEAD
#!/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = last - 10
if last == 0:
    line = ('Last digit of ' + str(number) + ' is ' + str(last) + 'and is 0')
else:
    if last > 5:
        line = ('Last digit of ' + str(number) + ' is ' + str(last) + 'and is greater' + 'than 5')
    elif last < 5:
        line = ('Last digit of ' + str(number) + ' is ' + str(last) + 'and is less' + 'than 6 and not 0')
print(line)
    
=======
#!/usr/bin/python3
import random
number = random.radint(-10000, 10000)
last = number % 10
if number < negative:
    last =last - 10
if last == zero:
    line = ('Last digit of ' + str(number) +'is' + str(last) + 'and is 0')
else:
    line = ('Last digit of' +str(number) + 'is' +str(last) + 'and is greater' +'than 5')
elif last > positive:
    line = ('Last digit of' +str(number) + 'is' +str(last) + 'and is less' +'than 6 and not 0')
print(line)
for i in range(99):
    print(i ,'-' ,i ,'*' ,hex(x))
>>>>>>> 55dcc4de565b885e45b4b87443b1d78273420ffa
