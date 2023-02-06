# BASIC LIST FEATURES EXAMPLES	

#declaring a list 
motocycles = ['honda', 'yamaha']
print(motocycles)


#how to change a element in a list
motocycles[0] = 'ducati'
print(motocycles)


#adding elements to the list using append 
motocycles.append('suzuki')
print(motocycles[-1])


#using insert to add a new element in the list at any position
motocycles.insert(1, 'china')
print(motocycles)


#using del to remove yamaha from the list 
del motocycles[2]
print(motocycles)


#series append starting with an empty list for example this is good for using it tp input users data
moto = []
moto.append('suzuki')
moto.append('honda')
moto.append('yamaha')
print(moto)


#using pop to remove an element then reselect the value after its been removed you can use a number in the parathese to select which element in the list
print(motocycles)

popped_motorcycles = motocycles.pop(1)
print(motocycles)
print(popped_motorcycles)

#using remove to delete from list but declaring it as a new variable

too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is to expensive for me.")