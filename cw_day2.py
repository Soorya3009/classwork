# You work for a bookstore that generates receipts for customers. Your task is to prepare a simple receipt using string techniques.
# Here’s what you need to do:
# Create a multiline string to store the receipt header.
# The customer bought 2 items:
# Book Title: "Python Basics" – ₹450
# Book Title: "Data Science Intro" – ₹600
# For each line showing the book and price, use a single string with basic {} placeholders and call format() once to fill in the values.
# Calculate the total price and add it similarly.
# Concatenate a thank-you message at the end.
# Make sure the output uses newline (\n) and tab (\t) for readability.
# Display the entire receipt in uppercase.


header = "BOOK WORLD RECEIPT\n---------------------\nCUSTOMER PURCHASE DETAILS:\n"


book1_title = "Python Basics"
book1_price = 450
book2_title = "Data Science Intro"
book2_price = 600


line1 = "\tBOOK: {} \t PRICE: Rs {}".format(book1_title, book1_price)
line2 = "\tBOOK: {} \t PRICE: Rs {}".format(book2_title, book2_price)


total = book1_price + book2_price
total_line = "\n\n\tTOTAL AMOUNT: Rs {}".format(total)


thank_you = "\n\nTHANK YOU FOR SHOPPING WITH US!"


receipt = header + line1 + "\n" + line2 + total_line + thank_you


print(receipt.upper())


