import math
import random


possibility_1=0
possibility_2=0

while True:
    list = [0, 1]
    number_1=random.choice(list)
    number_2=random.choice(list)
    number_3=random.choice(list)
    
    number_total=str(number_1)+","+str(number_2)+","+str(number_3)
    
    if number_total=="1,1,0" or number_total=="0,0,1":
        possibility_1 +=1

    if number_total=="1,1,1" or number_total=="0,0,0":
        possibility_2 +=1   

    print(str(number_total)+"      possibility_1= "+ str(possibility_1)+" possibility_2= "+ str(possibility_2) +"    "+str(possibility_1/possibility_2)+"   Possibilities Total:" + str(possibility_1+possibility_2))   

