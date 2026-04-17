import java.util.Arrays;

public class CheckTriangle
{
	public static void main(String[] args) {
		int[] array1 = {1, 2, 3, 4, 5};
		System.out.println("Is triangle: " + iteration(array1));
	}
    
	public static boolean iteration(int[] array) {
		int check = 1;
		for(int i: array) {
            if(check == i) check++;
            else return false;
		}
		return true;
	}
}
