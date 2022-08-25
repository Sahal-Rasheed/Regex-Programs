import re
txt="Sahal Middile Bingo"
x=re.search("^Sahal.*Bingo$",txt) #starting known and end known - (middle not known)
if x:
    print("found")
else:
    print("not found")