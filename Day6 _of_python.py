# try:
#     n = int(input("Table of "))
#     for i in range(1,11):
#         Table = n*i
#         print(f"{n}x{i}={Table}")
# except ValueError:
#     print(f"{n} is not a number")

# while True:
#     try:
#         print("Enter two numbers to divide")
#         n = int(input("Enter a number n: "))
#         k = int(input("Enter a number k: "))
#         division = n/k
#     except ValueError:
#             print("number is not an integer")
#     except ZeroDivisionError:
#         print("Number is not divisible by zero")
#     else:
#         break
# print(f"Division of {n}/{k} = {division}")

# x= int(input())
# z = str(x)
# revrs = z[::-1]
# if z == revrs :
#     print(True) 
# else:
#     print(False)


# l1 = [2,4,3]
# l2 = [5,6,4]
# l3 = []
# l1.reverse()
# l2.reverse()
# l4 = [str(i) for i in l1]
# l5 = [str(i) for i in l2]
# joint ="".join(l4)
# joint_1 ="".join(l5)
# joint = int(joint)
# joint_1 = int(joint_1)
# Sum_1 = joint_1+joint
# Sum_1 = [int(x)for x in str(Sum_1)]
# Sum_1.reverse()
# print(Sum_1)
n = int(input("EN: "))
t = tuple((input().split()))
t = tuple(map(int,t))
print(hash(t))