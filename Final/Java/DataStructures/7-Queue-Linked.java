class LinkedQueue<Base>
{
	private class Node
	{
		private Base object;
		private Node next;

		private Node(Base object, Node next)
		{
			this.object = object;
			this.next = next;
		}
	}

	private Node front;
	private Node rear;

	public LinkedQueue()
	{
		front = null;
		rear = null;
	}

	public boolean isEmpty()
	{
		return front == null && rear == null;
	}

	public void enqueue(Base object)
	{
		if(isEmpty())
		{
			front = rear = new Node(object, null);
		}
		else
		{
			rear.next = new Node(object, null);
			rear = rear.next;
		}
	}

	public Base dequeue()
	{
		if(isEmpty())
		{
			throw new IllegalStateException("Empty");
		}
		else
		{
			Base temp = front.object;
			front = front.next;
			if(front ==null)
			{
				rear = null;
			}
			return temp;
		}
	}
}