//
//  SORTY LIST. Skeleton program for CSci 1913 Project 2.
//
//    James Moen
//    07 Apr 17
//

//  SORTY LIST. A linked list of INT's that can be efficiently sorted.

class SortyList
{

//  NODE. A node in a singly linked linear list of INT's.

  private class Node
  {
    private int  key;   //  The INT.
    private Node next;  //  The next NODE in the list, or NULL.

//  Constructor. Make a NODE with KEY and NEXT.

    private Node(int key, Node next)
    {
      this.key  = key;
      this.next = next;
    }
  }

  private Node head;   //  Head NODE.
  private Node first;  //  First NODE in a list of NODEs.

//  SORTY LIST. Constructor. Make a list of NODEs that holds the INT arguments.
//  Also make a HEAD node for SORT to use.

  public SortyList()
  {
    head = new Node(0, null);
  }

  public SortyList(int first, int ... rest)
  {
    Node last = new Node(first, null);
    this.first = last;
    for (int index = 0; index < rest.length; index += 1)
    {
      last.next = new Node(rest[index], null);
      last = last.next;
    }
    head = new Node(0, null);
  }

//  SORT. Sort the list whose first NODE is FIRST. We can't make more NODEs but
//  we can change the NEXT slots of the existing NODEs.

  public SortyList sort()
  {
    first = sort(first);
    return this;
  }

//  Sort the list UNSORTED without making any new NODE's, and return the sorted
//  list.

  private Node sort(Node unsorted)
  {

//  YOUR CODE GOES HERE!
	  
	  //Testing
	  if(unsorted == null || unsorted.next == null)
		  return unsorted;
	  
	  //Halving
	  Node left = unsorted;
	  Node right = unsorted.next;
	  Node temp = right;
	  while(true)
	  {
		  unsorted.next = unsorted.next.next;
		  unsorted = unsorted.next;
		  if(unsorted == null)
		  {
			  temp.next = null;
			  break;
		  }
		  
		  temp.next = temp.next.next;
		  temp = temp.next;
		  if(temp == null)
		  {
			  unsorted.next = null;
			  break;
		  }
	  }
	  temp = null;
	  
	  //Sorting
	  left = sort(left);
	  right = sort(right);
	  
	  //Merging
	  Node merge = head;
	  temp = head;
	  while(true)
	  {
		  if(left == null)
		  {
			  temp.next = right;
			  break;
		  }
		  if(right == null)
		  {
			  temp.next = left;
			  break;
		  }
		  if(left.key <= right.key)
		  {
			  temp.next = left;
			  left = left.next;
			  temp = temp.next;
		  }
		  else
		  {
			  temp.next = right;
			  right = right.next;
			  temp = temp.next;
		  }
	  }
	  return merge.next;
  }

//  TO STRING. Turn FIRST into a string for printing. If the list is empty then
//  the string is "[]". Otherwise it's "[K₁, K₂ ..., Kⱼ]" where the K's are the
//  KEYS from FIRST, in order of appearance.

  public String toString()
  {
    StringBuilder builder = new StringBuilder();
    builder.append('[');
    if (first != null)
    {
      Node temp = first;
      builder.append(temp.key);
      temp = temp.next;
      while (temp != null)
      {
        builder.append(", ");
        builder.append(temp.key);
        temp = temp.next;
      }
    }
    builder.append(']');
    return builder.toString();
  }

//  MAIN. Test SORTY LIST by running it on a few examples.

  public static void main(String[] args)
  {
    System.out.println(new SortyList()                            .sort());
    System.out.println(new SortyList(0)                           .sort());
    System.out.println(new SortyList(1, 0)                        .sort());
    System.out.println(new SortyList(2, 1, 0)                     .sort());
    System.out.println(new SortyList(9, 8, 7, 6, 5, 4, 3, 2, 1, 0).sort());
    System.out.println(new SortyList(5, 8, 4, 9, 0, 1, 2, 3, 7, 6).sort());
    System.out.println(new SortyList(6, 8, 4, 9, 0, 7, 1, 2, 3, 7, 6, 3, 6, 8, 5, -13, 34, 65, 2, 33, 5, 6, 1, 5, 0, 0).sort());
    System.out.println(new SortyList(4, 6, 0)                     .sort());
    System.out.println(new SortyList(4, 6, 4)                     .sort());
    System.out.println(new SortyList(2, 1, 0, 88, 0, 2, 1, 4, 1)  .sort());
    
  }
}

/*
OUTPUT:

[]
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[-13, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 33, 34, 65]
[0, 4, 6]
[4, 4, 6]
[0, 0, 1, 1, 1, 2, 2, 4, 88]

*/