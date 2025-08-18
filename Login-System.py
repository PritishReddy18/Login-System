import json
import os

file = "user.json"

# Load existing user data
if os.path.exists(file):
    try:
        with open(file, "r") as f:
            user = json.load(f)
    except json.JSONDecodeError:
        user = {}
else:
    user = {}

# --- Main Program Loop ---
while True:
    choice = input("Sign up (1) , Login in (2) , Exit (3) ; Enter your choice : ")

    # --- SIGN UP ---
    if choice == "1":
        new_user = input("Enter your username: ")
        if new_user in user:
            print("❌ Username already exists! Please try another.")
            continue
        else:
            new_pass = input("Create your password: ")
            user[new_user] = new_pass
            # Save the updated dictionary immediately
            with open(file, "w") as f:
                json.dump(user, f, indent=4)
            print("✅ Username successfully created!")

    # --- LOGIN (Simplified Logic) ---
    elif choice == "2":
        while True:
            old_user = input("Enter your username: ")
            if old_user in user:
                while True:
                   old_pass = input("Enter your Password: ")
                   if user[old_user] == old_pass:
                       print("Successfully logged in!")
                       break

                   else:
                       print("Wrong password! entered")
                       continue
                break
            else:
                print("Incorrect username!")
                continue

    elif choice == "3":
        print("BYE! see u soon again!!")
        break
    else:
        print("Invalid choice!")
        continue
