class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.restaurant_name + " has wonderful and delicious " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.restaurant_name + " is now open for business. Welcome foodies!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        
        
restaurant = Restaurant('Hambrunch', 'Hamburger lunch menus')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 100

restaurant.open_restaurant()

print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 100