time = float(input("Enter the time in seconds:"))

days = time // (24*3600)
time %= (24*3600)

hours = time // 3600
time %= 3600

minutes = time // 60
time %= 60

seconds = time 
print ("D:HH:MM:SS --> %d: %d: %d: %d" % (days, hours , minutes , seconds))
