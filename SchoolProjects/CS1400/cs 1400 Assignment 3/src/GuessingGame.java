import java.util.Scanner;
import java.util.Random;

public class GuessingGame {

	public static void main(String[] args) {
		// Declarations
		Scanner Guess = new Scanner(System.in);
		Random rand = new Random();
		int g = 0;
		int i = 0;
		int j = 1;
		int r = rand.nextInt(10)+1;
		
		//prompt and 1st input
		System.out.println("Jacob Knight");
		System.out.println("Its a guessing game guess an whole number between 1 and 10.");
		g = Guess.nextInt();
		
		//System.out.println("rand = "+ r );
		
		//control and output.
		while ( i==0 ) {
			if( g == r){ 
				System.out.println("Good guess how did you know it was " + r + ". It only took " + j + " tries.");
				i = 1;
			} else if( g < 1 || g > 10 ){
				System.out.println("Between 1 and 10 Please.");	
				g = Guess.nextInt();
				j= j + 1;
			}else if( g < r ){
				System.out.println("Try allitle higher.");	
				g = Guess.nextInt();
				j= j + 1;		
			}else if( g > r ){
				System.out.println("Try allitle lower.");
				g = Guess.nextInt();
				j= j + 1;		
			}
		}
		Guess.close();
	}
}
