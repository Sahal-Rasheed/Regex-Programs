import re
txt="Sahal Bingo"
x=re.search("^Sahal",txt) #starting known
if x:
    print("found")
else:
    print("not found")