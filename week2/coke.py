amt_due = 50
print("Amount Due:", amt_due)

while amt_due > 0:
    insert = int(input("Insert coin (5, 10, or 25 cents): "))
    
    #  to Check if the inserted coin is valid
    if insert in [5, 10, 25]:
        amt_due -= insert
        
        # If amount due is still positive, print it
        if amt_due > 0:
            print("Amount Due:", amt_due)
        # If amount due is zero or less, calculate and print change
        elif amt_due <= 0:
            print("Change Owed:", abs(amt_due))
    else:
        print("Invalid coin. Please insert a valid coin.")
