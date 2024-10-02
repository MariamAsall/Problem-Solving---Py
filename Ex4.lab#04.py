items = int(input("Enter the number of items :"))
cost  = 0

if items < 10:
    cost =  12 * items
elif 10 < items < 99:
    cost = 10* items
else :
    cost = 7* items 
print ("The total cost is :", cost )