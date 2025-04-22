def main():
    # Create a list of numbers from 1 to 10
    numbers = list(range(1, 11))
    
    # Extract the first five elements
    first_five = numbers[:5]
    
    # Reverse the extracted elements
    reversed_first_five = first_five[::-1]
    
    # Print both lists
    print("Original list:", numbers)
    print("Extracted first five elements:", first_five)
    print("Reversed extracted elements:", reversed_first_five)

if __name__ == "__main__":
    main()