import java.util.Arrays;

public class CheckTriangle
{
	public static void main(String[] args) {
        final int START = 1;
        final String STR = "Is triangle: ";
        
        // false
		int[] array1 = {1, 5, 4, 2, 3};
		System.out.println(STR + recursion(array1, START));
		System.out.println(STR + iteration(array1));
		System.out.println();
		
		// true
		int[] array2 = {1, 2, 3, 4, 5};
		System.out.println(STR + recursion(array2, START));
		System.out.println(STR + iteration(array2));
	}
    
	public static boolean recursion(int[] array, int i) {
		if((array.length - 1) == 0) {
            return array[0] == i;
		} else {
            return array[0] == i && recursion(Arrays.copyOfRange(array, 1, array.length), i + 1);
		}
	}
    
	public static boolean iteration(int[] array) {
		int check = 1;
		for(int i: array) {
            if(check == i) {
                check++;
            } else {
                return false;
            }
		}
		return true;
	}
}