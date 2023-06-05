from random import randint

# 50 first names 25 male 25 female
f_name = ["James", "Robert", "John", "Michael", "David", "William", "Richard",
          "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew",
          "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
          "Kenneth", "Kevin", "Brian", "George", "Timothy",
          "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara",
          "Susan", "Jessica", "Sarah", "Karen", "Lisa", "Nancy", "Betty",
          "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna",
          "Michelle", "Carol", "Amanda", "Dorothy", "Melissa", "Deborah"
         ]
# 50 last names
l_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
          "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales",
          "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
          "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez",
          "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott",
          "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker",
          "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
         ]
# birth month
b_month = ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"
           ]
# state of birth
b_state = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
           "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
           "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
           "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
           "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# favorite color from list
f_color = ["Green", "Blue", "Red", "Yellow", "Pink"]

# open/create file and make 100000 entries
with open('data.txt', 'w') as f:
    for i in range(100000):
        f.write(f_name[randint(0,49)] + "," + l_name[randint(0,49)] + "," + b_month[randint(0,11)] + "," + b_state[randint(0,49)] + "," + f_color[randint(0,4)] + "\n")
    
