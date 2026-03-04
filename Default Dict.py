from collections import defaultdict

a=defaultdict()

a=["Mahimithran","Sakthi","Vishnu","Yugeshwarar","Ratish","Midhun"]

print(a)


for word in a:
    print(f"{word}:{len(word)}")