from math import pi, tan  
s = float (input("Enter the length of sides:"))
n = int(input("Enter the number of sides: "))
area = (n * s ** 2) / 4*tan(pi/n)
print ("The  area = ", area)
