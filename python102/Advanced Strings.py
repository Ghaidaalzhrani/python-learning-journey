# Find
text = "Traveling to new places allows people to discover different cultures, meet interesting people, and create unforgettable memories."
print(text.find("memories"))
print(text.find("traveling"))
print(text.find("to"))
#The `find()` function returns the index of the first matching element it encounters in the string.If we want to search for the last occurrence of an element, we use `rfind()`.
print(text.rfind("to"))
#Searching for an element within a specific range in the string
print(text.find("discover" ,40 ,50 ))


# Convert Text to List  ""Useing split"" The elements are separated based on spaces, meaning that spaces in the string are considered to separate one element from another.)
text = "A B C"
string_to_list1 = text.split()
print(string_to_list1)
#By default, elements are split based on spaces, but we can specify a different separator, such as a comma, by passing it to the function.
s = "ghida,ali,saeed,alzhrani"
string_to_list2 = s.split(",")
print(string_to_list2)
#As we can see, it not only uses the separator passed to the function for splitting, but also removes it from the string.for example:
text2 = "this is a string"
s = text2.split("s")
print(s)
#The `split()` function also allows you to control the number of splits and the resulting output.
text2 = "this is a string"
s = text2.split("s" , 1)
print(s)


# Convert List to Text ""Useing join""
text3 = ["A" , "B" , "C"]
print(" ".join(text3)) #The space here is the separator between each element in the string.
text3 = ["A" , "B" , "C"]
print("#".join(text3))

#The `join()` function also works with dictionaries and tuples.
d = {"name":"Ghaida" , "old":"19" , "major":"Ai"}
print(" ".join(d)) #This returns the keys.
print(" ".join(d.values())) #This returns the values.

t2 = ("i" , "love" , "Ai" , "and" , "python")
print(" ".join(t2))


# Text Validation (Use `is...()` methods to check whether a string meets certain conditions; they return a Boolean value.)
valuse = "A7i44"
print(valuse.isalpha()) #Checks if all characters are alphabetic
print(valuse.isalnum()) #Checks if all characters are letters or numbers
print(valuse.isdigit()) #Checks if all characters are digits
num = "100"
print(num.isdigit()) #Checks if all characters are decimal digits. Examples: "3" → True, "12.3" → False
num1 = "⁴"
print(num.isdecimal()) #Checks if all characters are digits. Examples: "²" or "3" → True, "12.3" → False
num3 = "¾"
print(num.isnumeric()) #Checks if all characters are numeric. Examples: "½" or "²" or "3"→ True, "12.3" → False

text4 = "she is so smart"
print(text4.islower())
print(text4.isupper())
text5 = "AI"
print(text5.isupper())
print(text5.islower())
text6 = "She Is So Smart"
print(text6.istitle())
text7 = " "
print(text7.isspace())

text8 = "my_fav_food"
print(text8.isidentifier())
text9 = "my name"
print(text9.isidentifier())


# strip() Function (Removing extra spaces from the string.)
p = "        learning python          "
print(p.strip())
p1 = "        learning python          "
print(p1.strip()) #It removes spaces from the beginning of the string.
p2 = "        learning python          "
print(p2.rstrip()) #It removes spaces from the end of the string.

p3 = "\n learning python "
print(p3.strip()) #Removing extra lines.

# replace() Function (Replacing a word that appears once or multiple times in the string.)
v1 = "1\n2\n3\n4\n5\n"
print(v1)
print(v1.replace("\n" , ","))

frinds = "Ghaida and Nadia are bistfrind"
print(frinds)
print(frinds.replace("bistfrind" , "sisters"))

# Text Manipulation
str = "I Enjoy Reading Books Because Books Are Relaxing"
print(str.lower())
print(str.upper())
print(str.swapcase()) #Changing uppercase letters to lowercase and lowercase letters to uppercase.
str2 = "I enjoy reading books because books are relaxing"
print(str2.title()) #Changing the first letter of each word to uppercase.


# Raw String Concept ( Adding r or R before a string makes backslashes (\) part of the string instead of escape characters.)
raw1 = "\t python"
print(raw1)
raw2 = r"\t python"
print(raw2)
#raw3 = "\xMyFolder\xMySubFolder\xMyFile.text"  ""it return erorre"""
#print(raw3)
raw4 = R"\xMyFolder\xMySubFolder\xMyFile.text"
print(raw4)


# format() Function (The format() function replaces curly braces {} with the given values)
first_name = "Ghaida"
second_name = "Ali"
age = "19 years old"
study = "I study Artificial Intelligence"
print("My name is {} {} , I am {} , and {}".format(first_name , second_name , age , study )) #pass the variables whose values we want to insert, in order.

frind1 = "Ghaida"
frind2 = "Rudayna"
frind3 = "Hams"
frind4 = "Aldanah"
print("{},{},{} and {} are frinds".format(frind1 , frind2 , frind3 , frind4))
#OR: Indexes can also be used to change the order of the variables.
print("{3},{2},{0} and {1} are frinds".format(frind1 , frind2 , frind3 , frind4))
#also each index can also be assigned a specific variable name and passed accordingly.
print("{F3},{F1},{F2} and {F4} are frinds".format(F1=frind1 , F2=frind2 , F3=frind3 , F4=frind4))

