# You are helping a shopper manage their grocery shopping list. 
# Your task is to create a simple Python program that does the following steps in order:

# Initial Grocery List:
# Create a list with the initial items: ["milk", "bread", "eggs"].
# Add Item Function:
#   Write a function add_item(item) that adds a given item (string) to the grocery list.
# Remove Last Item Function:
#   Write a function remove_last_item() that removes the last item from the grocery list.
# Lambda Function for Display:
# Use a lambda function to print each item in the list with the format: "Item: <item>".
# Recursive Character Count (Bonus):
# Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. 
# For example, ["milk", "bread"] has 4 + 5 = 9 characters..

grocery_list=["milk","bread","eggs"]

def add_item(item):
    grocery_list.append(item)
    print(item,"is added to grocery list")
def remove_last_item():
    grocery_list.pop()
display_item=lambda item:print("Item: ",item)
def count_characters(items,index=0):
    if index == len(items):      
        return 0
    return len(items[index])+count_characters(items,index+1)

add_item("biscuit")
add_item("cupcake")
remove_last_item()
print("The updated grocery list")
for x in grocery_list:
   
    display_item(x)
print("The character count of items: ",count_characters(grocery_list))
