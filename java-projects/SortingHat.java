import java.util.Scanner;

public class SortingHat
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Sorting Hat Quiz!");
	    System.out.print("1 for Brave, 2 for Smart: ");
	    int choice = sc.nextInt();
	    switch(choice) {
	        case 1: System.out.println("Gryffindor!"); break;
	        case 2: System.out.println("Ravenclaw!"); break;
	        default: System.out.println("Muggle!");
	    }
	}
}
