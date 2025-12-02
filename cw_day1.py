# A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
# The shop sold:
# 15.5 liters of apple juice
# 20 liters of orange juice
# 10.25 liters of grape juice
# Your task:
# Store the volume of each juice in separate variables.
# Calculate the total volume sold.
# Print the total volume.
# Convert the total volume to an integer and print it.
# Convert the total volume to a string and print it with a message.
# Add a random number between 5 and 10 (representing additional bonus liters) and print the final total


apple=15.5
orange=20
grape=10.25

total_volume=apple+orange+grape
print("Total Volume Sold : ", total_volume)

total_volume_int=int(total_volume)
print("Total Volume in Integer : ", total_volume_int)

total_volume_str=str(total_volume)
print(total_volume_str+" litres of juice are sold")

import random
bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("Final total with bonus:", final_total)
