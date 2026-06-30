import csv
import sys

emails = {"email_data":[]}
while True:
    try:
        print("Enter 1 for regstriation \n2 for login \n 3 for exit ")
        enter_no = int(input("Enter a no: "))
    except ValueError:
        print("Enter only nos")
    if enter_no == 1:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        with open("email.csv","a") as file:
            writer = csv.DictWriter(file,fieldnames=["email","password"])
            writer.writeheader()
            writer.writerow({"email":email,"password":password}) 
    elif enter_no == 2:
        enter_email = input("Enter your email to login: ")
        enter_password = input("Enter your password:")
        with open("email.csv") as file:
            reader = csv.DictReader(file,fieldnames=["email","password"])
            for row in reader:
                if enter_email ==row["email"]and enter_password == row["password"]:
                    print ("login sucessfull")
                    break
            else: 
                print("No such user")
    else:
        sys.exit("Exited")

# re.search(partten,string,flags = 0)