import java.util.Scanner;

public class SecurityCheck {

    public static void main(String[] args)
    {
        SecurityCheck seccheck = new SecurityCheck("1234", "abc", "4321");

        Scanner scanner = new Scanner(System.in);

        boolean access = false;

        String pw1;
        String pw2;
        String overridepw;

        while(!access)
        {
            System.out.println("Enter password 1");
            pw1 = scanner.next();

            System.out.println("Enter password 2");
            pw2 = scanner.next();

            System.out.println("Enter override password");
            overridepw = scanner.next();

            access = seccheck.accessGranted(pw1, pw2, overridepw);
        }

        System.out.println("Access granted!");
        scanner.close();
    }

    String userpw1;
    String userpw2;
    String overridepw;
    boolean locked = false;
    
    public SecurityCheck(String pw1, String pw2, String overrpw)
    {
        userpw1 = pw1;
        userpw2 = pw2;
        overridepw = overrpw;
    }
    
    public boolean login1(String trypw1)
    {
        if(!userpw1.equals(trypw1))
        {
            locked = true;
            return false;
        }
        return true;
    }
    
    public boolean login2(String trypw2)
    {
        if(!userpw2.equals(trypw2))
        {
            locked = true;
            return false;
        }
        return true;
    }
    
    public boolean adminLogin(String adminPw)
    {
        if(overridepw.equals(adminPw))
        {
            locked = false;
            return true;
        }
        return false;
    }
    
    public boolean accessGranted(String pw1, String pw2, String overrpw)
    {
        return (((login1(pw1) && login2(pw2)) && !locked) || adminLogin(overrpw));
    }
}
