cos_quan = input("How many people are in your group?")

if (cos_quan) >= ('10'):
    while cos_quan > ('10'):

        message = ("Sorry, there is no table for " + cos_quan +  " people, Please wait")
        print(message)

        exit = input("Type 'exit' to quit. ")

        if exit == 'exit':
            break   
        else: 
            continue
        
            
if (cos_quan) == ('10'):
    message = ("Come with me ma'am/sir there is a table for "+ cos_quan + " people")
    print(message)

else:
    print("Thank you for using my program")
    