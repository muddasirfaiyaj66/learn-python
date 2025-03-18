import matplotlib.pyplot as plt

#data 
x = [ i for i in range(0,11)]
y = [y ** 2 for y in x]

plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('something else')
plt.show()
