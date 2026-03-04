with open("C:/Users/harish/Downloads/Coimbatore.txt",'r') as f:
    words=f.read()
    words=words.split()
    for word in words:
        print(word)