#Stages of Life

age = input('Enter your age : ') 

if int(age) < 2:
        print("You're a baby.")  

elif int(age) <= 4:
        print("You're a toddler.")

elif int(age) <= 14:
        print("You're a kid.")

elif int(age) <= 20:
        print("You're a teenager.")

elif int(age) < 65:
        print("You're an adult.")

else:
        print("You're an elder.") 
