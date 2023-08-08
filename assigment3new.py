import random


name = ('Wellcome shiba')
print(name)
my_choice = input("your num:")

while True:
    if my_choice == "1":
        roll = random.randint(1,6)
        print("your roll result:", roll)
        if roll ==6:
            print("second-choice")
            second_choice = random.randint(1,6)
            print("second_chioce:", second_choice)
        else:
            break
        if my_choice == "2":
            break
        else:
            print("Error!")