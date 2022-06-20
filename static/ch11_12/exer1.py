filename = 'static/ch11_12/guest_book.csv'

print("Hello, please enter quit if you're done")
while True:
    name = input("\nMay I ask for your Name?")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hello there " + name + ", you've been added to the guest book. Please be sitted")
