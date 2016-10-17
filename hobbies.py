#!/usr/bin/python3
import cgi
import HTML

print("Content-type: text/html\n\n")

HTML.getHead("Home")
HTML.getHeader()
print("""
     <div class="container-float">
        <div class="row">
            <div class="col-xs-12">
                <div class="row">
                    <div class="col-xs-1 col-md-2">
                        <a name="resume"></a>
                    </div>
                    <div id="Main" class="col-xs-10 col-md-8">
                        <div>

                            <!-- Nav tabs -->
                            <ul class="nav nav-tabs" role="tablist">
                                <li role="presentation"><a href="#Programming" aria-controls="home" role="tab" data-toggle="tab">Programming</a></li>
                                <li role="presentation"><a href="#robotics" aria-controls="robotics" role="tab" data-toggle="tab">Robotics</a></li>
                                <li role="presentation"><a href="#gaming" aria-controls="gaming" role="tab" data-toggle="tab">Gaming</a></li>
                                <li role="presentation"><a href="#music" aria-controls="music" role="tab" data-toggle="tab">Music</a></li>
                            </ul>

                            <!-- Tab panes -->
                            <div class="tab-content">
                                <div role="tabpanel" class="tab-pane active" id="Programming">
                                <br>
                                    <h1>Programming</h1>
                                    <br>
                                    <div class="embed-responsive embed-responsive-16by9">
                                  <iframe width="560" height="315" src="https://www.youtube.com/embed/GFYT7Lqt1h8?list=PLlrATfBNZ98eOOCk2fOFg7Qg5yoQfFAdf" frameborder="0" allowfullscreen></iframe>
                                </div>
                                    <br>
                                    <p>
                                        I love Programming and this is one of my favorite searies. I hope you like it. Special thanks to Cherno who helped me build my first game.
                                    </p>
                                </div>
                                <div role="tabpanel" class="tab-pane" id="robotics">
                                <br>
                                <h1>Robotics</h1>
                                <br>
                                    <div>
                                    <img class="wide" src="imageLib/robotics.jpg" alt="Robotics pictures">
                                    </div>
                                        <br>
                                    <p>I have loved robotics since I was 12 I used to run a first robotics team and like building robots and Quad Copters.</p>
                                </div>
                                <div role="tabpanel" class="tab-pane" id="gaming">
                                    <br>
                                    <h1>Gaming</h1>
                                    <br>
                                    <div>
                                    <img class="wide" src="imageLib/TableTop.jpg" alt="Table top gaming colage">
                                    </div>
                                        <br>
                                    <p>I love all table top gameing and have since I was young. I am a nerd through and through. I love playing and GM/DMing and everything inbetween.</p>
                                </div>
                                <div role="tabpanel" class="tab-pane" id="music">
                                    <h1>Music</h1>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
HTML.getFoot()

