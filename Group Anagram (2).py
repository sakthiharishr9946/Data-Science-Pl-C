from collections import defaultdict

grp_ana=defaultdict(list)
words=["eat","tea","tan","ate","nat","bat"]
for word in words:
    key=''.join(sorted(word))
    grp_ana[key].append(word)
print(list(grp_ana.values))