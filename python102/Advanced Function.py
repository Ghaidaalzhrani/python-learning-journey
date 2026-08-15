#Positional Arguments : Passing arguments to a function based on their order
def info(name , work) :
    print("my name is ",name,"and im a ",work,"now")

info("Ghaida" , "Student")    
info("Student" , "Ghaida")    


#Keyword Arguments : Passing arguments to a function using the parameter names
def greet(name , hello) :
    print(hello,",",name)

greet(name ="Khalid" , hello ="Hi!" )   


#Default Parameter :  Giving a parameter a default value if no value is provided
def Ticket(Country , Airline="flynas") :
    print("Destination:",Country,"on", Airline)

Ticket("North Africa")   
Ticket("Japan" , "Saudi Airline")   

#Argument Packing : Collecting multiple arguments into a tuple using
def avg(*num) :
    total = sum(num)
    leng = len(num)
    average = total / leng

    print(average)

avg(40 , 9 , 33 , 20 , 7)    

#Argument Unpacking : Unpacking a list or tuple into separate arguments using
def info(S1 , S2 ,  S3) :
    print ("First Student's name :" , S1)
    print ("Second Student's name :" , S2)
    print ("Third Student's name :" , S3)

names = ("Turki" , "Azaam" , "Hamzah")

# info(names[0] , names[1] , names[2]) : This take the long way.

info(*names)


#Using Packing and Unpacking : Using * to pack or unpack multiple arguments
def alpha(*Letters) : #Here, all the elements were called as if they were part of a single element, which is the list.
    print(Letters)

Letters = ["A" , "B" , "C" ,"D" ,"E" , "F" , "G"]
alpha(Letters) #The elements are printed as a single element, which is the list.
alpha(*Letters) #Here, we use the `*` symbol so that each element in the list is received as a separate element.


#Dictionary Packing :  Collecting keyword arguments into a dictionary using **kwargs
def info(**kwargs) :
    print(kwargs)
    print(type(kwargs))
    #OR
    print("My name is",kwargs["name"],"and im", kwargs["age"] ,"years old , and im" ,kwargs["major"] ,"student")

info(name="Ghaida" , age="19" , major="Ai")    
#info("Ghaida" ,19" ,"Ai") : The function does not accept positional arguments because we used dictionary unpacking, so the function expects us to pass specific arguments.

#Dictionary Unpacking : Unpacking a dictionary into keyword arguments using **
def info1 (name1 , age1 , major1) :
    print("My name is",name1, "and i am",age1,"years old , and i am",major1,"student")

d = {"name1" : "Ghaida" , "age1" : 19 , "major1" : "Ai"}
info1(**d)
