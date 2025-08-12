# Program to demonstrate List methods: Add, Append, Extend & Delete

# Take initial list input from user
my_list = input("Enter elements of the list separated by spaces: ").split()
print("\nInitial List:", my_list)

# Append method (adds single element at the end)
element_append = input("\nEnter an element to append: ")
my_list.append(element_append)
print("List after append:", my_list)

# Extend method (adds multiple elements at the end)
elements_extend = input("\nEnter multiple elements to extend the list separated by spaces: ").split()
my_list.extend(elements_extend)
print("List after extend:", my_list)

# Insert method (adds element at a specific index)
index_insert = int(input("\nEnter index to insert element: "))
element_insert = input("Enter element to insert: ")
if 0 <= index_insert <= len(my_list):
    my_list.insert(index_insert, element_insert)
else:
    print("Invalid index! Inserting at the end.")
    my_list.append(element_insert)
print("List after insert:", my_list)

# Delete method (by value)
element_delete = input("\nEnter element to delete: ")
if element_delete in my_list:
    my_list.remove(element_delete)
    print("List after deleting element:", my_list)
else:
    print("Element not found in list.")

# Delete method (by index)
index_delete = int(input("\nEnter index to delete element: "))
if 0 <= index_delete < len(my_list):
    del my_list[index_delete]
    print("List after deleting by index:", my_list)
else:
    print("Invalid index! No deletion performed.")
