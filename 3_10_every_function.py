#This project (3-10) is where I use every function I have learned in chapter 3 based on the fuctionality of lists

countries = ['england', 'wales', 'scotland', 'america', 'poland', 'germany', 'austria']
print(countries)


countries.insert(0, 'russia')
print(countries)

countries.append('ireland')
print(countries)

countries[1] = 'great britain'
print(countries)

print(len(countries))

del countries[8]
print(countries)

countries.remove('poland')
print(countries)

print(len(countries))

#countries.sort(reverse=True)
#print(countries)

print(sorted(countries))
print(countries)

countries.reverse()
print(countries)

countries.sort()
print(countries)

print(len(countries))

del countries [1]
print(countries)

countries.remove('russia')
print(countries)

print(len(countries))

popped_countries = countries.pop(1)

print(f"\nI've always wanted to vist {popped_countries.title()} as they have the best Classical Music.")

countries.append('india')
countries.append('new zeland')
print(countries)

num_countires = len(countries)

print(num_countires)

print(f"\n There are {num_countires} Countires which I want to vist in the next 10 years. ")

countries.remove('wales')
print(countries)

#varibles dont update further down the code so you have to redeclare if you have chanaged something in that list. (such as i asked for the length a couple lines up and it gave me 6 i then removed something from the list but it diddnt change the number you have to re delcare it further down the code to get it to update.)

num_countires = len(countries)

print(f"\n There are {num_countires} Countires which I want to vist in the next 10 years. ")