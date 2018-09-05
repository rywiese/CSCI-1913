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
		if(object != null && object instanceof Dog) //if you pass the function a null pointer it will try to follow it and give you an error
		{
			Dog dog = (Dog) object; //the function thinks object has type Object, so we create dog that points to the same thing but is recognized as an instance of Dog
			return name.equals(dog.name); //you can see dog's name even though it is a private variable since you are in the Dog class.
		}
		else
		{
			return false;
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