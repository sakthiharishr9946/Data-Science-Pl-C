with open("C:/Python312/Data Science Class -Placement/M1.txt",'r') as f1, open("C:/Python312/Data Science Class -Placement/M2.txt",'r') as f2:
    text=f1.read()+f2.read()
with open("C:/Python312/Data Science Class -Placement/MM1.txt",'w') as f:
    f.write(text)