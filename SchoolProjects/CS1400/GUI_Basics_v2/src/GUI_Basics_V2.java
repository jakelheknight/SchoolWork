import javafx.application.Application;
import javafx.stage.Stage;
import javafx.fxml.*;
import javafx.scene.*;
import javafx.stage.Stage;
import javafx.event.*;
import javafx.scene.control.*;
import javafx.scene.input.*;

public class GUI_Basics_V2 extends Application {

	//add the fxml controls and fxml event methods here

	@FXML TextField myTextField;
	@FXML Button myButton;
	@FXML Label valitity;
	@FXML Label output;

	@FXML protected void execute(ActionEvent event) {
		String input = myTextField.getText();
		if(input.equals("one")){
			valitity.setText("Valid");
			output.setText("One is the lonliest number");
		}
		else if(input.equals("")){				
			valitity.setText("Valid");
			output.setText("empty");
		}else{					
			valitity.setText("Invalid");
			output.setText("Invalid Entry");				
		}
	}

	public void start(Stage primaryStage) throws Exception {
		FXMLLoader loader = new FXMLLoader(getClass().getResource("GUI_Basics_V2.fxml"));
		loader.setController(this);
		Parent root = loader.load();

		Scene myScene = new Scene(root,420,450); //change the width and height as you may like
		primaryStage.setScene(myScene);
		primaryStage.show();
	}

	public static void main(String[] args) {
		launch(args);
	}
}