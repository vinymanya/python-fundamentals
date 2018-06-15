
# 'foo', 'bar' and "fooBar" algorithm challenge
for num in range(100, 100001):
	if num % 2 == 0:
		print "Bar"
	elif num % 2 != 0:
		print "Foo"
	else:
		print "FooBar"