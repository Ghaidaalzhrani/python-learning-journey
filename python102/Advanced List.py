#2D_Lists
values = [[1 , 2 , 3] , True , "python"]
print(values[0][2])

data = [["Malak" , "Ghaida" , "Ali"] , [19 , 44 , 46] , ["Orthopedic Doctor" , "Student" , "Nurse"]]
print(data[0][0],data[1][2],data[2][2])


#Filter_Function : selects elements from a list that meet a specific condition.
ages = [21 , 19 , 5 , 20 , 11 , 7]
def filtered_ages(age):
    return age >= 18

print(list(filter(filtered_ages , ages)))


#Map_Function : : applies a function to each item in a list.
num = [21 , 19 , 5 , 20 , 11 , 7]
def square(num) :
    return num ** 2

print(list(map(square , num)))


#Sort_Function : sorts the items in a list in ascending order.
numbers =[100 , 345 , 6 , 54 , 222 , 87]
names = ["Zainab" , "Asmaa" , "Rola" , "Wasan"]
numbers.sort()
names.sort()
print(numbers)
print(names)

#OR **For sorting in reverse order**

numbers.sort(reverse=True)
names.sort(reverse=True)
print(numbers)
print(names)


#Reverse_Function
ai_tools = ["ChatGPT", "Claude", "Gemini", "Copilot", "Perplexity", "Midjourney", "DALL-E", "GitHub Copilot", "DeepSeek", "Grok"]
ai_tools.reverse()
print(ai_tools)

#List_Comprehension_Concept
num2 = [2 ,4 ,6 ,8 , 5]
double1 = [x * 2 for x in num2]
print(double1)
# **We can also add a condition.**
double2 = [x * 2 for x in num2 if x%2 == 0]
print(double2)
