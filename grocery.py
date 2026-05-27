#Emilio

items = [
    "Milk", "Eggs", "Bread", "Butter", "Cheese",
    "Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Sausage",
    "Pasta", "Rice", "Quinoa", "Cereal", "Oatmeal",
    "Apples", "Bananas", "Oranges", "Strawberries", "Blueberries",
    "Grapes", "Pineapple", "Mangoes", "Lemons", "Limes",
    "Potatoes", "Onions", "Garlic", "Carrots", "Broccoli",
    "Cauliflower", "Spinach", "Kale", "Lettuce", "Bell Peppers",
    "Tomatoes", "Cucumbers", "Zucchini", "Mushrooms", "Avocados",
    "Olive Oil", "Vegetable Oil", "Cooking Spray", "Salt", "Pepper",
    "Sugar", "Brown Sugar", "Flour", "Baking Powder", "Baking Soda",
    "Peanut Butter", "Jelly", "Honey", "Maple Syrup", "Nutella",
    "Coffee", "Tea", "Hot Chocolate", "Creamer", "Sugar Packets",
    "Orange Juice", "Apple Juice", "Soda", "Sparkling Water", "Sports Drink",
    "Chips", "Crackers", "Pretzels", "Popcorn", "Cookies",
    "Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Frozen Chicken Nuggets", "Frozen Waffles",
    "Canned Soup", "Canned Beans", "Canned Corn", "Canned Tomatoes", "Canned Tuna",
    "Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Hot Sauce",
    "Paper Towels", "Toilet Paper", "Facial Tissues", "Dish Soap", "Laundry Detergent"
]
prices = [
    3.49, 2.99, 2.79, 3.99, 4.59,
    7.99, 6.49, 5.99, 4.99, 4.49,
    1.79, 4.29, 5.99, 3.99, 3.49,
    4.49, 1.39, 3.99, 4.99, 5.49,
    5.49, 3.49, 4.99, 1.79, 1.79,
    3.99, 2.49, 1.29, 2.29, 2.99,
    3.49, 3.49, 3.99, 2.49, 3.49,
    2.99, 1.79, 2.49, 2.99, 1.99,
    7.99, 5.49, 3.99, 1.29, 2.49,
    2.49, 2.99, 3.49, 2.49, 1.99,
    3.99, 3.29, 4.99, 6.99, 5.49,
    9.99, 4.49, 3.99, 2.49, 1.99,
    4.29, 3.99, 1.99, 2.49, 2.99,
    3.99, 3.49, 2.99, 2.49, 4.99,
    5.99, 6.49, 2.99, 7.49, 4.99,
    2.79, 1.49, 1.29, 1.79, 2.49,
    2.99, 2.49, 4.49, 3.49, 3.99,
    8.99, 12.99, 3.99, 2.99, 11.99
]

#Functions
#Take a grocery item and prints or RETURNS the price
def price_check(item_name):
    item_name = item_name.lower()
    for i in range(len(items)):
        if items[i].lower() == item_name:
            return prices[i] # return price
    return "Item not found"

def discount_calculations(coupon):
    for i in range(len(prices)):
        prices[i] = round(prices[i] * (1 - coupon), 2)

def discount(sale):
    print("Prices Before Discount:")
    print(prices)
    discount_calculations(sale)
    print("")
    print("Prices After Discount:")
    print(prices)

def budget(amount):
    affordable = [] # list to store items within budget
    for i in range(len(items)):
        if prices[i] <= amount:
            affordable.append(items[i])
            print(items[i], "- $", prices[i])
    return affordable

def checkout(cart):
    total = 0
    for item in cart:
        price = price_check(item)
        total = total + price
    return round(total, 2)

# Main
discount(.20)
print(" ")
print(f"Price Check: ${price_check("Ice Cream")}")
print(" ")
budget(2)
print(" ")
customer_items = ["Frozen Waffles", "Coffee", "Sugar", "Maple Syrup", "Butter"]
total_price = checkout(customer_items)
print(f"Customer total: ${total_price}")
