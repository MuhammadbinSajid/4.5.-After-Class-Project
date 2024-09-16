# Function to calculate power
def calculate_power(base, exponent):
    result = base ** exponent  # Using the exponentiation operator
    return result

# Input from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (n): "))

# Calculating power
power_result = calculate_power(base, exponent)

# Displaying the result
print(f"{base} raised to the power of {exponent} is {power_result}")
