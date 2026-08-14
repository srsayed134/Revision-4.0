mpwd = input("What is your master password? ")
#For master encrypted feature "https://youtu.be/O8596GPSJV4"

def view():
    name = input("Write which password do you need? ")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            if name == user:
                print("User: ", user, "| Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" +pwd + "\n")

while True:
    mode = input("Do you want an add password or viewing password and q means exit (add/view/q)? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        
