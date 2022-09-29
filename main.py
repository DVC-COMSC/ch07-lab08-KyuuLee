
numbers = list(map(int, input('Enter 5 numbers in ascending order').split()))
# print (numbers)
insval = int(input('Enter the insertion value'))

i = 0
while ( i < len(numbers)):
	if (insval < numbers[i]):
		numbers.insert(i, insval)
		break
	i += 1
else:
	numbers.append(insval)

print (numbers)


