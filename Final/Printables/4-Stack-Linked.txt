class LinkedStack <Base>
{
	private class Node
	{
		private Base object; //private with respect to outermost class
		private Node next; //LinkedStack can access these vars
		private Node(Base object, Node next)
		{
			this.object = object;
			this.next = next;
		}
	}

	private Node top;

	public LinkedStack()
	{
		top = null;
	}

	public void push(Base object)
	{
		top = new Node(object, top);
	}

	public void pop()
	{
		if(isEmpty())
		{
			throw new IllegalStateException("Stack is empty");
		}
		else
		{
			top = top.next;
		}
	}

	public Base peek()
	{
		if(isEmpty())
		{
			throw new IllegalStateException("Stack is empty");
		}
		else
		{
			return top.object;
		}
	}

	public boolean isEmpty()
	{
		return top == null;
	}
}