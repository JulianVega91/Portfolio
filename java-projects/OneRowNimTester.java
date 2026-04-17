public class OneRowNimTester
{ 
  public static void main(String args[])
  {
    OneRowNim game = new OneRowNim();
    game.report();
    game.takeThree();
    game.report();
    game.takeThree();
    game.report();
    game.takeOne();
    game.report();
  } //main()
}
class OneRowNim
{ 
  private int nSticks = 7; // Start with 7 sticks.
  private int player = 1;  //Player 1 plays first.

  public void takeOne()
  {
    takeSticks(1);
  } // takeOne()

  public void takeTwo()
  {
    takeSticks(2);
  } // takeTwo()

  public void takeThree()
  {
    takeSticks(3);
  }  // takeThree()
  
  void takeSticks(int sToTake)
  {
    nSticks = nSticks - sToTake;
    player = 3 - player;
  }  // takeSticks()
  
  public int getSticks()
  {
    return nSticks;
  }
  
  public String getReport()
  {
    return ("Number of sticks left: " + getSticks() + "\nNext turn by player " + player);
  }

  public void report()
  {
    System.out.println(getReport());
  }   // report()
} // OneRowNim class