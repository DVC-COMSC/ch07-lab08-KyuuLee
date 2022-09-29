# ******************************
# Make your Code
# ******************************
import random 

numbers = []
for i in range(10):
	numbers.append(random.randint(0,20))
print ("Before sorted\n", numbers)

insert_val = int(input("Enter one integer"))
#numbers = sorted(numbers)
numbers.sort()

print ("Before insertion\n", numbers)


for i in range(len(numbers)):
	if ( insert_val < numbers[i]):
		numbers.insert(i, insert_val)
		break
else:
	numbers.append(insert_val)

print ("After insertion\n", numbers)


