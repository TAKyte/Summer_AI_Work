# numpy for array deceleration matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt

# read text file from
data = open('data.txt', 'r')
# file reader
People = data.readlines()
# starting index for adding people info to array increase after each line
index = 0
# make array to hold info 
person_data = np.zeros((len(People), 5))
# convert the array to string type to hold values # string can be up to 16 charters 
person_data = person_data.astype('<U16')

# read in all data split the array by ,
# for each index overwrite the 0's with the person array 
# then increase the index when done close the file
for line in People:
    line = line.rstrip()
    person = line.split(",")
    person_data [index] = person
    index+=1
data.close()

# print all catagories of person data from a random index to show that data can be read
test_person = 52
print("\nthe " + str(test_person+1) +" respondent is "+person_data[test_person][0]+" "+person_data[test_person][1])
print("they were born in "+person_data[test_person][3]+" during the month of "+ person_data[test_person][2])
print("and their favorite color is "+person_data[test_person][4]+"\n")

# initialize all colors to zero for counting favorite colors
Green = 0
Blue = 0
Red = 0
Yellow = 0
Pink = 0

# loop through each entry finding their favorite color
for entry in range(len(person_data)):
    ans = person_data[entry][4]

    if ans == "Green":
        Green += 1
    elif ans == "Blue":
        Blue += 1
    elif ans == "Red":
        Red += 1
    elif ans == "Yellow":
        Yellow += 1
    elif ans == "Pink":
        Pink += 1

# plot info data, labels, color to display category as
fColors = [Green, Blue, Red, Yellow, Pink]
myLabels = ["Green", "Blue", "Red", "Yellow", "Pink"]
myColors = ["Green", "Blue", "Red", "Yellow", "Pink"]

# plot data, labels, colors, display percentiles
plt.pie(fColors, labels=myLabels, colors=myColors, autopct='%1.1f%%')
plt.title("favorite colors")
plt.show()


# initialize all colors to zero for counting favorite colors
Green = 0
Blue = 0
Red = 0
Yellow = 0
Pink = 0

# find all december birthdays and their favorite color
for entry in range(len(person_data)):
    if person_data[entry][2] == "December":
        ans = person_data[entry][4]

        if ans == "Green":
            Green += 1
        elif ans == "Blue":
            Blue += 1
        elif ans == "Red":
            Red += 1
        elif ans == "Yellow":
            Yellow += 1
        elif ans == "Pink":
            Pink += 1

fColors = [Green, Blue, Red, Yellow, Pink]
# plot data, labels, colors, display percentiles
plt.pie(fColors, labels=myLabels, colors=myColors, autopct='%1.1f%%')
plt.title("December birthday favorite colors")
plt.show()