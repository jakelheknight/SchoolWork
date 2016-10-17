import java.util.ArrayList;
import java.util.Scanner;

public class ArrayLists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int quit = 0;
		Scanner read = new Scanner(System.in);
		ArrayList<Point> pointArray = new ArrayList<Point>();
		String temp = new String(); 
		
		System.out.println("Jacob Knight");
		System.out.println("You can quit at any time by typing Q.");
		try{
		System.out.println("What is the first point? (x,y)");
		temp = read.nextLine();
		if(temp.equals("Q")||temp.equals("q")){
			System.out.println("Thanks for playing.");
			quit = 1;
		}else{
		Point point1 = new Point(Double.parseDouble(temp.substring(1, temp.indexOf(","))),Double.parseDouble(temp.substring(temp.indexOf(",")+1,temp.length()-1)));
		
		while(quit == 0){
			System.out.println("What is the next point? (x,y)");
			temp = read.nextLine();
			if(temp.equals("Q")||temp.equals("q")){
				System.out.println("Thanks for playing.");
				quit = 1;
			} else { 
			pointArray.add(new Point(Double.parseDouble(temp.substring(1, temp.indexOf(","))),Double.parseDouble(temp.substring(temp.indexOf(",")+1,temp.length()-1))));
			System.out.println("The distances are.");
			for(int ii = 0; ii < pointArray.size();ii++){
				System.out.println(Math.sqrt((pointArray.get(ii).getX() - point1.getX()) * (pointArray.get(ii).getX() - point1.getX())+ (pointArray.get(ii).getY() -point1.getY())*(pointArray.get(ii).getY() -point1.getY())));
			}
			}
		}}
		}catch(Exception e){
			System.out.println("That wasnt an acceptable input please put in you points as (x,y)");
		}

	}

}
