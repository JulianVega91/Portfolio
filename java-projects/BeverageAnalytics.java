import java.util.Scanner;

/**
 * Beverage Analytics Tool
 * * An interactive program that calculates annual beverage spending and 
 * performs string manipulation to analyze user preferences.
 * * Key Features:
 * - Cost projection (weekly/annual)
 * - Object method invocation (.equals, .concat, .length)
 * - Boolean-to-String conversion
 */
public class BeverageAnalytics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // --- Input Section ---
        System.out.print("Enter your full name: ");
        String firstName = sc.next();
        String lastName = sc.next();
        
        System.out.print(firstName + ", please enter your favorite beverage: ");
        String favBeverage = sc.next();
        
        System.out.print("Enter the cost of a " + favBeverage + " (e.g., 1.23): ");
        double bevCost = sc.nextDouble();
        
        System.out.print("Enter how many times you enjoy it per week: ");
        int bevPerWeek = sc.nextInt();
        
        // --- Financial Calculations ---
        double spendPerWeek = bevCost * bevPerWeek;
        double spendPerYear = spendPerWeek * 52;
        
        System.out.println("\n--- Financial Summary ---");
        System.out.println("Weekly spend: $" + spendPerWeek);
        System.out.println("Estimated annual cost for the " + lastName + " family: $" + spendPerYear);
        
        // --- String Manipulation & Logic ---
        // Checking if the user preference matches "coffee"
        String coffeeReference = new String("coffee");
        boolean userLikesCoffee = coffeeReference.equalsIgnoreCase(favBeverage);
        
        // Building a statement using .concat and valueOf
        String statusString = String.valueOf(userLikesCoffee);
        String finalStatement = "It is ".concat(statusString).concat(" that coffee is specifically liked.");
        
        System.out.println("\n--- Data Analysis ---");
        System.out.println(finalStatement);
        System.out.println("The name '" + firstName + "' has " + firstName.length() + " characters.");
        
        sc.close();
    }
}
