#Programme to converte kilometers into miles (from 140 Python exercises)

km = float(input("Enter distance in kilometers"))

#Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles = km*conversion_factor
print(f"Entered {km} kilometers is equal {miles} in miles")
