

#list
names=["ghaida" , "nado" , "dno"]
print(names)
print(type(names))

#index in list
names=["ghaida" , "nado" , "dno"]
print(names[0])

#change valuse in list
names[2]="rody"
print(names)

#add nwe value (append)
names=["Ghaida" , "Nado" , "Dno"]
names.append("Rudayna")
print(names)

#add nwe value in spisfic plase (insert)
names=["Ghaida" , "Nado" , "Dno"]
names.insert(1,"Rudayna")
print(names)

#remove value from list or remove all values
names=["Ghaida" , "Nado" , "Dno"]
names.remove("Dno")
print(names)

names=["Ghaida" , "Nado" , "Dno"]
names.clear()
print(names)

#-------------------------------
#tuples 
personsl_info=("ahmad" , "dammam" , "21-6-2004")
print(personsl_info)
print(type(personsl_info))

print(personsl_info[1])

#-------------------------------

#Dictionaries

#personsl_info=("ahmad" , "dammam" , "21-6-2004")

personsl_info={"name":"ahmad"  , "city":"dammam" , "birthDate":"21-6-2004"}
print(type(personsl_info))

#key in dict
print(personsl_info["birthDate"])
print(personsl_info.values())
print(personsl_info.keys())

#Delet values
del personsl_info["city"]
print(personsl_info)










