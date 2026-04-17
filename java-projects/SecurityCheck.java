import java.util.Scanner;

public class SecurityCheck
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int count = 0;
	    boolean lockedOut = false;
	    
	    while(count < 3 && !lockedOut) {
	        System.out.print("Enter password: ");
	        String pass = sc.next();
	        if(pass.equals("1234")) {
	            System.out.println("Access Granted");
	            break;
	        }
	        count++;
	    }
	    if(count == 3) System.out.println("Locked Out");
	}
}
