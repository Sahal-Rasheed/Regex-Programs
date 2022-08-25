import re
txt="Sahal Bingo"
x=re.search("[Bingo]",txt) #use sqr brace to search any word in txt
if x:
    print("found")
else:
    print("not found")