#exercise One:
def reverse_and_concatenate(s, i):
    if i == 0:
        return ['']
    else:
        reverse = s[::-1]
        concatenation = reverse *(i)
        return concatenation

text = input("Enter the text to be concatenated: ")
number = int(input("Enter the number of concatenation: "))
answer = reverse_and_concatenate(s=text,i=number)
print(answer)

#exercise Two:
def Upper_then_lower(s):
    upper = []
    lower = []
    for char in s:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)
    new_string = ''.join(upper+lower)
    return new_string
string = input("Enter a string: ")
answer = Upper_then_lower(s=string)
print(answer)

#exercise Three:
def sorted_string(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
sorting = sorted_string(s1=string1,s2=string2)
print(sorting)

#exercise Four:
def max_and_min(list):
    maximum_num = 0
    maximum_num_index = 0
    minimum_num = 1000
    minimum_num_index = 0
    for i in range(len(list)):
        if list[i] > maximum_num:
            maximum_num = list[i]
            maximum_num_index = i
        if list[i] < minimum_num:
            minimum_num = list[i]
            minimum_num_index = i

    return maximum_num, maximum_num_index, minimum_num, minimum_num_index

list1 = [5,4,8,9,12,11,1.5,33,65,48,2,7,166]
maximum, maximum_index, minimum, minimum_index = max_and_min(list=list1)
print(f"Max:{maximum},Min:{minimum},MaxIndex:{maximum_index},MinIndex:{minimum_index}")

#exercise Five:
def count_digits(n):
    """counts the number of digits of a number recursively"""
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

number = int(input("enter a number: "))
digit_count = count_digits(n=number)
print(f"The number {number} has {digit_count} digits.")

#exercise Six:
def list_jumps(jumps):
    starter = 0
    x = len(jumps)
    for _ in range(x):
        if starter < 0 or starter >= x:
            return "out of bounds"

        jump = jumps[starter]
        jumps[starter] = 0
        starter += jump

    if starter == 0:
        return "cycle"
    else:
        return "out of bounds"

jumps1 = [0,-1,1,-2]
print(list_jumps(jumps1))
jumps2 = [4,-4,2,2]
print(list_jumps(jumps2))

#exercise Seven: POS system
products = {
    "123": {"name": "Banana", "price": 1},
    "124": {"name": "apple", "price": 1},
    "125": {"name": "watermelon", "price": 7},
    "126": {"name": "peach", "price": 1.5},
    "127": {"name": "pineapple", "price": 5},
    "128": {"name": "egg", "price": 1},
    "129": {"name": "tomato", "price": 0.75},
    "130": {"name": "potato", "price": 1},
    "131": {"name": "lettuce", "price": 1.75},
    "132": {"name": "onion", "price": 0.5},
    "133": {"name": "cucumber", "price": 1.5},
    "134": {"name": "coconut", "price": 4},
    "135": {"name": "bread", "price": 1.25},
    "136": {"name": "mango", "price": 3.5},
    "137": {"name": "avocado", "price": 2.5},
}

def POS():
    print("Welcome to my store guys!")

    while True:
        receipt = []
        price_total = 0
        starter = input('Do you want to start a new receipt? (yes or no): ')
        if starter.lower() != 'yes':
            print('Thank you for using our POS!')
            break

        receipt, price_total = adding_products(receipt, price_total)
        transaction(receipt, price_total)

def adding_products(receipt, price_total):
    while True:
        barcode = input("Scan barcode, or enter 'stop' to finish: ")
        if barcode.lower() == "stop":
            break
        if barcode in products:
            quantity = int(input("Enter the quantity you want to purchase: "))
            product = products[barcode]
            receipt.append({"name": product["name"], "price": product["price"], "quantity": quantity})
            print(f"{quantity} '{product['name']}' was added to the receipt.")
            price_total += product["price"] * quantity
        else:
            print("Sorry, product was not found")

    return receipt, price_total

def transaction(receipt, price_total):
    complete = input("Do you want to complete the purchase? ")
    if complete.lower() == 'yes':
        print("Your receipt is: ")
        for product in receipt:
            print(f"{product['name']} - Quantity: {product['quantity']} - Price: {product['price']}$")
        print()
        print(f"Your total price is: {price_total}$")
        print("Thank you for shopping!")
        print()
POS()

