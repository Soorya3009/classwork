# You are helping a small stationery shop owner manage a simple list of items.
# First, ask the user to enter the name of a new item.
# If the file items.txt does not exist, create it and write the item into it.
# If the file exists, open it in append mode and add the new item.
# After writing, display the full list of items from the file to the user


item = input("Enter the name of a new stationery item: ")

try:

    with open("items.txt", "a") as file:
        file.write(item + "\n")

    print("\nCurrent list of stationery items:")
    with open("items.txt", "r") as file:
        for line in file:
            print("-", line.strip())

except Exception as e:
    print("An error occurred:", e)
