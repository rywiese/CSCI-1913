//Same as Linked List
class AssociationList<Key, Value>
{
	private class Node
	{
		private Key key;
		private Value value;
		private Node next;
		
		private Node(Key k, Value v, Node n)
		{
			key = k;
			value = v;
			next = n;
		}
	}
	
	private Node first;
	
	public AssociationList()
	{
		first = null;
	}
	
	public Value get(Key key)
	{
		Node temp = first;
		while(temp!=null)
		{
			if(isEqual(temp.key, key))
				return temp.value;
			else
				temp = temp.next;
		}
		throw new IllegalArgumentException("No such key");
	}
	
	private boolean isEqual(Key leftKey, Key rightKey)
	{
		if(leftKey==null && rightKey==null)
			return true;
		else if(leftKey!=null && rightKey!=null)
			return leftKey.equals(rightKey);
		else
			return false;
	}
	
	public boolean isIn(Key key)
	{
		Node temp = first;
		while(temp!=null)
		{
			if(isEqual(temp.key, key))
				return true;
			else
				temp = temp.next;
		}
		return false;
	}
	
	public void put(Key key, Value value)
	{
		Node temp = first;
		boolean isIn = false;
		while(temp!=null)
		{
			if(isEqual(temp.key, key))
			{
				temp.value = value;
				isIn = true;
				break;
			}
			else
				temp = temp.next;
		}
		if(!isIn)
		{
			first = new Node(key, value, first);
		}
	}
}





//Left right trick (delete a node in a linked list except for the first)
Node left = head; //every list is defined with a head node which cant be deleted. It is the first node in the list.
Node right = head.next;
while(right != null)
{
	if(right.object.equals(key))
	{
		left.next = right.next;
		break;
	}
	else
	{
		left = right;
		right = right.next;
	}
}

//How to make an empty list
head = new Node(null, null)

public boolean isEmpty()
{
	return head.next==null;
}

//left right trick (add a node BEFORE)
Node left = head;
Node right = head.next;
while(right != null)
{
	if(right.object.equals(oldkey))
	{
		left.next = new Node(newKey, right);
		break;
	}
	else
	{
		left = right;
		right = right.next;
	}
}

//left right trick (add a node AFTER)
Node temp = head.next;
while(temp != null)
{
	if(temp.object.equals(oldKey))
	{
		temp.next = new Node(newKey, temp.next);
		break;
	}
	else
	{
		temp = temp.next;
	}
}

How efficient an association list is (using O notation).
	O(n), except for insert which is O(1)