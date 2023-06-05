import pandas as pd
#data set
ds = pd.read_csv("cancer.csv")
# x data set is the dataset without the results so drop the first column
x = ds.drop(columns="diagnosis(1=m, 0=b)")
# y is just the known results
y=ds["diagnosis(1=m, 0=b)"]