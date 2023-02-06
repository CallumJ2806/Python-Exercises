places = ['dubai', 'america', 'london', 'vienna', 'berlin']
print(places)

print(sorted(places))

print("\n see the orginal list is still here")
print(places)


print("\n The orginal list is now in reverse order")
print(sorted(places, reverse=True))

print("\n see the orginal list is still here")
print(places)

#made the list into reverse order
places.reverse()
print(places)

#list back to orginal order
places.reverse()
print(places)

#making the list alphabetical order 
places.sort()
print(places)

#reversing the list in aplhabetical order
places.sort(reverse=True)
print(places)



