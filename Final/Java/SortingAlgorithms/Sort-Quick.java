private swap(int[] array, int left, int right)
{
	int temp = array[left];
	array[left] = array[right];
	array[right] = temp;
}

private void quicksort(int[] array, int leftEnd, int rightEnd)
{
	int left = leftEnd;
	int right = rightEnd;
	int pivot = array[(leftEnd + rightEnd) / 2];

	do
	{
		while(array[left] < pivot)
		{
			left += 1;
		}
		while(array[right] > pivot)
		{
			right -= 1;
		}
		if(left <= right)
		{
			swap(array, left, right);
			left += 1;
			right -= 1;
		}
	}
	while(left <= right);
	if(leftEnd < left)
	{
		quicksort(array, leftEnd, right);
	}
	if(left < rightEnd)
	{
		quicksort(array, left, rightEnd);
	}
}