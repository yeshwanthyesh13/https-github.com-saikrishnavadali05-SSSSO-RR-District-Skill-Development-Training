amount = int(input("Enter amount less than 100: "))  # Get amount

fifties = amount // 50      # Number of ₹50 notes
remainder = amount % 50     # Leftover after ₹50s
tens = remainder // 10      # Number of ₹10 coins

print("₹50 notes:", fifties)
print("₹10 coins:", tens)