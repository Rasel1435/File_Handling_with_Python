#Task 7
#Create a Simple File System
#Creation, Writing Data, Modifying File Data, Reading Data.
import os

while True:
    option = int(input("Select File Operation: 1.Create 2.Add Data 3.Delete 4.View"))
    if option == 1:
        fillename = input("Enter Filename: ").replace(" ","_")
        try:
            with open(f"{fillename}.txt", mode='x') as f:
                data = input('Enter Data')
                f.write(data)
        except FileExistsError as e:
            print(e)

    elif option == 2:
        fillename = input("Enter Filename: ")
        try:
            with open(f"{fillename}.txt", mode='a') as f:
                data = input('Enter Data')
                f.write('\n'+data)
        except FileNotFoundError as e:
            print(e)

    elif option == 3:
        fillename = input("Enter Filename: ")
        try:
            os.remove(f"{fillename}.txt")
        except FileNotFoundError as e:
            print(e)

    elif option == 4:
        fillename = input("Enter Filename: ")
        try:
            with open(f"{fillename}.txt", mode='r') as f:
                for line in f.readlines():
                    print(line)
        except FileNotFoundError as e:
            print(e)

    else:
        print("Select Valid option!")

        