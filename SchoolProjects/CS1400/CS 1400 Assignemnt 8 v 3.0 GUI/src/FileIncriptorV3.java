import javafx.application.Application;
import javafx.fxml.*;
import javafx.scene.*;
import javafx.stage.*;
import javafx.event.*;
import javafx.scene.control.*;
import javafx.scene.input.*;
import java.util.*;
import java.io.*;

public class FileIncriptorV3 extends Application {

	// add the fxml controls and fxml event methods here
	Stage primary;
	@FXML
	TextArea en1;
	
	@FXML
	TextArea en2;
	
	@FXML
	protected void callFileChooser() {
		String input = "";
		FileChooser fc = new FileChooser();
		File myFile = fc.showOpenDialog(primary);
		try {
			Scanner in = new Scanner(myFile);
			PrintWriter Fout1 = new PrintWriter(new File("Encripted1.txt"));
			PrintWriter Fout2 = new PrintWriter(new File("Encripted2.txt"));
			while (in.hasNext() == true) {
				input = input + "\n" + in.nextLine();
			}
			String Enc1 = Encryption1(input);
			String Enc2 = Encryption2(input);
			Fout1.println(Enc1);
			Fout2.println(Enc2);
			in.close();
			en1.setText(Enc1);
			en2.setText(Enc2);
		} catch (FileNotFoundException e) {
			System.out.println("could not find the file.");
		}
	}

	public void start(Stage primaryStage) throws Exception {
		primary = primaryStage;
		FXMLLoader loader = new FXMLLoader(getClass().getResource("EncriptionGUI.fxml"));
		loader.setController(this);
		Parent root = loader.load();

		Scene myScene = new Scene(root, 400, 400); // change the width and
													// height as you may like
		primaryStage.setScene(myScene);
		primaryStage.show();
	}

	// ------------------------------------------------------------------------------------------------------------
	public static void main(String[] args) {
		launch(args);
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
			char C = Finput.charAt(ii);
			int ASCII = (int) C;
			if (ASCII >= 97 && ASCII < 122) {
				Out = Out + (ASCII - 96);
			} else if (ASCII >= 65 && ASCII < 90) {
				Out = Out + (ASCII - 39);
			} else if(Character.isDigit(C)){
				if(C == '0'){
					
				} else if(C == '0'){
				 Out = Out +"Ze";	
				} else if(C == '1'){
					Out = Out +"On";
				} else if(C == '2'){
					Out = Out +"Tw";
				} else if(C == '3'){
					Out = Out +"Th";
				} else if(C == '4'){
					Out = Out +"Fo";
				} else if(C == '5'){
					Out = Out +"Fi";
				} else if(C == '6'){
					Out = Out +"Si";
				} else if(C == '7'){
					Out = Out +"Se";
				} else if(C == '8'){
					Out = Out +"Ea";
				} else if(C == '9'){
					Out = Out +"Ni";
				}
				
			} else {
				Out = Out + Finput.charAt(ii);
			}
		}
		return Out;
	}

}
