import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5] 
y_axis = [45, 15, 21, 27, 42] 

plt.plot(x_axis, y_axis)

y_axis = [45, 30, 27, 27, 30]
plt.plot(x_axis, y_axis)

plt.xticks(range(0,6,1))
plt.xlabel("game")
plt.ylabel("marginal");
plt.show();
