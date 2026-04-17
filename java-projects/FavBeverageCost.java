import java.util.Scanner;

public class FavBeverageCost
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter your full name: ");
        String firstName = sc.next();
        String lastName = sc.next();
      
        System.out.print(firstName + ", please enter your favorite beverage: ");
        String favBeverage = sc.next();
        System.out.print("Enter the cost of a " + favBeverage + " as a number such as 1.23: ");
        double bevCost = sc.nextDouble();
        System.out.print("Enter the times that you enjoy a " + favBeverage + " in a week: ");
        int bevPerWeek = sc.nextInt();
      
        double spendPerWeek = bevCost * bevPerWeek;
        System.out.println("You spend $" + spendPerWeek + " per week on your $" + bevCost + " " + favBeverage + " which you enjoyed " + bevPerWeek + " times per week");
      
        System.out.print("True or false, you would like to save more money: ");
        boolean saveMore = sc.nextBoolean();
        System.out.println("It is " + saveMore + " that the " + lastName + " family would like to save $" + (spendPerWeek * 52) + " per year");
        
        String strCoffee;
        strCoffee = new String ("coffee");
        boolean userLikesCoffee;
        userLikesCoffee = strCoffee.equals(favBeverage);
        String strUserLikesCoffee;
        strUserLikesCoffee = String.valueOf(userLikesCoffee);
        String statement = "It is ".concat(strUserLikesCoffee);
        statement = statement.concat(" that coffee is liked");
        System.out.println(statement);
      
        int nameLength = firstName.length();
        System.out.println(firstName + " is " + nameLength + " character long");
    }
}
