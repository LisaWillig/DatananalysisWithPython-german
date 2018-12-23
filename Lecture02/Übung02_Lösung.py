import numpy as np

#### Aufgabe1 ####

# Create a Vector
firstVector = np.arange(10, 50)

# Change the order of the vector
firstVector[::-1]

# create an array of a certain shape (3,3), 
# fill it with values from 0 to 8
secondArray = np.arange(9).reshape(3,3)

# fill a creates array with random values
thirdArray = np.random.rand(5, 5)

# Use numpy functions to determine max value, 
# min value and the mean value of the array
print('Max: ', np.max(thirdArray))
print('Min: ', np.min(thirdArray))
print('Mean: ', np.mean(thirdArray))

# create an array with shapes 10x10 
# filled with ones
fourthArray = np.ones(shape=(10, 10))

# write Zeros in the outer columns and rows
fourthArray[0,:]=0
fourthArray[:,0]=0
fourthArray[-1,:]=0
fourthArray[:,-1]=0
print(fourthArray)

# cut through the array to get 
# subarray only filled with ones
fifthArray=fourthArray[1:-1, 1:-1]

# Add Arrays together, plusoperator 
# performs elementwise operations
sixthArray = fifthArray + fifthArray
print(sixthArray)

# Get the size or length of an array
print(sixthArray.size)
print(len(sixthArray))

# Ask if 2 Arrays are equal
print(np.equal(sixthArray,fifthArray))
print(np.array_equal(sixthArray,fifthArray))

# create two arrays filled with zeros 
# and ones respectively
firstArray = np.zeros(shape=(10, 10))
secondArray = np.ones(shape=(10, 10))

# Fill every even numbered row/column 
# pair with the value 5
for row in range(len(firstArray[:, 0])):
    for col in range(len(firstArray[0, :])):
        if row%2 == 0 and col%2 == 0:
            firstArray[row][col] = 5

# Use of boolean indexing: get only values 
# for above 5/below 5
newFirst = firstArray[firstArray>2]
newSecond = firstArray[firstArray<2]

# Fill positions in array with 5 by using 
# index slices
otherOption = np.zeros(shape=(10, 10))
otherOption[0:9:2, 0:9:2] = 5

# Shape information gets lost during boolean indexing
# regain shape by reshaping (but the position of the
# original index is still lost)
thirdArray = np.concatenate((newFirst, newSecond), axis = 0)
print(thirdArray.reshape(10, 10))


# Examples for Python scope
############################
i = 5

def myFunction(i):
    i +=1
    return i

print(i)
i = myFunction(i)
print(i)
print(myFunction(i))

############################
def firstfunction():
    i = 20

    def secondfunction():
        global i
        i = 30
    #    print(i)

    secondfunction()
    print(i)

i = 10
firstfunction()
print(i)