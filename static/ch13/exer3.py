class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaurant_name + " has wonderful and delicious " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is now open for business. Welcome foodies!"
        print("\n" + msg)

restaurant = Restaurant('Hambrunch', 'Hamburger lunch menus')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()