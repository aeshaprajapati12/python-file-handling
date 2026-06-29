myfile = open("Aesha.txt","w")
myfile.write("Hello Aesha!!")
myfile.close()

print("\n")

myfile = open("Aesha.txt","a")
myfile.write("Hello Aesha!!")
myfile.close()

print("\n")

myfile = open("Aesha.txt","x")
myfile.write("Hello Aesha!!")
myfile.close()

print("\n")


f = open("Aesha.txt", "r")
print(f.read())
f.close()

print("\n")

myfile2 = open("Aesha.txt","r")
mydata = myfile2.read()
print(mydata)

print("\n")




