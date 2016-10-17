

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.fxml.*;
import javafx.scene.*;
import javafx.stage.Stage;
import javafx.event.*;
import javafx.scene.control.*;

public class FirstGUI extends Application {

    //add the fxml controls and fxml event methods here
	@FXML protected void execute(ActionEvent event) {
		 //implement your logic here.
		}

	@FXML TextField myTextField;
	@FXML Button myButton;
	@FXML Label validation;
	@FXML Label output;
    
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("GUI_Basics.fxml"));
        loader.setController(this);
        Parent root = loader.load();

        Scene myScene = new Scene(root,400,400); //change the width and height as you may like
        primaryStage.setScene(myScene);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}