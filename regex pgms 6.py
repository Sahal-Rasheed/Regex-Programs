import re
txt="Sahal Bingo"
x=re.search("[a-z]",txt) # a - z alphabets search eym
if x:
    print("found")
else:
    print("not found")