import java.util.Iterator;
class Stack<Base>
{
	private class Node
	{
		private Base object;
		private Node next;
		//...
	}
	private Node top;
	//...

	private class StackIterator implements Iterator<Base> //all of these methods are in Iterator
	{
		private Node where;

		private StackIterator()
		{
			where = top;
		}

		public boolean hasNext()
		{
			return where != null;
		}

		public Base next()
		{
			Base temp = where.object;
			where = where.next;
			return temp;
		}

		public void remove()
		{
			//do nothing because we don't want to be able to remove things unless you use the pop method.
		}
	}

	public StackIterator iterator()
	{
		return new StackIterator();
	}

	//...
	
}

//implementation of iterator
Stack<string> s = new Stack<String>();
s.push("A");
s.push("B");
s.push("C");
Iterator<String> i = s.iterator();

while(i.hasNext())
{
	System.out.println(i.next());
}

//print every element without knowing what kind of stack you're working with and without using stack methods