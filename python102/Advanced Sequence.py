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

#index() function (Searching for an element in a sequence)
text = "Im a future engineer"
the_list = [10 , 9 , 8 , 7 , 6 , 5]
the_tuple = (4 , 3 ,2 , 1 ,0)

print(text.index("engineer"))
print(the_list.index(7))
print(the_tuple.index(2))


# len() Function()
text1 = "Im a future engineer"
the_list1 = [10 , 9 , 8 , 7 , 6 , 5]
the_tuple2 = (4 , 3 ,2 , 1 ,0)

print(len(text1))
print(len(the_list1 ))
print(len(the_tuple2))


# count() Function
string1 = "Python is a powerful programming language, and learning Python can make programming easier,faster, and more enjoyable. I love Python because Python helps me solve problems and build intelligent applications with Python."
l = [6,6,6,6,6,6,7,7,7,7,7,7,7,7]
t = (0,5,9,8,7,5)

print(string1.count("Python"))
print(l.count(6))
print(t.count(5))


# in Operator
text3 = "Artificial Intelligence helps engineers analyze data, build machine learning models, and develop intelligent systems using Python and cloud technologies."
print("Intelligence" in text3)
print("machine learning" in text3)
print("Data" in text3)

models = ("FNN", "CNN", "RNN", "LSTM")
print("CNN" in models)
print("ANN" in models)

neurons = [16, 32, 64, 128, 256, 512]
print(512 in neurons)
print(1024 in neurons)


# Concatenation and Repetition
#NOTE : Add a space at the beginning of the text to prevent the texts from merging.

ftrst_name = " Ghaida"
second_name = " Alzahrani"
print(ftrst_name+second_name )
#Repetition
print(ftrst_name*5)

l1= [1 , 2 , 3 , 4 , 5 ,]
l2 =[ 6 , 7 , 8 , 9 ]

print(l1+l2)
