
# Quick Sort Function
def quickSort(lst):
	if(len(lst) < 2):
		return lst

	pivot = lst[0]
	leftList = [_ for _ in lst if _ < pivot] + [pivot]
	rightList = [_ for _ in lst if _ > pivot]

	return quickSort(leftList) + quickSort(rightList)

# Main Function
if __name__ == '__main__':
	lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -2]
	print(quickSort(lst))