import java.io.*;
import java.util.Scanner;

public class BeveragePrefProcessor
{
    public void processPref(String fileName) {
        try {
            FileReader fr = new FileReader(fileName);
            Scanner sc = new Scanner(fr);
            String firstName = sc.next();
            String favBeverage = sc.next();
            System.out.println(firstName + " likes " + favBeverage);
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        BeveragePrefProcessor proc = new BeveragePrefProcessor();
        proc.processPref("BeveragePref.txt");
    }
}
