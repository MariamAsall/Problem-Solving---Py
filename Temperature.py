temp = float(input("Enter temp in celsis :"))

if temp < -273.15:
    print("the temperature is invalid because it is below absolute zero")
elif temp ==  -273.15:
    print("the temperature is absolute 0.")
elif -273.15 < temp <0:
    print("the temperature is below freezing.")
elif temp == 0:
    print("the temperature is at the freezing point")
elif 0 < temp < 100:
    print("the temperature is in the normal range.")
elif temp == 100:
    print("The temperature is at the boiling point")
else: 
    print("the temperature is above the boiling point.")
