import csv

with open("C:/Users/harish/Downloads/Coimbatore.txt",'w') as data:
    writer=csv.writer(data)
    writer.writerow(["S.No","Name","Dept"])
    writer.writerow([1,"Mahimithran","Ph.D (DS)"])
    writer.writerow([2,"Sakthi","M.Sc (DS)"])
    writer.writerow([3,"Vishnu","M.Phil (DS)"])
