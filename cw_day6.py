# You are working on a simple attendance tracking system for a 5-day workshop. You have a list of the number of students present each day:
# attendance = [18, 20, 19, 15, 21]
# Your tasks are:
# Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
# Count how many days the class was full.
# Calculate and print the total attendance for all 5 days.


attendance=[18,20,19,15,21]
Full=0
Not_Full=0 
Total=0
for x in attendance:
    if x >=20:
        print("Full")
        Full=Full+1
    else:
        print("Not Full")
        Not_Full=Not_Full+1
    Total=Total+x
print(Full," days the class is Full")
print(Not_Full," days the class is not full")
print("The total attendence for all 5 days is ",Total)
