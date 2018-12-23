import tempConversion

##### Aufgabe 2 ############


Temperature_Fahrenheit = [0, 30, 60, 90, 100, 120]
Temperature_Degree = [0, 0, 0, 0, 0, 0]



for idx, temp in enumerate(Temperature_Fahrenheit):
    Temperature_Degree[idx] = (temp-32) * 5/9
    if temp>95:
        print('Warning! Temperature is critical: ', temp)


for idx, temp in enumerate(Temperature_Fahrenheit):
    Temperature_Degree[idx] = tempConversion.tempConversion_FtoDeg(temp)
    tempConversion.warnTemp(temp)


Temperature_Degree=[]
Temperature_Warning=[]

for temp in Temperature_Fahrenheit:
    Temperature_Degree.append((temp-32) * 5/9)
    if temp>95:
        Temperature_Warning.append('critical Temperature: '+str(temp)+'°F')

print(Temperature_Warning)


###### Aufgabe 3 ##########
sum1 = 0

for i in range(10):
    if i%3==0 or i%5==0:
        sum1 = sum1 + i

print(sum1)

sum2 = 0

for i in range(1000):
    if i%3==0 or i%5==0:
        sum2 = sum2 +i

print(sum2)


###### Lösungsvariante 2 ##########
# 5
answer5 = sum(range(5, 1000, 5))

# 3
answer3 = sum(range(3, 1000, 3))

# 15, because 15 can be / 3 and 5
answer15 = sum(range(15, 1000, 15))
print("Answer is: ", answer3 + answer5 - answer15)
