import pandas as pd
#data set
ds = pd.read_csv("cancer.csv")
# x data set is the dataset without the results so drop the first column
x = ds.drop(columns="diagnosis(1=m, 0=b)")
# y is just the known results
y=ds["diagnosis(1=m, 0=b)"]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15) 
from keras.models import Sequential
from keras.layers import Dense

# Initialize the neural network
classifier = Sequential()
# Layers 
classifier.add(Dense(units = 32, activation = 'relu', input_dim = 30))
classifier.add(Dense(units = 16, activation = 'relu'))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy')