# task 3-4 guest list 
guestlist = ['sharon', 'karl', 'rosco']
invite = f'Hello would you come to the party'
print(f"{invite} {guestlist[0].title()}")
print(f"{invite} {guestlist[1].title()}")
print(f"{invite} {guestlist[2].title()}")

# task 3-5 
print(guestlist[2])
guestlist.insert(2, 'lola')
reinvite = f"Hello would you come to the party {guestlist[2].title()} as somone can't make it which means there is a spare space ?"
print(reinvite)

print(f"Good evening {guestlist[0]}, {guestlist[1]} and {guestlist[2]} we have found a bigger table so we will be inviting more guests.")


#task 3-6 more guests 
guestlist.insert(0, 'donald')
guestlist.insert(2, 'carol')
guestlist.insert(6, 'lottie')

print(f"{invite} {guestlist[0].title()}")
print(f"{invite} {guestlist[1].title()}")
print(f"{invite} {guestlist[2].title()}")
print(f"{invite} {guestlist[3].title()}")
print(f"{invite} {guestlist[4].title()}")
print(f"{invite} {guestlist[5].title()}")
print(f"{invite} {guestlist[6].title()}")

#task 3-7 shrinking the guests lists 
print("There are now two spaces avalible as two guests cant make it tonight due to fmaily issues")
# need to figure out how to .pop multiple items at once instead of keep writing the code as the list changes also how to get both names in the same popped_guestlist varible.
popped_guestlist = guestlist.pop(0)
popped_guestlist2 = guestlist.pop(0)
print(guestlist)
print(f"we are sorry you cant make it {popped_guestlist.title()} and {popped_guestlist2.title()}")

print(guestlist)
del guestlist [0]
del guestlist [2]
print(guestlist)

num_guests = len(guestlist)

print(f"There are now {num_guests} guests attending the meal tonight at 7pm. ")
