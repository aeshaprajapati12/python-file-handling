fname = input("Enter filename: ")
content = input("Enter content: ")

myfile = open(fname, "w")
myfile.write(content)
myfile.close()

print("File created successfully!")
