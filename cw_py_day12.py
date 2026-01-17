# Create a program for a mini library system that asks the user to enter a book title and publication year.
# If the book title contains only alphabets and spaces, accept it. Otherwise, show an error.
# The publication year must be a 4-digit number starting with “19” or “20”. If not, display an error.
# Use appropriate error handling to catch any invalid inputs and ensure a message is printed at the end whether or not there was an error.

try:
   
    title = input("Enter book title: ")

   
    if not title.replace(" ", "").isalpha():
        raise ValueError("Error: Book title must contain only alphabets and spaces.")


    year = input("Enter publication year: ")


    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Publication year must be a 4-digit number starting with 19 or 20.")


    print("\nBook details accepted successfully!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

except Exception:
    print("An unexpected error occurred.")

finally:
    print("\nThank you for using the mini library system.")
