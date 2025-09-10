# define a list

shopping_list = ["rocket", "apple", "carrot", "mango"]

print(f"I have {len(shopping_list)} items to purchase")

print("These items are: ")

for item in shopping_list:
    print(item, end=" ")

print("\nI also have to buy rice.")

# push data into list
shopping_list.append("rice")

print(
    f"With rice, the shopping list is: {shopping_list}"
)  # ['apple', 'carrot', 'mango', 'rice']

# sort list
shopping_list.sort()

print(shopping_list)  # ['apple', 'carrot', 'mango', 'rice', 'rocket']

# delete from list

del shopping_list[0]

print(shopping_list)  # ['carrot', 'mango', 'rice', 'rocket']
