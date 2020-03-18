
# 
def median(ar, ranked = False):
	if not ranked:
		data = sorted(ar[:])
	else:
		
		data = ar[:]

	# Data with odd length
	if len(data) % 2 != 0:

		# f(x) = (l(x) + 1) / 2 th term is the median of data
	
		return data[len(data) / 2]

	# Data with even length
	# f(x) = [l(x) / 2 th term + (l(x) + 2) / 2th term] / 2
	# 2.0 is to declare that median can be a float
	# in case of even length data
	return (data[len(data) / 2 - 1] + data[(len(data) + 1) / 2]) / 2.0

# Test
odd = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]
even = [8, 7, 5, 2, 1, 3, 4, 6]

if median(odd, ranked = True) == 131415 and median(even) == 4.5:
	
	# Print statements on separate lines look better
	print("Median of odd data: " + str(131415))
	print("Median of even data: " + str(4.5))
	print("Yeah, it works!")

else:
	# If algo didn't work
	print("There's something wrong!")


