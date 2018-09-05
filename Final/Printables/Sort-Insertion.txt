private void insertion(int[] array)
{
	for(int count = 1; count < array.length; count += 1)
	{
		int element = array[count];
		int index = count - 1;
		while(index >=0 && element < array[index])
		{
			array[index + 1] = array[index];
			index -= 1;
		}
		array[index+1] = element;
	}
}

Why a comparison-based sort requires Ω(n log n) comparisons for n elements.