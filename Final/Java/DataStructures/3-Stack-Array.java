class ArrayStack <Base>
{
	private int count;
	private int size;
	private Base[] objects;

	public ArrayStack(int size)
	{
		count = 0;
		this.size = size;
		objects = (Base[]) new Object[this.size];
	}

	public boolean isEmpty()
	{
		return count==0;
	}

	public boolean isFull()
	{
		return count==size;
	}

	public void push(Base object)
	{
		if(isFull())
		{
			throw new IllegalStateException("Stack is full");
		}
		else
		{
			objects[count] = object;
			count++;
		}
	}

	public void pop()
	{
		if(isEmpty())
		{
			throw new IllegalStateException("Stack is Empty");
		}
		else
		{
			objects[count-1] = null;
			count--;
		}
	}

	public Base peek()
	{
		if(isEmpty())
			throw new IllegalStateException("Stack is Empty");
		else
			return objects[count - 1];
	}
}