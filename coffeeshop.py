#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso      £2.50")
print(" > Americano     £3")
print(" > Latte         £2.50")
print(" > Cappuccino    £3")
print(" > Macchiato     £2.50")
print(" > Mocha         £3.50")
print(" > Flat White    £2.50")
print("----------------------------")

price = 0
#lager en funksjon for at den ikke skal fortsete etter det er invalid option.
def coffee_type():
   coffee = input("What type of coffee would you like?").title()
   if coffee=="Espresso":
      price = price + 2.50
   elif coffee=="Americano":
      price = price + 3
   elif coffee=="Latte":
      price = price + 2.50
   elif coffee=="Cappuccino":
      price = price + 3
   elif coffee=="Macchiato":
      price = price + 2.50
   elif coffee=="Mocha":
      price = price + 3.50
   elif coffee=="Flat White":
      price = price + 2.50
   else:
      print("Invalid option. Please select a type of coffee from the menu.")
      coffee_type()
coffee_type()

#velge hvor stor kafen skal være
def coffee_size():
   Size = input("What size of coffee would you like?")
   if Size=="M":
      price = price + 0
   elif Size=="L":
      price = price + 1
   elif Size=="XL":
      price = price + 1.50
   else:
      print("Invalid option. Please select a type of coffee from the menu.")
      coffee_size()
   coffee_size()

#hvor de vil være
def coffee_takeaway():
   place = input("Do you want take away?")
   if place=="No":
      price = price + 0
   elif place=="Yes":
      price = price + 1
   else:
      print("Invalid option. Please select a type of coffee from the menu.")
      coffee_takeaway()
   coffee_takeaway()

#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))