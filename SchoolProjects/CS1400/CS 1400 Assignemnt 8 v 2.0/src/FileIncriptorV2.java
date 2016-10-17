import java.io.*;
import java.util.Scanner;

public class FileIncriptorV2 {
	// File uses some basic encryption techniques and saves as an encrypted
	// file.

	// --------------------------------------------------------------------------------------------------------------

	public static void main(String[] args) {
		// Declarations
		String fileName = "";
		Scanner read = new Scanner(System.in);
		String input = "";
		// String thisLn = "";

		// Prompt and input
		System.out.println("What is the name of the txt file you want encoded?(don't write the extention .txt)");
		fileName = read.nextLine();

		// Open file catch file not found.
		try {
			Scanner Fin = new Scanner(new File(fileName + ".txt"));
			PrintWriter Fout1 = new PrintWriter(new File(fileName + "Encripted1.txt"));
			PrintWriter Fout2 = new PrintWriter(new File(fileName + "Encripted2.txt"));
			while (Fin.hasNext()) {
				input = input + "\n" + Fin.nextLine();
			}
			Fout1.println(Encryption1(input));
			Fout2.println(Encryption2(input));
			Fin.close();
			read.close();
			Fout1.close();
			Fout2.close();
		} catch (FileNotFoundException exception) {
			System.out.println(
					"Could not find the file or could not write the file. Make sure its in the same directory as this program.");
		}
	}

	// -------------------------------------------------------------------------------------------------------------

	public static String Encryption1(String Finput) {
		String Out = "";
		for (int ii = 0; ii < Finput.length(); ii++) {
			int ASCII = (int) Finput.charAt(ii);
			if ((ASCII >= 97 && ASCII < 122) || (ASCII >= 65 && ASCII < 90)) {
				Out = Out + Character.toString((char) (ASCII + 1));
			} else if (ASCII == 122) {
				Out = Out + "a";
			} else if (ASCII == 90) {
				Out = Out + "A";
			} else {
				Out = Out + Finput.charAt(ii);
			}
		}
		return Out;
	}

	// -------------------------------------------------------------------------------------------------------------

	public static String Encryption2(String Finput) {
		String Out = "";
		for (int ii = 0; ii < Finput.length(); ii++) {
			int ASCII = (int) Finput.charAt(ii);
			if (ASCII >= 97 && ASCII < 122) {
				Out = Out + (ASCII - 96);
			} else if (ASCII >= 65 && ASCII < 90) {
				Out = Out + (ASCII - 39);
			} else {
				Out = Out + Finput.charAt(ii);
			}
		}
		return Out;
	}

}
