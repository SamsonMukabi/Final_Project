f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
f.close()

appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])

import matplotlib.pyplot as plt

days = list(range(1, len(appleprices) + 1))  # Day 1 to number of data points
prices = appleprices

plt.plot(days, prices, color='blue')
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.xlabel("Day")
plt.ylabel("Trading Price")
plt.grid()

plt.show()
