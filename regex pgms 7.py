import re
txt="Sahal Bingo"
x=re.search("Sah?.l",txt) #one or zero occurane nokuka oloo ail koodya false
if x:
    print("found")
else:
    print("not found")