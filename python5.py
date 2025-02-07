# Taking input from user
# in python we can use input() function for input from user. this input function gives return value as string/chatacter

a = input("ENTER YOUR NAME: ")
print("YOUR NAME IS : ",a)

# input function assign karta hai varible ke andar wo string jisko user deta hai
# python mai by default ya hai ki jab hum usko input denge kuch bhi to wo use as a string dekhega

b = input("ENTER YOUR FIRST NUMBER : ")
c = input("ENTER YOUR SECOND NUMBER : ")           

print(b + c)                                  # concatenate kar dega
print(int(b)+int(c))                          # ACTUAL ARITHMETIC OPERATION
print(int(b)+float(c))                        # ACTUAL ARITHMETIC OPERATION
print(bool(b)+bool(c))                        # ACTUAL ARITHMETIC OPERATION
