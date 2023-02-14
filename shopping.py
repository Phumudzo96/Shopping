#Ask user to enter three products
product1 = input("Enter first product? ")
product2 = input("Enter second product? ")
product3 = input("Enter third product? ")

#Ask the user to enter the prices of the three products
price1 = float(input("Price for first product? "))
price2 = float(input("Price for second product? "))
price3 = float(input("Price for third product? "))

#add the prices of all the products
total = price1 + price2 + price3

#Get the avarage price of the products
avarage = total / 3

#Round off the avarage price of the product
avarage1 = round(avarage)

#Print the results
sentence = f"The Total of {product1}, {product2}, {product3} is R{total} and the average price of the items is R{avarage1}."
print(sentence)

