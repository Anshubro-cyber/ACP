file = open('a.txt','r')
print("File in normal read mode..")
print(file.read())
file.close()

file = open('a.txt','r')
print("File read in parts..")
print("\n Read in parts \n")
print(file.read(9))
file.close()

file = open('a.txt','r')
print("Reading first line..")
print(file.readline())
file.close()

file = open('a.txt','r')
print("Reading multiple lines..")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('a.txt','r')
print("Looping through lines..")
for line in file:
    print(line)
file.close()

print("Reading odd lines..")
fn = open('a.txt','r')
fn1 = open('au.txt','w')
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 !=0):
        fn1.write(cont[i-1])
    else:
        pass
fn1.close()
fn1 = open('au.txt','r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()
