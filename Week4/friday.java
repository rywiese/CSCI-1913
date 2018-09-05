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