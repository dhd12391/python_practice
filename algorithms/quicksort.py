# Quicksort 

def quicksort(list):
	left = []
	middle = []
	right = []

	if len(list) == 0 or len(list) == 1:
		return list
	
	pivot = list[0]
	for item in list:
		if item < pivot:
			left.append(item)
		elif item == pivot:
			middle.append(item)
		elif item > pivot:
			right.append(item)
	
	return quicksort(left) + middle + quicksort(right)

