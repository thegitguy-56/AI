# Program to demonstrate List operations with user input

# Taking user input for nested list
nested_list = []
n = int(input("Enter number of sublists: "))
for i in range(n):
    sublist = input(f"Enter elements of sublist {i+1} separated by spaces: ").split()
    nested_list.append(sublist)
print("\nNested List:", nested_list)

# Length of the list
print("Length of nested list:", len(nested_list))

# Concatenation of two lists
list1 = input("\nEnter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()
concat_list = list1 + list2
print("Concatenated List:", concat_list)

# Membership test
element = input("\nEnter element to check membership in list1: ")
print(f"Is '{element}' in list1?", element in list1)

# Iteration over a list
print("\nElements in list2:")
for item in list2:
    print(item)

# Indexing
index = int(input("\nEnter index to access in list1: "))
if -len(list1) <= index < len(list1):
    print(f"Element at index {index} in list1:", list1[index])
else:
    print("Invalid index!")

# Slicing
start = int(input("\nEnter start index for slicing list1: "))
end = int(input("Enter end index for slicing list1: "))
print("Sliced portion of list1:", list1[start:end])
