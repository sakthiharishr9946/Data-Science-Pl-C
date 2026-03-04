with open("C:/Users/harish/Downloads/Coimbatore.txt",'r') as f:
    print(f.tell())
    print(f.seek(19))
    print(f.read())