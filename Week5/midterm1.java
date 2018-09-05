JAVA

How to define a class.

How to define a method.

How the for statement works.
	for(int i=1; i<11; i++){
              System.out.println("Count is: " + i);

How the if–else statement works.

How the while statement works.

How the types boolean, char, int, double, and String work.

How pointers (references) work.

How the arithmetic operators +, −, *, /, and % work.

How the relational operators ==, !=, <, >, <=, and >= work.

How the assignment operator = works.

How to access the elements of an array with [].

How to make a class instance with new.

How to make an array with new.

How to find the length of an array.
	ArrayList<Integer> arr = new ArrayList(10);
	int size = arr.size();

How the . (dot) operator works with class instances.

How 1-dimensional arrays work.

How the prefixes private and public work.

How to declare instance variables in a class.

How to declare local variables in a method.



int[] a = new int[10];
String s,t;
s = "Hello";
t = "Hello";
s.equals(t);
s.charAt(0);



class Account
{
	private int dollars;

	public Account(int starting)
	{
		if(starting < 0)
		{
			throw new IllegalArgument Exception("Negative Balance");
		}
		else
		{
			dollars = starting;
		}
	}

	public void deposit(int amount)
	{
		if(amount <  0)
		{
			throw new IllegalArgumentException("Negative amount");
		}
		else
		{
			dollars += amount;
		}
	}

	public void withdraw(int amount)
	{
		if(amount > dollars)
		{
			throw new IllegalArgumentException("Insufficient Funds")
		}
		else
		{
			dollars -= amount;
		}
	}

	public int balance()
	{
		return dollars;
	}
}

class Driver
{
	public static void main(String[] args)
	{
		Account rich = new Account(10000); /*rich is a pointer*/ 
		rich.withdraw(1000);
		System.out.println(rich.balance()); /*prints 9000*/
		Account richer = rich; /*Does not make a new account. It makes a new pointer to the same account.*/
		richer.withdraw(1000);
		System.out.println(rich.balance()); /*prints 8000*/
	}
}	












class Dog
{
	private String name;
	private static int count = 0;
	private static final int numberOfLegs = 4;

	public Dog(String name)
	{
		this.name = name;
		count += 1;
	}

	public static int howMany()
	{
		return count;
	}

	public static boolean equals(Object object)
	{
		if(object instanceof Dog)
		{
			if()
		}
	}
}

class Driver
{
	public static void main(string[] args)
	{

	}
}

//'This' points to the current class instance
//'Final' is a variable whose value can't change

//all classes inherit .equals() from the Object class, which is logically equivalent to == (returns true <=> reference the same data, i think). This must be overridden if you want it to work differently