# string slicing
    # (if we want some specific range of string to print)

# jab hum index ke range likhte hain [] isme to last wale index ko print nahi karega
names = "Mohammad,Sohail"
print(names[0:8])      # like 0 to n-1 
  

# length of strin(no of character including space)

print(len(names))

# or

na = 'my name is sohail'
len= len(na)
print("intro is",len,"character sentence")

# hame starting index mention karna hoga ki hum kaha se start karna chahte hain agr nahi karenge  to python by default
# 0 lega

aabc = "default"
print(aabc[:2])           # agr hamne koi intial index mention nahi kiya to by default python 0 lega
print(aabc[2:3])          # if we want to mention from other than 0
print(aabc[:])            # if we want to print full string
# uppar  ke teeno ko string slicing kehte hain aur abb hum negative slicing ko dekhenge

print(aabc[0:-3])         # aise mai bydefault pehle highest index lega compiler and -3 ko add kar dega highest ke sath
# print(aabc[0:len(aabc)-3])