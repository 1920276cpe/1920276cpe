

print("Welcome To NetmaX !")

age = input('Please enter your age (type quit to exit):  ') 
 


while age != 'quit':
    

    if int(age) <= 3:
            print("Your ticket is free")  
            break
    elif int(age) <= 12:
            print("Your ticket is 10 pesos")
            break
    elif int(age) < 12:
            print("Your ticket is 15 pesos")
            break
    elif int(age) < 100:
            print("Your ticket is 15 pesos")
            break

    else:
        print("Invalid.")
        break 

print("Thank you, Enjoy the movie.")
    
