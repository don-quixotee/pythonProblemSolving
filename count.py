
def count(ar, n):
	count = 0
	
	for element in ar:
		# More complex condition could be 
		# => (not element != n)
		if element == n:
			count += 1
	
	return count

# Testing
# add your test cases in list below
test_cases = [([1, 1, 2, 3, 5, 8, 13, 21, 1], 1), ("Captain America", "a")]
for test_case in test_cases:
	print("TestCase: {}, {}".format(test_case[0], test_case[1]))
	print("Results: {}\n".format(count(test_case[0], test_case[1])))


