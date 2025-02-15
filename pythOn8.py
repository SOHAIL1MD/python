# yaad rahe index mai compiler start se leke end-1 tak print karega but o se start karne ki wjh se hame lagta hai ki end tak print ho rha hai  
#print("my name is mohammad khan")
#  index
name = 'mohammad' 
print(name[:8])

# length function
name1 = 'SOHAIL'
print(len(name1))
print("given name involve",len(name1),'character')

len1 = len(name1)

print("given name involve",len1,'character')

# index function ke istemal karte waqt agr 0 nahi lagaye to wo by default 0 lega warna hum waha kisi aur integer ko bhi le sakte hain khud ki trf se
print(name[:2])
print(name[2:4])

# aur agr hum kuch bhi specify nahi karenge to to bydefault wo start mai 0 and end mai length lega string ka 
print(name[:])

# NEGATIVE SLICING
print(name[0:-5]) 
# isme actually by default length of name lega and usko add karga -5 se like print(name[0:10+(-5)])
print(name[0:len(name)+(-5)])

print(name[-4:-1])
# aise case mai compiler first bydefault pehle length lega and given numbers ko add karega
# aur agr aisa kuch banega kisi case mai 4:2 to full string ko print kar dega

print(name[-5:])
