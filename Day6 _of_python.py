# try:
#     n = int(input("Table of "))
#     for i in range(1,11):
#         Table = n*i
#         print(f"{n}x{i}={Table}")
# except ValueError:
#     print(f"{n} is not a number")

while True:
    try:
        print("Enter two numbers to divide")
        n = int(input("Enter a number n: "))
        k = int(input("Enter a number k: "))
        division = n/k
    except ValueError:
            print("number is not an integer")
    except ZeroDivisionError:
        print("Number is not divisible by zero")
    else:
        break
print(f"Division of {n}/{k} = {division}")