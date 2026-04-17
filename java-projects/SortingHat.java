import java.util.Scanner;

public class Version2
{
	public static void main(String[] args) {
	    
	    Scanner sc = new Scanner(System.in);
	    String user = new String("y");
	    
	    do
	    {
	        System.out.println();
	        System.out.println("\"Quit\" to stop the program");
	        System.out.println("You are in the world of Harry Potter, the Sorting Hat is about to tell your house");
	        System.out.println("But you know the spell to confuse the hat, you just need to chose the house");
	        System.out.print("Which house would you like to belong to? (Gryffindor, Slytherin, Ravenclaw, Hufflepuff): ");
	        String place = sc.next();
	        System.out.println();
	        
	        switch(place)
	        {
	            case "Gryffindor":
	            case "gryffindor":
	                System.out.println("Ah, Gryffindor! Get ready to save the world...\nor at least get into epic trouble.");
	                break;
	                
	            case "Slytherin":
	            case "slytherin":
	                System.out.println("Slytherin, huh? ambition and… a touch of mystery.\nJust remember: if you find a snake talking to you in the bathroom, don't ask why.");
	                break;
	                
	            case "Ravenclaw":
	            case "ravenclaw":
	                System.out.println("Ravenclaw, brilliant choice! Here the books choose you...\nand yes, you may wake up reciting potions");
	                break;
	                
	            case "Hufflepuff":
	            case "hufflepuff":
	                System.out.println("Welcome to Hufflepuff, the coziest house! We have cookies, hugs…\nand a serious nap schedule.");
	                break;
	                
	            case "Quit":
	            case "quit":
	                System.out.println("Come on! Even Muggles can last longer in a History of Magic class.");
	                user = "n";
	                break;
	                
	            default:
	                System.out.println("Oops, that didn't turn out as you expected! A failed spell?\nBetter try another option before you turn into a toad.");
	        }
	        
	        if(user.equals("y"))
	        {
	            System.out.println();
	            System.out.print("Do you want to continue? (y/n): ");
	            user = sc.next();
	        }
	    }
	    while(user.equals("y"));
	}
}