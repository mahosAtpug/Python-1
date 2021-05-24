introduction = input ("Enter Your Introduction : ")
print (introduction)

characterCount = 0
wordCount = 1
for i in introduction :
    characterCount = characterCount + 1
    if (i == " "):
        wordCount = wordCount + 1

print("Number of Characters Your Wrote : " , characterCount)
print("Number of Words Your Wrote : " , wordCount)