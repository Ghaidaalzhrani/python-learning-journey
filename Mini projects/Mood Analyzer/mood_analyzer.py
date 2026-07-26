

positive_words=["happy" , "excited" , "joyful" , "optimistic", "relaxed" , "confident" , "cheerful" , "delighted" , "calm" , "energetic"]
negative_words=["sad" , "angry" , "stressed" ,"bored" , "frustrated" , "anxious" , "tired" , "disappointed" , "miserable"]

while True:
 user_answer=input("what do you feel today?").lower()
 user_answer=user_answer.replace(" ' " , "")
 user_answer=user_answer.replace("," , "")
 user_answer=user_answer.replace("." , "")

 if user_answer =="exit" :
    break


 positive_score=0

 for p in positive_words:
    if p in user_answer:
        positive_score+=1



 negative_score=0

 for n in negative_words:
    if n in user_answer:
        negative_score+=1


 if  positive_score > negative_score:
    print("your mood is good !")

 elif  positive_score < negative_score:
    print("oh sorry , tomorrow will be okay")


 else:
    print("wrong messege")

