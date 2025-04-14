def binary_divisible_by_5(binary_numbers):
    # Split input into a list
    binary_list = binary_numbers.split(',')

    # Filter numbers that are divisible by 5 using direct binary-to-decimal conversion
   divisible_by_5 = [num for num in binary_list if int(num, 2) % 5 == 0]
   
   

    # Print the result as a comma-separated sequence
    print(','.join(divisible_by_5))

# Example usage
binary_input = input("Enter comma-separated binary numbers: ")
binary_divisible_by_5(binary_input)



