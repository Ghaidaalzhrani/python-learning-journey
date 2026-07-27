
majors={"Ai":["Math & logic " , "Smart systems" ,  "Machine learning" , "Data analysis"] , "CyberSecurity":["Information security" , "Vulnerability detection" , "Network security" , "Security investigation"] , "Computer Science":["programming" , "problem solving" , "Algorithms" , "Computer systems"] , "information system": ["Business technology" , "Business analysis" , "information management" , "technology & Business "]}

AI_counter=0
cyber_counter=0
cs_counter=0
cis_counter=0

hello="Hello! Today, we will explore the university major that suits you best. What is your name?"
U_name=input(hello)

for m in majors :
    for a in majors[m] :
     Qt=U_name+", Do you like "+ a +" ? Yes/No :"
     user_answer=input(Qt)

     while  user_answer!="Yes" and  user_answer!="No":
      print("please answer with Yes/No ")
      user_answer=input(Qt)

     if user_answer == "Yes" :
         if m == "Ai":
          AI_counter+=1 

         elif m == "CyberSecurity":
           cyber_counter+=1     

         elif m == "Computer Science":
           cs_counter+=1 

         elif m == "information system":
          cis_counter+=1         

if AI_counter > cyber_counter and  AI_counter  > cs_counter and  AI_counter > cis_counter:
   recommended_major = "Artificial Intelligence"

elif cyber_counter > AI_counter and cyber_counter > cs_counter and cyber_counter > cis_counter:
  recommended_major = "Cybersecurity"

elif cs_counter > AI_counter and cs_counter > cyber_counter and cs_counter > cis_counter :
  recommended_major ="Computer Science"

elif cis_counter > AI_counter and cis_counter > cyber_counter and cis_counter > cs_counter :
  recommended_major = "Information System"


else:
    recommended_major = "No clear recommendation"
    print("There is a tie between two or more majors.")


print("Your recommended major is : "+ recommended_major)          
