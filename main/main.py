# This code plots a graph with the given data file.
# Written by Melania Yoo

# Import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
import random 

# Agg is used to create .png files
mpl.use('Agg')

# Create empty figure to plot graphs on
fig = plt.figure()

# Open the data file in .csv
f = open("2850814.csv", "r")
print(f.readline())

# Create a list for the data
data = [ ]

# This prints the data by line by line.
i = 0
for line in f:
  print(len(line))
  i+=1

  # This only prints the data, before 1140th line, which is the only available data in the file that the code can read. 
  if len(data) < 1140:
    print(i)
    # Appends each line into my data.
    data.append(int(line))
for l in data:
  print (l)

# y-values becomes the data and x values starts from zeero and ends when the data ends. 
x = [i for i in range (0,len(data))]
y = data

# Add subplots using add_subplot(rows,cols,number)
grid = fig.add_subplot(1,1,1)

# Add data to grids
grid.plot(x,y)

# Save graphs to .png file
fig.savefig('graph.png')