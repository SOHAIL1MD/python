# string in python
# jo bhi chiz ko double quote ya single quote ke andar likhe wo string hota hai
# print("MY NAME IS \"MOHAMMAD KHAN")       #JAB DOUBLE QUOTE LAGA HOO START AND END MAI AUR AGR HAME 
#                                          #DOUBLE QUOTE SENTENCE MAI CHAHIYE TO \" LAGAO AUR AGR SINGLE QUOTE HAI TO
#                                         #  DOUBLE QUOTE NRML LAGA SAKTE
# print('MY NAME IS "MOHAMMAD KHAN')

# name = "sohail"
# print("hello", name)

# python generally usi line mai dekhta hai ki string close hua ya nahi hua agr nahi to EOL(end of line )error dega
# isse bachne ke liye hum single triple ya double quote ka istemal karenge agr hume multiple line string chahiye too
intro = '''MY NAME IS MOHAMMAD, KHAN
                            I'M 20 YEARS OLD
                            I PERSUE MY BE IN COMP ENGG FROM AIKTC PANVEL'''

print(intro)


st =  """
                                Developer friendly text for describing the purpose of function
                                Some test cases used by different unit testing libraries
                                """

print(st)

#   index in string (if we want to print any specific letter from string)
#   consider fisrt letter as zero index and last index is not print
# in python string is like an array of character (array = collection of items)

name = "MOHAMMAD"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

# if we want to print full string as above method 
# one way is calculate full length with alphaber as well as space
# another way is for loop with string 

intro = 'my name is mohammad khan'
for character in intro:
    print(character)