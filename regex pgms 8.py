import re
txt="Sahal Bingo"
x=re.search("Sah+?",txt) #one or more occurance
if x:
    print("found")
else:
    print("not found")