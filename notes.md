#Date:27/06/2026
#Notes

An dictionary can be empety it does't matter . you can append a dictionary if its inside a list 
it can be used to create login,register function 
for eg
store_data = {"data":[]}
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    store_data["data"].append({"username": username, "password": password})
    break
