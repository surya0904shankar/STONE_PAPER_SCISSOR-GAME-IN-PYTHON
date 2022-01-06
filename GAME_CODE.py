print("you need 5 points to win")
score_user=0
score_comp=0
while score_user!=5 and score_comp!=5:
    k=["stone","paper","scissor"]
    import random as s
    g=s.choice(k)
    w=input("enter choice: stone,paper or scissor").lower() 
    if g==w:
        print("computer's choice",g)
        print("no points both are same")
        print() 
        
    elif w=="stone" and g=="scissor":
       score_user+=1
       print("computer's choice",g)
       print("you win a point")
       print("your score:",score_user,"computer's score:",score_comp)
       print()
       
    elif w=="scissor" and g=="paper" :
       score_user+=1
       print("computer's choice",g)
       print("you win a point")
       print("your score:",score_user,"computer's score:",score_comp)
       print()
       
    elif w=="paper" and g=="stone":
       score_user+=1
       print("computer's choice",g)
       print("you win a point")
       print("your score:",score_user,"computer's score:",score_comp)
       print() 

    elif g=="stone" and w=="scissor":
       score_comp+=1
       print("computer's choice",g)
       print("computer wins a point")
       print("your score:",score_user,"computer's score:",score_comp) 
       print() 

    elif g=="scissor" and w=="paper" :
        score_comp+=1
        print("computer's choice",g) 
        print("computer wins a point")
        print("your score:",score_user,"computer's score:",score_comp) 
        print()
    elif g=="paper" and w=="stone":
        score_comp+=1
        print("computer's choice",g)
        print("computer wins a point")
        print("your score:",score_user,"computer's score:",score_comp)
        print()
        
    else:
        print("invalid choice")
if score_user > score_comp:
    print("great you won the match")
elif  score_user < score_comp:
    print("sorry you lost  the match")



