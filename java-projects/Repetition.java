import java.util.Scanner;

public class Repetition
{
	public static void main(String[] args) {
	    
	    int stars;
	    int numStars = 0;
	    int starsRow;
	    //3rd Step      Create a Scanner
	    Scanner sc = new Scanner(System.in);
	    
	    //Stars Row Loop
	    //5th Step      Ask user how many stars
		System.out.print("How many stars?: ");
		//6th Step      Save the input in a variable called stars
		stars = sc.nextInt();
		//7th Step      Create a loop that print the stars from 0 to user input
		while (numStars < stars)
		{
		    System.out.print("*");
		    numStars++;
		}
		//8th Step      Print an empty line
		System.out.println();
		//9th Step      Create a loop that print the stars from user input to 0
		while (stars > 0)
		{
		    System.out.print("*");
		    stars--;
		}
		System.out.println();
		
		//Y Loop
		String userIn = "y";
		System.out.println();
		//10th Step     Create a loop that ask the user to enter "y" to continue
		while(userIn.equals("y"))
		{
		    System.out.println("Enter 'y' to continue");
		    userIn = sc.next();
		}
		System.out.println();
		
		//While Loop Challenge
		System.out.print("How many stars?: ");
		stars = sc.nextInt();
		numStars = 0;
		
		while(numStars < stars)
		{
		    starsRow = 0;
		    while(starsRow < numStars)
		    {
		        System.out.print("*");
		        starsRow++;
		    }
		    numStars++;
		    System.out.println();
		}
		
		while(stars > 0)
		{
		    starsRow = 0;
		    while(starsRow < stars)
		    {
		        System.out.print("*");
		        starsRow++;
		    }
		    stars--;
		    System.out.println();
		}
	}
}
