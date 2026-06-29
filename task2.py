num = int(input("Enter number of lines: "))
fname = input("Enter filename: ")

myfile = open(fname, "w")

for i in range(1, num + 1):
    content = input(f"Enter content for {fname} line {i}: ")
    myfile.write(content + "\n")

myfile.close()

print("File created successfully!")