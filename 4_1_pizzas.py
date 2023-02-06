# task 4-1 on for loops and it's based on pizza 

pizzas = ['pineapple', 'cheese', 'meat feast', 'bacon']
for pizza in pizzas:
	print(f"I really like {pizza.title()} Pizza.")

print("\nI Really Like pizza alot.")


#task 4-10 
print(f"The first 3 pizzas in this list are {pizzas[:3]}")

print(f"The middle 3 pizzas in this list are {pizzas[1:]}")

print(f"The last 3 pizzas in this list are {pizzas[-3:]}")

#task 4-11

friend_pizzas = pizzas[:]
friend_pizzas.append("chicken")

print(f"my favorite pizzas are")
for pizza in pizzas:
	print(pizza.title())

print(f"my favorite pizzas are")
for fav_pizza in friend_pizzas:
	print(f"my freinds facorite pizzas is {fav_pizza.title(//)}")