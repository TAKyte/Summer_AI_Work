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

print("\n\n\n\n\n" + y_test + "")

# Initialize the neural network
classifier = Sequential()
# Layers 
classifier.add(Dense(units = 32, activation = 'relu', input_dim = 30))
classifier.add(Dense(units = 16, activation = 'relu'))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dense(units = 6, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy')
classifier.fit(x_train, y_train, batch_size = 1, epochs = 150)

y_pred = classifier.predict(x_test)
y_pred = [ 1 if y>=0.5 else 0 for y in y_pred ]

total = 0
correct = 0
incorrect = 0
# loop all predictions
for i in range(len(y_pred)):
  total=total+1
  # check each position in array and if the known solution matches the prediction
  print(y_test.at[i,0] + " " + y_pred[i])
  if(y_test.at[i,0] == y_pred[i]):
    correct=correct+1
  else:
    incorrect=incorrect+1

print("Accuracy " + str(correct/total))
print("Correct " + str(correct))
print("incorrect " + str(incorrect))