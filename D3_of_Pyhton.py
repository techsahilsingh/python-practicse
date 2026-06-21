def main():
    """Conditional statements"""
    # data = user_data()
    # print(data)
    

# def user_data():
#     name = input("Enter your name: ").strip().title
#     age = int(input("Enter your Age: "))
#     if age >=18:
#         if name == "":
#             print("Please Enter a Name")
#             enter_name = input("").strip().title()
#             print(f"Welcome,{enter_name}")
#         else:
#              print(f"Welcome,{name}")
#     else :
#         print("You must be over 18")
n = int(input().strip())
if n%2 ==0 and range(2,6):
    print("Not Weird")
elif n%2 ==0 and range(6,21):
    print("Weird")
elif n%2 ==0 and n>20:
    print("Not Weird")
else:
    print("Weird")

main()



