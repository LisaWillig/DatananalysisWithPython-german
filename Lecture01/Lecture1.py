"""
My first Python script

- this is a multiline comment

"""
# My second comment

'''
This is also a multiline comment
'''
statement = 0

if statement !=False:
    print(4)

counter = 1000
count = 0
sum = 0

while count < counter:
    if count%3 ==0:
        sum = sum+count
    elif count%5 ==0:
        sum = sum+count

    count = count +1

print(sum)