import numpy as np

y = 9, 2, 5, 4, 12
# Standard Deviation = mean (abs(x - x.mean())²)
# textbook code = SD / Accuracy
print(np.std(y) / 250)
# output = 0.014444376068214231
# the result is the cushion allowance for regression outputs

