class Deque<Base>
{
	private class Node
	{
		private Base object;
		private Node left;
		private Node right;
		
		private Node(Base object, Node left, Node right)
		{
			this.object = object;
			this.left = left;
			this.right = right;
		}
	}
	
	private Node head;
	
	public Deque()
	{
		head = new Node(null, null, null);
		head.left = head;
		head.right = head;
	}
	
	public void enqueueFront(Base object)
	{
		head.right.left = new Node(object, head, head.right);
		head.right = head.right.left;
	}
	
	public void enqueueRear(Base object)
	{
		head.left.right = new Node(object, head.left, head);
		head.left = head.left.right;
	}
	
	public Base dequeueFront()
	{
		if(isEmpty())
			throw new IllegalStateException("Empty");
		else
		{
			Node temp = head.right;
			head.right = head.right.right;
			head.right.left = head;
			return temp.object;
		}
	}
	
	public Base dequeueRear()
	{
		if(isEmpty())
			throw new IllegalStateException("Empty");
		else
		{
			Node temp = head.left;
			head.left = head.left.left;
			head.left.right = head;
			return temp.object;
		}	
	}
	
	public boolean isEmpty()
	{
		return head.right == head;
	}
}

//delete p
p.left.right = p.right;
p.right.left = p.left;

//add a node to the right of p
q = new Node("C", p, p.right);
p.right.left = q;
p.right = q;

//add a node to the left of p
q = new Node("A", p.left, p);
p.left.right = q;
p.left = q;

//add a head (Circular DLL)
head = new Node(null, null, null);
head.left = head;
head.right = head;

//traversing a (DDLL)
temp = head.right;
while(temp != head)
{
	//visit temp
	temp = temp.right;
}