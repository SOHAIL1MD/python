#   the conversion of one data types to other data type in known as type casting or type conversion
#   python supports a wide variety of functions/method like int str floar hex oct dict set tuple for type casting 
#   jab hum variable declare karen string type ka aur use

a = "10"
b = "2"

print(a+b)


m = 10
n = 2
print(int(m)+int(n))

# a1 = "MOHAMMAD"
# b1 = "SOHAIL"

# print(a1+b1)

# a2 = "MOHAMMAD "
# b2 = "SOHAIL"

# print(a2+b2)

# a3 = "10"
# b3 = "SOHAIL"

# print(a3+b3)


# there are two types of type casting
# explicit(jo hum chah kar rhe hain) it can be achieved by python built in type conversion fncts likeint float hex oct str 
# implicit(jo python automatically kar rha hai

#   example of explicit conversion

string = "15"
number =  15
string_number = int(string)
sum = number + string_number
print("The sum of both number is: ", sum)

# example of implicit conversion
# isme order dekha jata hai chote order wala bade order mai change hota hai taaki data loss na ho

x = 14
print(type(x))

y = 13.0                                    # float>>int
print(type(y))

z = x+y
print(z)
print(type(z))