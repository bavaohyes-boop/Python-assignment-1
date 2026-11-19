# Sample data provided in the assignment
marks_list = [78, 35, 92, 48, 61]

# 1. Create a list containing five student marks and convert it into a tuple.
marks_tuple = tuple(marks_list)

# 2. Display both collections and their data types.
print("List:", marks_list, "| Type:", type(marks_list))
print("Tuple:", marks_tuple, "| Type:", type(marks_tuple))

# 3. Find and display the highest and lowest marks using appropriate built-in operations.
highest_mark = max(marks_list)
lowest_mark = min(marks_list)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)

# 4. Count how many students scored at least 40 marks.
# Without using loops or functions as per instructions, we evaluate conditions manually or count occurrences:
# Checking each element manually based on index:
count_at_least_40 = (
    (marks_list[0] >= 40) + 
    (marks_list[1] >= 40) + 
    (marks_list[2] >= 40) + 
    (marks_list[3] >= 40) + 
    (marks_list[4] >= 40)
)
print("Students scoring at least 40:", count_at_least_40)

# 5. Check whether all marks are within the valid range of 0 to 100 and display the Boolean result.
all_valid_range = (
    (0 <= marks_list[0] <= 100) and
    (0 <= marks_list[1] <= 100) and
    (0 <= marks_list[2] <= 100) and
    (0 <= marks_list[3] <= 100) and
    (0 <= marks_list[4] <= 100)
)
print("All marks within valid range (0-100):", all_valid_range)

# 6. Try changing one element in the list and one element in the tuple. 
# Observation comment:
# Lists are mutable, so modifying an element directly (e.g., marks_list[0] = 80) works successfully.
# Tuples are immutable, so attempting to modify an element (e.g., marks_tuple[0] = 80) 
# raises a TypeError: 'tuple' object does not support item assignment.
