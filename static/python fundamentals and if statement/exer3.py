#Color Ball Game 3
ball_color = ('green') 
guess = input('Guess the color :')


if guess == ('green'):
    print(" You've earned 5 points, Very Good!")

elif guess == ('yellow'): 
    print("You've earned 10 points, Very Good!")

elif guess == ('red'):

    print("You've earned 15 points, Very good!")
else:

   print("Better luck next time")


print("Thanks for playing") 