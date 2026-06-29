num = int(input("Enter number of users: "))
fname = input("Enter filename: ")

myfile = open(fname, "w")

for i in range(1, num + 1):
    print(f"\nEnter details of User {i}")

    name = input("Enter name: ")
    email = input("Enter email: ")
    mobileno = input("Enter mobile no: ")
    address = input("Enter address: ")

    myfile.write(f"User {i}\n")
    myfile.write(f"Name    : {name}\n")
    myfile.write(f"Email   : {email}\n")
    myfile.write(f"Mobile  : {mobileno}\n")
    myfile.write(f"Address : {address}\n")
    myfile.write("-" * 30 + "\n")

myfile.close()

print("File created successfully!")