import java.util.Random;
import java.util.Scanner;

public class DiceSim {

	public static void main(String[] args) {
		//Declarations
		Scanner Read = new Scanner(System.in); 	//Scanner for user input.
		Random role = new Random(); 			// Start random number generator
		int n = 100; 							// Number of dice thrown.
		int hist [] = new int[11]; 				//Stores the values for our Histogram.
		int histNorm [] = new int[11]; 			//Stores the values for our Normalized Histogram.
		int tmp =0;								//Temporarily stores values.
		boolean input = false; 
//------------------------------------------------------------------------------------ 	
		//Input number of roles.
		System.out.println("Welcome to Mr. Knights Dice throwing simulator. \n"
				+ "How many Dice should we through? \n "
				+ "(Plese enter a number between 100 and 1000)");
		while(!input){
			n =Read.nextInt();
			if(n>=100 && n<=1000){
				input = true;
			}else{
				System.out.println("Invalid response plese enter an integer between 100 and 1000");
			}
		}
//-----------------------------------------------------------------------------------
		//Build the array
		for(int jj = 0; jj < n; jj++){
			tmp = role.nextInt(6)+role.nextInt(6);
			hist[tmp]=hist[tmp]+1;
		}
//-----------------------------------------------------------------------------------
		//Normalize histogram
		for(int kk=0; kk<hist.length;kk++){
			histNorm[kk]=100*hist[kk]/n;
		}
//-----------------------------------------------------------------------------------
		//Show Histogram
		System.out.println("Drum role please. \nYour results are in the folowing histogram. \nPlease note that 1 * represents 1 %");
		for(int hh = 0; hh<histNorm.length;hh++){
			tmp = hh+2;
			System.out.print("\n"+tmp+":  ");
			for(int kk = 0; kk<histNorm[hh];kk++){
				System.out.print(" *");
			}
		}
		System.out.println("\n \nThank you for usign the dice sim.");
		Read.close();
	}

}
