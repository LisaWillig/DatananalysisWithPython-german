#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

### Aufgabe 1 : Strings ###

myStrings = {}
data = np.genfromtxt("Daten/Data6_2.txt", dtype = str,  delimiter = '\t')

print(data)

for entry in data:
    try:
        myStrings[entry] +=1
    except KeyError:
        myStrings[entry] = 1
print(myStrings)


### Aufgabe 2 : Daten regridden ###

def regridArray(Array, Column, Grid):
    """
    This function returns a new version of a numpy Array where data are
    averaged within boxes of a given grid. The new array contains the average
    value of the datapoints within each gridbox. If the datapoints coincide
    with the gridpoints this function reduces to a simple average.

    Parameters
    ----------
    Array : numpy Array
        numpy Array that contains separate data in columns
    Column : integer
        integer number of the column to which the array will be regridded
    Grid:  1D numpy Array
        Array that contains the gridpoints
        select = Grid(i)<= Array(:,Column) & Array(:,Column)< Grid(i+1)

    Returns
    ------
    result : numpy Array
    a numpy array that contains the regridded Array

    Example
    -------

    >>> AllDataAveraged =regridArray(AllDataNormalized,0,TimeGrid)

    This returns a numpy array that is regridded according to column 1 and the
    specified TimeGrid.

    """

    time = Array[:, Column]
    ArrayTemp = Array
    ArrayNew = np.zeros((np.size(Grid), 2))
    ArrayNew[:, 0] = Grid
    counter = 0
    for t in range(np.size(Grid) - 1):
        select1 = time >= Grid[t]
        select2 = time < Grid[t + 1]
        select = select1 & select2
        if np.sum(select) <= 0.:
            ArrayNew = np.delete(ArrayNew, t - counter, 0)
            counter += 1
        else:
            ArrayNew[t - counter, 1] = np.mean(ArrayTemp[select, 1])

    return (ArrayNew)


# Read Data
data = np.genfromtxt("MOKE.txt", skip_header=1)

# Create new Grid for Time
grid1 = np.linspace(-50, 0,2, endpoint=True)
grid2 = np.linspace(0, 1,5, endpoint=True)
grid3 = np.linspace(1, 100,10, endpoint=True)
grid4 = np.linspace(100, 1000, 50, endpoint=True)
grid = np.concatenate((grid1, grid2, grid3, grid4), axis=0)

# Call regrid function, returns new Array
data_regrid = regridArray(data, 0, grid)

# Plot Old vs New Array
plt.plot(data[:, 0]-180, data[:, 1], label=('Original'))
plt.plot(data_regrid[:, 0]-180, data_regrid[:, 1], 'o', label=('New Grid'))
plt.legend()
plt.title("MOKE Signal")
plt.xlabel("time (ps)")
plt.ylabel("Intensity (a.u.)")
plt.show()
plt.savefig("RegridExample.png")