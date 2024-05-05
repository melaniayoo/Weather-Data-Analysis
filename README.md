# Weather-Data-Analysis

- Utilized Python to examine and visualize the average temperatures for specific time periods with datasets.
- Processed data from a CSV file using Python s Matplotlib library to create a line plot, generating a graph.png image.

## Project Description

This repository analyzes weather data from a CSV file, specifically focusing on visualizing average temperatures for specific time periods. Here's a breakdown of what it does:

1. Importing Libraries: Imports necessary libraries for data visualization, such as Matplotlib.
2. Setting up Matplotlib: It configures Matplotlib to save plots as image files.
3. Reading Data: It opens a CSV file named "2850814.csv" and prints the first line to get a sense of its structure.
4. Data Processing: Reads the data line by line and adds it to a list called `data`. 
5. Plotting Data: It sets up x and y values for the plot. In this case, the x-values represent indices (0 to the length of data) and y-values represent the temperature data.
6. Creating Plot: It creates a figure and adds a subplot to it. Then, it plots the data points on the subplot.
7. Saving Plot: Finally, it saves the plot as a PNG image named "graph.png".

This script essentially visualizes temperature data from a CSV file using Matplotlib, producing a line plot as output.

## Project Structure: 

```
main
|---- 2850814.csv
|---- graph.png
|---- main.py
```
