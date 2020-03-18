

def mean_(*args):
	sum_ = 0.0
	length_ = 0.0

	for arg in args:
		sum_ += arg
		length_ += 1.0

	return sum_ / length_

# Function to get mean of array
def mean_ar(ar):
	return float(sum(ar))/float(len(ar))


# Test
# First function
if mean_(12, 445, 76, 23, 7, 9, 17, 19, 100) == 78.66666666666667:
	print("First Function Works!")

# Second function
if mean_ar([12, 445, 76, 23, 7, 9, 17, 19, 10]) == 68.66666666666667:
	print("Second Function Works!")

