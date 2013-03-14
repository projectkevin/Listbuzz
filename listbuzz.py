list = range(1,101)
fizz = filter(lambda x: x % 3 == 0, list)
buzz = filter(lambda x: x % 5 == 0, list)
for i in fizz:
	list[i-1] = "Fizz"
for i in buzz:
	list[i-1] = "Buzz"
print list