f=open("C:/Users/harish/Downloads/Coimbatore.txt","r")
read_operation=f.readlines()
print(read_operation)

with open("C:/Users/harish/Downloads/Coimbatore.txt",'r') as f:
    print("USING READ\n")
    print(f.read())
with open("C:/Users/harish/Downloads/Coimbatore.txt",'r') as f:
    print("USING READLINE\n")
    print(f.readline())
with open("C:/Users/harish/Downloads/Coimbatore.txt",'r') as f:
    print("USING READLINES\n")
    print(f.readlines())