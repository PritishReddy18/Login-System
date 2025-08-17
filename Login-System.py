#sign up and login system

import os
import ast

if os.path.exists("user.txt"):
    with open("user.txt", "r") as f:
        user = ast.literal_eval(f.read())
else:
    user = {}

while True:
    choice = input("Sign up (1) , Login in (2) , Exit (3) ; Enter your choice : ")
    if choice == "1":
        new_user = input("Enter your username: ")
        new_pass = input("Create your password: ")
        if new_user in user:
            print("username already taken")
            continue
        user[new_user] = new_pass

        with open("user.txt", "w") as f:
            f.write(str(user))

        print("username successfully added")

    elif choice == "2":
       while True:
           old_user = input("Enter your username: ")
           if old_user in user:
               while True:
                   new_pass = input("Enter your password: ")
                   if user[old_user] == new_pass:
                       print("Successfully logged in")
                       break
                   else:
                       print("wrong password")
                       continue
               break
           else:
                print("Invalid username entered!")
                continue

    elif choice == "3":
        print("Ended successfully!!")
        break
    else:
        print("invalid choice")
        continue
