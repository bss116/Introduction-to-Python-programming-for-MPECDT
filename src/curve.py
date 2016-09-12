import pylab
import numpy as np

xy_file = open("../data/xy.dat", "r")

#Initialise an empty list to store the elevation
x = []
y = []

# Now we start reading the interesting data
n = 0
while True:  # This will keep looping until we break out.
    # Here we use a try/except block to try to read the data as normal
    # and to break out if unsuccessful - ie when we reach the end of the file.
    try:
        # Read the next line
        line = xy_file.readline()

        # Split this line into words.
        words = line.split()

        # If we do not have 52words then it must be blank lines at the end of the file.
        if len(words) != 2:
            break
    except:
        # If we failed to read a line then we must have got to the end.
        break

    n += 1  # Count number of data points

    try:
        # The elevation data is on the 4th column. However, the BODC
        # appends a "M" when a value is improbable and an "N" when
        # data is missing (maybe a ship dumped into it during rough weather!)
        # Therefore, we put this conversion from a string into a float in a
        # try/except block.
        xdata = float(words[0])
        x.append(xdata)
        ydata = float(words[1])
        y.append(ydata)

    except:
        continue

# For plotting lets convert the list to a NumPy array.
x = np.array(x)
y = np.array(y)

#print len(x)
#print len(y)

pylab.plot(x, y)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.show()

print np.max(y)
print np.min(y)
