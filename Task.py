Dept=['CS','IT','CSDA','AIDS','AIML','DS']
SoCS=['CS','IT']
SoISDS=['CSDA','AIDS','AIML','DS']
Dept
Dept.remove("AIML")
for i in Dept:
    if i in SoISDS:
        print("SoISDS:",i)
    if i in SoCS:
        print("SoCS:",i)

Dept.append("CSCS")
SoCS.append(Dept[5])
print(Dept)
print(SoCS)