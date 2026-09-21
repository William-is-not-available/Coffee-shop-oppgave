#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
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

#velge hvor stor kafen skal være
Size = input("What size of coffee would you like?")
if Size=="M":
   price = price + 0
elif Size=="L":
   price = price + 1
elif Size=="XL":
   price = price + 1.50

#hvor de vil være
place = input("Do you want take away?")
if place=="No":
   price = price + 0
elif place=="Yes":
   price = price + 1

#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))