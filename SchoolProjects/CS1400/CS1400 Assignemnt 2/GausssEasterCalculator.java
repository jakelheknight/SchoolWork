import java.util.Scanner;

public class GausssEasterCalculator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner year = new Scanner(System.in);
			System.out.println("enter the year. ");
			int y = year.nextInt();
			//int y = 2001;
			int a = y%19;
			int b = y/100;
			int c = y%100;
			int d = b/4;
			int e = b%4;
			int g = (8*b+13)/25;
			int h = (19*a+b-d-g+15)%30;
			int j = c/4;
			int k = c%4;
			int m = (a+11*h)/319;
			int r = (2*e+2*j-k-h+m+32)%7;
			int n = (h-m+r+90)/25;
			int p = (h-m+r+n+19)%32;
			String month = "";
			if(n == 3){
				month = "March";
			}else{
				month = "April";
			}
			System.out.println(
					"Easter will be on " + month + "," + p + "."
					);
	}

}
