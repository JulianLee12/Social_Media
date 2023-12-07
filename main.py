import json
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

with open('accounts.txt') as a:
    data = a.read()

accounts = json.loads(data)


def signUp(username, password):
    while (username in accounts):
        username = input("Username is already taken, please enter a diffrent one: ")

    accounts[username] = {"password": password, "post": []}
    print("Sign up successful! ")

    with open('accounts.txt', 'w') as f:
        f.write(json.dumps(accounts))

    profile(accounts[username], username)


def login(username, password):
    try:
        if (accounts[username]["password"] == password):
            print(f"Welcome {username} you logged in successfully! ")
            profile(accounts[username], username)
    except:
        print("Login incorrect try again! ")
        homePage()


def homePage():
    print(green + bold + italics + underline +
          """
          WELCOME TO JULIAN'S VERY OWN 
          INSTANT SOCIAL MEADIA
           """ + end)
    username = input("Username: ")
    password = input("Password: ")
    choice = input("signup/login: ")
    while (choice != "signup" and choice != "login" and choice != "x"):
        choice = input("Invalid choice, please select to either signup/login or press x to cancel")

    if (choice == "signup"):
        signUp(username, password)
    elif (choice == "login"):
        login(username, password)
    else:
        print("Returning to homepage...")
        homePage()

def post(user, username):
    print("POST A NEW STATUS")
    posting = True
    while (posting):
        newPost = input("Enter a new post or x to cancel: ")
        if (newPost == "x"):
            posting = False
            break
        print(f"You are posting {newPost}")
        confirm = input("Press y to confirm or x to cancel")
        if (confirm == "y"):
            user["post"].append(newPost)
            with open('accounts.txt', 'w') as f:
                f.write(json.dumps(accounts))
        else:
            continue

    profile(user, username)


def view(user,username):
    print("Viewing all posts")
    for i in range (len(user["post"])):
        print(f'{i+1}. {user["post"][i]}')
        print("----------------------------")

    confirm = ""
    while(confirm != "x"):
        confirm = input("Select x to return to homepage: ")

    if(confirm == "x"):
        profile(user,username)




def edit(user,username):
    print("Viewing all posts")
    for i in range(len(user["post"])):
        print(f'{i + 1}. {user["post"][i]}')
        print("----------------------------")

    choice = -1
    while (choice-1 not in range(len(user["post"]))):
        choice = int(input("Which status would you like to edit: "))

    print(f"You are editing {user['post'][choice-1]}")
    editPost = input("What would you like to edit: ")
    print(f"You are updating your post to {editPost}")

    confirm = ""
    while (confirm != "x" and confirm != "c"):
        confirm = input("Press c to confirm or x to to return to homepage")

    if(confirm == "c"):
        user['post'][choice-1] = editPost
        profile(user,username)
    else:
        profile(user,username)

def changePassword(user,username):
    newPassword = input("Please enter a new password for your account: ")
    while(newPassword == user["password"]):
        newPassword = input("Please enter a new password for your account: ")

    print(f"Your new password is {newPassword}")

    confirm = ""
    while (confirm != "x" and confirm != "c"):
        confirm = input("Press c to confirm or x to to return to homepage")

    if(confirm == "c"):
        user["password"] = newPassword
        with open('accounts.txt', 'w') as f:
            f.write(json.dumps(accounts))
        profile(user,username)
    else:
        profile(user,username)

def deleteStatus(user,username):
    if(len(user["post"]) == 0):
        print("No statuses to delete ")

        confirm = ""
        while (confirm != "x" and confirm != "c"):
            confirm = input("Press x to to return to homepage")
        if (confirm == "x"):
            profile(user, username)

    else:
        print("Viewing all posts")
    for i in range(len(user["post"])):
        print(f'{i + 1}. {user["post"][i]}')
    choice = -1
    while (choice - 1 not in range(len(user["post"]))):
        choice = int(input("Which status would you like to delete: "))

    print(f"You are deleting {user['post'][choice-1]}")

    confirm = ""
    while (confirm != "x" and confirm != "c"):
        confirm = input("Select c to confirm or x to to return to homepage")



    if (confirm == "c"):
        del user['post'][choice - 1]
        profile(user, username)

    else:
        profile(user, username)







def deleteUser(user, username):
    print("YOU ARE ABOUT TO DELETE YOUR ACCOUNT PERMANENTLY")
    password = input("Please type your password to confirm ")
    if(user["password"] == password):
        print("We have confirmed you account deletion. ")
        del accounts[username]
        with open('accounts.txt', 'w') as f:
            f.write(json.dumps(accounts))
        homePage()

    else:
        print("Invalid password please try again. ")
        homePage()

















def profile(user, username):
    print("-----------------------------")
    print("WELCOME " + username.upper(), dt_string)
    print("-----------------------------")

    print("PLEASE SELECT AN OPTION: ")
    print(
        """
    1. View Statuses📈
    2. Post a Status✍️
    3. Edit a Status📈
    4. Delete a Status🗑
    5. Change Password👤
    6. Delete Account❌
    7. Return to Homepage🏠
    """ + "\n")

    userChoice = ""
    while (userChoice not in ["1", "2", "3", "4", "5", "6", "7"]):
        userChoice = input("Please select an option: ")

    if (userChoice == "1"):
        view(user,username)
    if (userChoice == "2"):
        post(user,username)
    if (userChoice == "3"):
        edit(user,username)
    if (userChoice == "4"):
        deleteStatus(user, username)
    if (userChoice == "5"):
        changePassword(user,username)
    if (userChoice == "6"):
        deleteUser(user, username)
    else:
        homePage()





homePage()
























































































































