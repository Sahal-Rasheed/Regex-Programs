import re
txt="Sahal Bingo"
x=re.search("Bingo$",txt) #end known
if x:
    print("found")
else:
    print("not found")