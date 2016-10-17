import javafx.animation.*;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.util.Duration;
 
public class Drawings extends Application {
 
    public static void main(String[] args) {
        launch(args);
    }
 
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Drawing Operations Test");
        Group root = new Group();
        Canvas canvas = new Canvas(700, 700);
        GraphicsContext gc = canvas.getGraphicsContext2D();
        drawShapes(gc);
        root.getChildren().add(canvas);
        Circle c = new Circle(350,347,5);
        Rectangle r = new Rectangle(300, 50, 100, 50);
        r.setFill(Color.RED); 
        root.getChildren().add(r);
        root.getChildren().add(c);
        
        TranslateTransition translate = 
                new TranslateTransition(Duration.millis(750)); 
                translate.setToX(0); 
                translate.setToY(-350); 
        
                ParallelTransition transition = new ParallelTransition(c, 
                        translate); 
                        transition.setCycleCount(Timeline.INDEFINITE);
                        transition.play(); 
                
        primaryStage.setScene(new Scene(root));
        primaryStage.show();
    }

    private void drawShapes(GraphicsContext gc) {
    	double center = 700/2;
    	double size = 10;
    	gc.setFill(Color.GREEN);
        gc.fillPolygon(new double[]{center-size, center, center+size, center},
                       new double[]{center+size, center, center+size, center-2*size}, 4);
        gc.strokePolygon(new double[]{center-size*2, center, center+size*2, center},
                       new double[]{center+size*2, center, center+size*2, center-4*size}, 4);
        gc.fillRect(center-20,center+50, 40, 40);
    }
}