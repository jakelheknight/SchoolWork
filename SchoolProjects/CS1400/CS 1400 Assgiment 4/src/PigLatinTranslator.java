import java.util.Scanner;

public class PigLatinTranslator {
	public static String convert(String in){
		in = in.toLowerCase();
		int[] tmpFV = {in.indexOf('a'), in.indexOf('e'),in.indexOf('i'),in.indexOf('o'),in.indexOf('u'),in.indexOf('y')};
		int FV = in.length();
		for(int ii = 0; ii<tmpFV.length;ii++){
			if(tmpFV[ii]<FV && tmpFV[ii] != -1){
				FV=tmpFV[ii];
			}
		} 
		String PLout = "";
		if(FV == 0){
			PLout = in+"way";
		}else{
			PLout = in.substring(FV)+in.substring(0, FV)+"ay";
		}
		return PLout;
	}//takes in a word and returns that word in pig Latin.
	
	public static String preproccessing(String sentince){
		sentince = sentince.replaceAll(" there's ", " there is ");
		sentince = sentince.replaceAll(" we'll ", " we will ");
		sentince = sentince.replaceAll(" it's ", " it is ");
		sentince = sentince.replaceAll(" you'll ", " you will");
		sentince = sentince.replaceAll(" is'nt ", " is not ");
		sentince = sentince.replaceAll("\\.", " 1");
		sentince = sentince.replaceAll("\\?", " 2");
		sentince = sentince.replaceAll("\\!", " 3");
		sentince = sentince.replaceAll("\\,", " 4");
		
		return sentince;
	}//Takes care of conjunctions and punctuation. Ran out of time to finish the long list. Threw in a few common ones for fun
	
	public static void main(String[] args) {
		System.out.println("Welcome to Jacob Knights Pig Latin translator. \n"
				+ "You can quit at any time by entering q.");
		Scanner wordRead = new Scanner(System.in);
		String sentince = "";
		int quit = 0;
		while( quit == 0) {
			System.out.println("\nWhat word or sentince do you want translated?");
			sentince = wordRead.nextLine();
			if(sentince.equals("q")){
				quit = 1;
				System.out.println("Good By.");
			}else{
			sentince = preproccessing(sentince);
			String[] words = sentince.split(" "); //Break into words.
			String[] PLwords = new String[words.length];
			for(int ii = 0; ii < words.length; ii++){
				
				PLwords[ii] = convert(words[ii]);
				if(PLwords[ii].equals("1ay")){
					System.out.print(".");
				}else if(PLwords[ii].equals("2ay")){
					System.out.print("?");
				}else if(PLwords[ii].equals("3ay")){
					System.out.print("!");
				}else if(PLwords[ii].equals("4ay")){
					System.out.print(",");
				}else{
					if(ii != 0){
						System.out.print(" ");
					}
					System.out.print(PLwords[ii]);
				}
			}
			}
		}	
		wordRead.close();
	}	
}

	
