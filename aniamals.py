# task 3-4 guest list 
guestlist = ['sharon', 'karl', 'rosco']
invite = f'hello would you come to the party'
print(f"{invite} {guestlist[0].title()}")
print(f"{invite} {guestlist[1].title()}")
print(f"{invite} {guestlist[2].title()}")

# task 3-5 
print(guestlist[2])
guestlist.insert(2, 'lola')
reinvite = f"hello would you come to the party {guestlist[2].title()} as somone can't make it which means there is a spare space ?"
print(reinvite)