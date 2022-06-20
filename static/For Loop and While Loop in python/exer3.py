value = input("Enter a value: ")

type(int(value))

while value != "exit":
    if int(value)%10 == 0:
        print("Your value "+ value + " is a multiple of 10")
        value = input("Enter a value(type exit to quit):")
        if value == "exit":
            break
    else:
        print("Your value "+ value + " is not a multiple of 10")
        value = input("Enter a value(type exit to quit):")
        if value == "exit":
            break