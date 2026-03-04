from collections import Counter
word1="anagram"
print("Enter a word to find Anagram of the word |Anagram|}")
word2=input()


if (Counter(word1))==(Counter(word2)):
    print("Anagram")
else:
    print("Not a Anagram")