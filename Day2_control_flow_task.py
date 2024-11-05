# Read from the User
fav_flavour = "vanilla"  # Satoshi

# Shop
stock1 = "chocolate mint"
stock2 = "vanilla"
stock3 = "coffee"
stock4 = "green tea"

# Expected Output
# Yes, we have vanilla in stock

# Sorry, we ran out strawberry

#Task1.1
answer = input("What flavour do you want?:").lower()

if answer == stock1:
    print(f"Yes, we have {answer} in stock")
elif answer == stock2:
    print(f"Yes, we have {answer} in stock")
elif answer == stock3:
    print(f"Yes, we have {answer} in stock")
elif answer == stock4:
    print(f"Yes, we have {answer} in stock")
else:
    print(f"Sorry, we ran out {answer}")

#Task1.2
if (
    answer == stock1 
    or answer == stock2 
    or answer == stock3 
    or answer == stock4
    ):
    print(f"Yes, we have {answer} in stock")
else:
    print(f"Sorry, we ran out {answer}")


