import javafx.application.Application;
import javafx.stage.Stage;
import javafx.fxml.*;
import javafx.scene.*;
import javafx.stage.Stage;
import javafx.event.*;
import javafx.scene.control.*;

public class DistanceCalculator extends Application {

	@FXML
	TextField rx1;
	@FXML
	TextField rx2;
	@FXML
	TextField ry1;
	@FXML
	TextField ry2;
	@FXML
	Button calc;
	@FXML
	Slider Ymin;
	@FXML
	Slider Xmin;
	@FXML
	Label Solution;

	@FXML
	public void Calc(ActionEvent event) {
		double x1 = 0;
		double x2 = 0;
		double y1 = 0;
		double y2 = 0;
		int valid = 1;
		try {
			x1 = Double.parseDouble(rx1.getText());
			x2 = Double.parseDouble(rx2.getText());
			y1 = Double.parseDouble(ry1.getText());
			y2 = Double.parseDouble(ry2.getText());
		} catch (NumberFormatException e) {
			Solution.setText("No non numeric vlaues allowed.");
			valid = 0;
		}
		if (valid == 1) {
			double yMin = Ymin.getValue();
			double xMin = Xmin.getValue();
			double d = Math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1));
			if (x1 >= xMin || x2 >= xMin || y1 >= yMin || y2 >= yMin) {
				Solution.setText("Jacob Knigt:  The distance between (" + x1 + "," + y1 + ") and (" + x2 + "," + y2
						+ ") is " + d);
			} else {
				Solution.setText("one or more of your points is out of bounds." + xMin + " " + yMin);
			}
		}
	}

	public void start(Stage primaryStage) throws Exception {
		FXMLLoader loader = new FXMLLoader(getClass().getResource("DistanceCalc.fxml"));
		loader.setController(this);
		Parent root = loader.load();

		Scene myScene = new Scene(root, 500, 700); // change the width and
													// height as you may like
		primaryStage.setScene(myScene);
		primaryStage.show();
	}

	public static void main(String[] args) {
		launch(args);
	}
}