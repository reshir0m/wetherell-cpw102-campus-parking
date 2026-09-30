# Named constant 
# using 2.0 as it's value, automaically storing as a float in program 
COST_PER_HOUR = 2.0

# Processing of program
def calculated_estimated_parking_cost(parked_hours):
    estimated_cost = parked_hours * COST_PER_HOUR
    return estimated_cost


# Define the main logic of program
def main():

    # Create a variable in which I will store user-entered parked hours
    # variable is a named space in memory

    parked_hours = float(input("How many hours will you be / have you parked?"))

    # Call function
    cost = calculated_estimated_parking_cost(parked_hours)

    # Output
    print(cost)

# Call main function and execute logic of program
main()