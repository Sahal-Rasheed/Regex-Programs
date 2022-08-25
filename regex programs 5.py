import re
txt="Sahal Bingo"
x=re.search("[^bog]",txt) #b,o,g ozhike ella lettersilm edelm ail ondon nokum edelum ndaya madi for that use - ^ to skip unwanted alphabets
if x:
    print("found")
else:
    print("not found")