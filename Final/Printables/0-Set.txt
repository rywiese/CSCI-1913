class Set<Base>
{
  private int    count;      //  How many elements the SET has so far.
  private Base[] elements;   //  The elements in the SET.
  private int    factor;     //  Multiply by this many elements to resize.
  private int    increment;  //  Add this many elements to resize.

//  Constructors. LENGTH defaults to 10, FACTOR to 1, and INCREMENT to 10.

  public Set()
  {
    this(10, 1, 10);
  }

  public Set(int length)
  {
    this(length, 1, 10);
  }

  public Set(int length, int factor, int increment)
  {
    if (length < 0 || factor < 1 || increment < 1)
    {
      throw new IllegalArgumentException("Parameter(s) out of range.");
    }
    else
    {
      count          = 0;
      elements       = (Base[]) new Object[length];
      this.factor    = factor;
      this.increment = increment;
    }
  }

//  ADD. Add ELEMENT to the set if it's not already a member.

  public void add(Base element)
  {
    if (where(element) < 0)
    {
      if (count >= elements.length)
      {
        int newLength = factor * elements.length + increment;
        Base[] newElements = (Base[]) new Object[newLength];
        for (int index = 0; index < count; index += 1)
        {
          newElements[index] = elements[index];
        }
        elements = newElements;
      }
      elements[count] = element;
      count += 1;
    }
  }

//  IS EMPTY. Test if the set has no elements.

  public boolean isEmpty()
  {
    return count == 0;
  }

//  IS EQUAL. Test if LEFT equals RIGHT, where either or both may be NULL.

  private boolean isEqual(Base left, Base right)
  {
    if (left == null || right == null)
    {
      return left == right;
    }
    else
    {
      return left.equals(right);
    }
  }

//  IS IN. Test if ELEMENT is a member of the set.

  public boolean isIn(Base element)
  {
    return where(element) >= 0;
  }

//  LENGTH. Return the current number of elements in the set.

  public int length()
  {
    return count;
  }

//  REMOVE. Remove ELEMENT from the set. Do nothing if ELEMENT is not there.

  private void remove(Base element)
  {
    int index = where(element);
    if (index >= 0)
    {
      while (index < count - 1)
      {
        elements[index] = elements[index + 1];
        index += 1;
      }
      count -= 1;
      elements[count] = null;
    }
  }

//  TO STRING. Convert the set to a STRING, for printing.

  public String toString()
  {
    StringBuilder builder = new StringBuilder();
    builder.append('{');
    if (count > 0)
    {
      builder.append(elements[0]);
      for (int index = 1; index < count; index += 1)
      {
        builder.append(", ");
        builder.append(elements[index]);
      }
    }
    builder.append('}');
    return builder.toString();
  }

//  WHERE. Return the index of ELEMENT in ELEMENTS, or -1 if it isn't there.

  private int where(Base element)
  {
    for (int index = 0; index < count; index += 1)
    {
      if (isEqual(element, elements[index]))
      {
        return index;
      }
    }
    return -1;
  }

//  MAIN.  Test SET's methods on a few examples. The comments show what will be
//  printed.

  public static void main(String[] args)
  {
    Set<String> set = new Set<String>(1, 1, 2);

    System.out.println(set);            //  {}
    System.out.println(set.isEmpty());  //  true
    System.out.println(set.isIn("A"));  //  false
    System.out.println(set.isIn("B"));  //  false
    System.out.println(set.length());   //  0

    set.add("A");
    System.out.println(set.isEmpty());  //  false
    System.out.println(set.isIn("A"));  //  true
    System.out.println(set.isIn("B"));  //  false
    System.out.println(set);            //  {A}
    System.out.println(set.length());   //  1

    set.add("B");
    System.out.println(set);            //  {A, B}
    System.out.println(set.length());   //  2
    
    System.out.println(set.isIn("A"));  //  true
    System.out.println(set.isIn("B"));  //  true

    set.add("C");
    System.out.println(set);            //  {A, B, C}
    System.out.println(set.length());   //  3
    set.add("C");
    System.out.println(set);            //  {A, B, C}
    System.out.println(set.length());   //  3

    set.remove("B");
    System.out.println(set);            //  {A, C}
    System.out.println(set.length());   //  2

    set.remove("Z");
    System.out.println(set);            //  {A, C}
    System.out.println(set.length());   //  2

    set.remove("A");
    System.out.println(set);            //  {C}
    System.out.println(set.length());   //  1
  }
}