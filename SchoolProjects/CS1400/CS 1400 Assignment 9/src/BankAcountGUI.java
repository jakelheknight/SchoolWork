import javafx.application.Application;
import javafx.stage.*;
import javafx.fxml.*;
import javafx.scene.*;
import javafx.event.*;
import javafx.scene.control.*;
import javafx.scene.input.*;

public class BankAcountGUI extends Application {

    //add the fxml controls and fxml event methods here
    @FXML RadioButton deposit;
    @FXML RadioButton withdraw;
    @FXML RadioButton info;
    @FXML RadioButton exit;
    @FXML TextField money;
    @FXML TextArea Out;
    BankAccount Account = new BankAccount("John Doe", 12345 );
    
    @FXML protected void runProcess(){
    	double input = 0;
    	try {
    		input = Double.parseDouble(money.getText());if(deposit.isSelected()){
        		Account.deposit(input);
        		Out.setText("Success, your new ballance is  " + Account.getBalance());
        	} else if(withdraw.isSelected()){
        		Account.withdraw(input);
        		Out.setText("Success, your new ballance is  " + Account.getBalance());
        	} else if(info.isSelected()){
        		Out.setText("Name: " + Account.getName() + "\nAccount #: " + Account.getAccountNum()
        		+"\nBalance: $" + Account.getBalance());
        	} else if(exit.isSelected()){
        		System.exit(0);
        	}
    	}catch(NumberFormatException e){
    		Out.setText("Pleas enter a valid amount.");
    	}
    }
    
    
    public void start(Stage primaryStage) throws Exception {
    	FXMLLoader loader = new FXMLLoader(getClass().getResource("BankAcountGUI.fxml"));
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

