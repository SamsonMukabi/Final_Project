f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
f.close()

# Convert data to floats
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])

# Compute mean and standard deviation
import numpy as np

mean_price = np.mean(appleprices)
std_dev_price = np.std(appleprices)

# Print results
print("Mean Price:", round(mean_price, 2))
print("Standard Deviation:", round(std_dev_price, 2))
