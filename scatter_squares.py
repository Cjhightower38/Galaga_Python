import matplotlib.pyplot as plt

x_val = [1, 2, 3, 4, 5]
y_val = [1, 4, 9, 16, 25]

# (s=) represents the size of the point
plt.scatter(x_val, y_val, s=100)
# Set chart title and label axes.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


import matplotlib.pyplot as plt

x_val = list(range(1, 1001))
y_val = [x**2 for x in x_val]

plt.scatter(x_val, y_val, s=40)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
