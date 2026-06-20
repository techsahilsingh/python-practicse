def main():
    """Conditional statements"""
    data = user_data()
    print(data)

def user_data():
    name = input("Enter your name: ").strip().title
    age = int(input("Enter your Age: "))
    if age >=18:
        if name == "":
            print("Please Enter a Name")
            enter_name = input("").strip().title()
            print(f"Welcome,{enter_name}")
        else:
             print(f"Welcome,{name}")
    else :
        print("You must be over 18")

def lists():
    List_1 = [int(input("Enter 5 Numbers"))]


main()



