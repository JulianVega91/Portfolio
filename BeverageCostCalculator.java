import java.util.Scanner;

/**
 * Beverage Cost Calculator
 * A program to analyze weekly and annual spending habits on favorite beverages.
 * Demonstrates basic Java syntax, data types, and interactive console I/O.
 */
public class BeverageCostCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // --- User Identification ---
        System.out.print("Enter your full name: ");
        String firstName = sc.next();
        String lastName = sc.next();
        
        // --- Input Gathering ---
        System.out.print(firstName + ", please enter your favorite beverage: ");
        String favBeverage = sc.next();
        
        System.out.print("Enter the cost of a " + favBeverage + " (e.g., 1.23): ");
        double bevCost = sc.nextDouble();
        
        System.out.print("Enter the times that you enjoy a " + favBeverage + " in a week: ");
        int bevPerWeek = sc.nextInt();
        
        // --- Calculations ---
        double spendPerWeek = bevCost * bevPerWeek;
        double spendPerYear = spendPerWeek * 52;
        
        // --- Output Results ---
        System.out.println("\n--- Summary ---");
        System.out.println("Weekly spend: $" + spendPerWeek);
        System.out.println("Beverage: " + favBeverage + " ($" + bevCost + " each)");
        System.out.println("Frequency: " + bevPerWeek + " times per week");
        
        System.out.print("\nTrue or false, you would like to save more money: ");
        boolean saveMore = sc.nextBoolean();
        
        System.out.println("It is " + saveMore + " that the " + lastName + " family would like to save $" + spendPerYear + " per year.");
        
        sc.close(); // Buena práctica: cerrar el scanner
    }
}
