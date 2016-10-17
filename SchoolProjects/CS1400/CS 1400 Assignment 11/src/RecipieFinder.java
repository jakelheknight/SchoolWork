import java.net.*;
import java.io.*;
import java.util.*;

import com.sun.media.jfxmedia.logging.Logger;

public class RecipieFinder {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner Read = new Scanner(System.in);
		String Website = "";
		
		//-----------------------------------------------------
		
		System.out.println("Jacob Knight");
		System.out.println("What is the URL for the recipe?");
		Website = Read.nextLine();
		if(Website.contains("allrecipes.com")){
			if(!Website.substring(0,7).equals("http://")){
				Website = "http://" + Website;
			}
			//System.out.println(Website);
			try{
				URL page = new URL(Website);
				BufferedReader in = new BufferedReader(
				new InputStreamReader(page.openStream()));
				String inputLine;
				int I = 0;
				int n = 1;
				while ((inputLine = in.readLine()) != null){
					if(inputLine.contains("<title>")){
						System.out.println("Title:");
						System.out.println(inputLine.substring(inputLine.indexOf('>')+1, inputLine.length()-8) + "\n\nIngredients:");
					}
					else if(inputLine.contains("itemprop=\"ingredients\">")){
						System.out.println(inputLine.substring(inputLine.indexOf('>')+1, inputLine.length()-7));
					}
					else if(inputLine.contains("class=\"recipe-directions__list--item\">")){
						if(I == 0){
							System.out.println("\n\nDirections:");
							I = I+1;
						}
						System.out.println("\n" + n + ":" +inputLine.substring(inputLine.indexOf('>',inputLine.indexOf('>')+1)+1, inputLine.length()-12));
						n++;
					}
				}
				in.close();
			}catch(MalformedURLException e){
				System.out.println("Malfomed");
			}catch(IOException e){
				System.out.println("IOE");
			}
		}else{
			System.out.println("That is not an allrecipes URL...");
		}

	}

}
