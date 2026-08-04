# Indexing Concept(Accessing elements in lists, strings, and tuples)
alphabbet = "abcdefghijklmnopqrstuvwxyz"
print(alphabbet[6])
#OR
print(alphabbet[-20])


# Slicing Concept(Closed range: from ... to ...) [IN STRING]
text = "My name is Ghaida, and I enjoy studying Python."
print(text[40 : 46])
#OR
print(text[-7 : -1])

#OR (Open range: from start to end)
print(text[23 : ])
#OR
print(text[-24: -1 ])

#OR (Open range: from end to stsrt)
print(text[ : 17])
#OR
print(text[-47 : -30])

#OR (Open range: print all the string)
print(text[:])

# Slicing Concept [ IN LIST/TUPLE]
list1= [1 , 2 , 3 ,4 , 5]
print(list1[3 : 5])

tuple1 = (6 , 7 , 8 , 9 , 10)
print(tuple1[1 : ])


# Slicing Concept (By selecting a specific pattern)
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[0 : 16 :2])
#OR
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[16 : : -2])


# slice() Function
alphabbet = "abcdefghijklmnopqrstuvwxyz"
## It works the same as this command : print(alphabbet[0 : 5])
s = slice(0 , 5)
print(alphabbet[s])
## It can also be applied to lists and tuples
list1= [1 , 2 , 3 ,4 , 5]
s = slice(0 , 5 , 2)
print(list1[s])

tuple1 = (6 , 7 , 8 , 9 , 10)
t = slice(0 , 5 , 3 )
print(tuple1[t])


# index() Function
# len() Function
# count() Function
# in Operator
# Concatenation and Repetition