def inArray(pick,arraylist):
    index = 0
    for element in arraylist:
        if pick == element:
            return index
        index = index + 1
    return - 1

def carPrice(index):
    priceArray = ["25,000", "30,000", "20,000", "50,000", "35,000", "40,000"]
    return priceArray[index]


print("Hello, Welcome to Michaels Used Cars, what are you looking for?")

print("please pick between Type, Color, and Brand")

carType = ["Sedan", "Pickup", "Coupe", "Sports Car", "Minivan", "Hybrid"]
carColor = ["White", "Black", "Red", "Blue", "Yellow", "Green", "Brown"]


print("When you have the car you want please type checkout and your total will come up")

print(carType)
ctpick = input("Please input what car type do you desire")
while inArray(ctpick, carType) < 0:
    print("You didnt input an available car type")
    print(carType)
    ctpick = input("Please input a choice from above")

print(carColor)
ccpick = input("Please input desired color of car")
while inArray(ccpick, carColor) < 0:
    print("You didnt inout an available car color")
    print(carColor)
    ccpick = input("Please input a color from the list above")


index = inArray(ctpick, carType)
price = carPrice(index)
   
print("You have chosen a", ctpick, "in the color", ccpick)
leaveChoice = input("Would you like to check out with your current choices if so type checkout")

if leaveChoice == "checkout":
    print("the price for your", ctpick, "in", ccpick, "comes out to", price)
    print("Thank you for your patronage at Michaels Used Cars!")












    
