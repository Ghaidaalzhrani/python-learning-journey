
#Cearet Functsion
def greet():
    name = input("please enter your name: ")
    time = input("please enter the time: ")
    print("Good " + time + ", " + name + "!")

#greet() 


#Function Call
#We can Call the functoin more than once in any place in a code


#Parameters
def numbers(num):
    for n in range(num):
        print(n)

#numbers(2)        
#numbers(6)  
#numbers(9)  


def sum(first_num , second_num):
    print(first_num + second_num )

#sum(49 , 18)   
 


def sum() :
   num1= input("enter first num :")
   int_num1=int(num1)
   num2= input("enter second num :")
   int_num2=int(num2)
   print(int_num1 + int_num2)      

#sum()


#output by using (return)
def sum(first_num , second_num):
    result = first_num + second_num
    return result

value = sum(10 , 5)
#print(value)


#Ability to call the function to more than one position

value = sum(4 , 6) * sum(3 , 2)
print(value)