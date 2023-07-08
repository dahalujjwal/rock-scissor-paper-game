"""


hint:

paper>rock
rock>scissor
scissor>paper


"""
import random

items=['r','p','s']

print("\n")
print("---------------------------------------------------------------------")
print("--->   Rock ✊, Paper ✋ and Scissor ✌ Game !!   <---")
print("---------------------------------------------------------------------")

uc=input("Do You Wanna to Play (y/n): ") #uc= your choice
print("\n")

if uc=='y':
    


    print("There are 5 Rounds...Best Of Luck !!")
    
    print("---------------------------------------------------------------------")
    print("--> Choose 'Rock' as 'r'  'Paper' as 'p'  and 'Scissor' as 's' <-- ")
    print("---------------------------------------------------------------------")
    
    print("""
    Win Point: 2
    Draw Point : 1
    """)
    print("---------------------------------------------------------------------")




    
    while uc!='n':
        
        
        if uc=='y':
            
            m=0  #computer point
            n=0   #your point

            for x in range(1,6):  #--> esle 5 patak loop chalaucha
                ch=random.choice(items)
                choose=input("--> ")
                c=choose
                

                if c=='r' and ch=='p':
                    print(" \t You Selected : Rock || Computer Selected : Paper so You Loose!!")
                    m+=2
                elif c=='r' and ch=='s':
                    print(" \t You Selected : Rock || Computer Selected : Scissor so You win!!")
                    n+=2
                elif c=='r' and ch=='r':
                    print(" \t You Selected : Rock || Computer Selected : Rock so Draw!!")
                    m+=1
                    n+=1
                    
                    


                elif c=='p' and ch=='s':
                    print(" \t You Selected : Paper || Computer Selected : Scissor so You Lose !!")
                    m+=2
                elif c=='p' and ch=='r':
                    print(" \t You Selected : Paper || Computer Selected : Rock so You Win!!")
                    n+=2
                elif c=='p' and ch=='p':
                    print(" \t You Selected : Paper || Computer Selected : Paper so Draw!!")
                    m+=1
                    n+=1
                    
                    
                    

                elif c=='s' and ch=='p':
                    print(" \t You Selected : Scissor || Computer Selected : Paper so You Win!!")
                    n+=2
                elif c=='s' and ch=='r':
                    print(" \t You Selected :Scissor || Computer Selected : Rock so You Loose!!")
                    m+=2
                elif c=='s' and ch=='s':
                    print(" \t You Selected : Scissor || Computer Selected : Scissor so Draw!!")
                    m+=1
                    n+=1
                
                else:
                    print(" \t Choose 'Rock' as 'r'  'Paper' as 'p'  and 'Scissor' as 's' ")

                

        
            print("---------------------------------------------------------------------")
            print(f""" \t  \t 
                GAME OVER !!

                Your Point : {n}
                Computer Point: {m}
                """)
            print("---------------------------------------------------------------------")
            if(m>n):
                print(" \t  \t  \t You Loose!!")

            elif(m<n):
                print(" \t  \t  \t You Win!!")
            else:
                print(" \t  \t  \t Draw!!")
            print("---------------------------------------------------------------------")  
           
       
        
        
        
        uc=input("Do You Wanna to Play Again (y/n): ") 

       
        

    
else:
    print("You Don't Want to Play This Game Sorry !!")