Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#CS 175
#Aidan Mazzola
#Restaurants Version 2

def getanswer(cancel):
    answer = input(f'Is anyone in your party{cancel}?')
    if answer.lower() == 'yes':
        return True
    
    else:
        return False
running = True
while running:
    print('Respond using "yes" or "no" .\n')
    vegetarian=input("Is anyone in your party a vegetarian? ")
    vegan=input("Is anyone in your party a vegan? ")
...     gluten_free=input("Is anyone in your party gluten-free? ")
...     print("Here are your restaurant choices:")
...     if vegetarian=="yes" and vegan=="yes" and gluten_free=="yes":
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     elif vegetarian=="yes" and vegan=="yes" and gluten_free=="no":
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     elif vegetarian=="yes" and vegan=="no" and gluten_free=="yes":
...         print("Main Street Pizza Company")
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     elif vegetarian=="no" and vegan=="yes" and gluten_free=="yes":
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     elif vegetarian=="no" and vegan=="no" and gluten_free=="yes":
...         print("Main Street Pizza Company")
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     elif vegetarian=="yes" and vegan=="no" and gluten_free=="no":
...         print("Main Street Pizza Company")
...         print("Corner Cafe")
...         print("Mama's Fine Italian")
...         print("The Chef's Kitchen")
...     elif vegetarian=="no" and vegan=="yes" and gluten_free=="no":
...         print("Corner Cafe")
...         print("The Chef's Kitchen")
...     else:
...         print("Joe's Gourmet Burgers")
...         print("Main Street Pizza Company")
...         print("Corner Cafe")
...         print("Mama's Fine Italian")
...         print("The Chef's Kitchen")
... 
...     answer= input('\nWould you like to search again?')
...     if answer.lower() == "no":
...         print('Goodbye!')
...         running = False
...     else:
