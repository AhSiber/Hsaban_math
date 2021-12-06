#!bin/python3.8.10 

# Import required modules

import math


# colors ! 
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'

help = F"""
{GREEN} Geometric {WHITE} and arithmetic{RED} follow-ups 🇮 🇷 🇦 🇳 {WHITE}

# 1 = Arithmetic sequences 
# 2 = Geometric sequence  
# 3 = Radius in Daryereh 
# 4 = Chinus 
# 5 = Square root 
# 6 = Return the absolute value of x.  

""" 
print(help) 

math_ = int(input('Enter number "Tools" : ')) 


if math_ == 1 : 
    try:
        # input  First account sequence number and Enter Number of sentences requested and Wad absolute magnitude  
        a = int(input('Enter First account sequence number : ‌'))
        d = int(input("Wad absolute magnitude : "))
        n = int(input('Enter Number of sentences requested : ') )
        # Calculation of input numbers ; 
        word_Split = n /2 
        word_2a = 2 * a 
        word_n_d = (n - 1 ) * d 
        # Calculation and output of work ; 
        new_1 = word_2a + word_n_d 
        print(f"answer : {word_Split * new_1}")
        # end 
    except : 
        print(f"value Error : Please enter the correct entry!")

elif math_ == 2 :
    try:
        # input  First account sequence number and Enter Number of sentences requested and Wad absolute magnitude   
        a = int(input('Enter First account sequence number :‌ '))
        q = int(input("Wad absolute magnitude : "))
        n = int(input('Enter Number of sentences requested : ') )
        # Calculate  ; 
        Qu_N = q ** n 
        Calc = Qu_N - 1  
        # Final Output [ Geometric sequence ] ; 
        print(f"answer : {a * Calc}")
        # end 
    except : 
        print(f"value Error : Please enter the correct entry! ")

elif math_ == 3 : 
    try: 
        # Input the number of points asked in the circle 
        p = int(input('Enter the number of dots : '))
        # Calculation of dots  
        P_Not_One = p -1 
        Calculate = P_Not_One * p 
        Tg = Calculate /  2 
        # Final Output [ Dots on the circle ] ; 
        print(f"answer : {Tg}")
        # end 
    except : 
        print(f"value Error : {p}")  

elif math_ == 4 : 
    try:
        # input Chinus 
        cosinoss = int(input('Enter your number [ Convert to cosine ] : '))
        # Convert number to cosine 
        print(F"answer : {math.cos(cosinoss)}")
        # end 
    except: 
        print(f"value Error : {cosinoss}")  

elif math_ == 5 : 
    try: 
        # input sqrt  
        user_  = int(input('Enter Square root [ number ]  : '))
        # Take the second input number  
        print(f"answer : {math.sqrt(user_)}") 
        # end 
    except: 
        print(f"value Error : {user_}")  

elif math_ == 6:
    try: 
        # Rturn the absolute value of x = > input 
        user_X = int(input('Enter number [ Return the absolute value ] : '))
        print(f"answer : {math.fabs(user_X)}")
    except : 
        print(f"value Error : {user_X}")  
