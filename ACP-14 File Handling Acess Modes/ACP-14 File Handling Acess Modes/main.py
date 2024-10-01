file_read = open('Abcd.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('Abcd.txt','w')
file_write.write("File in write mode .....")
file_write.write("This is file program")
file_write.close()

file_read = open('Abcd.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_append = open('Abcd.txt','a')
file_append.write("/n File in append mode ......")
file_append.close()

file_read = open('Abcd.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()