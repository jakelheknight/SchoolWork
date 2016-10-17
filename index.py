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
                    </div>
                    <div id="Main" class="col-xs-10 col-md-8">
                        <h1>Welcome to my Online Portfolio</h1>
                        <hr>
                        <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
                            <!-- Indicators -->
                            <ol class="carousel-indicators">
                                <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                            </ol>

                            <!-- Wrapper for slides -->
                            <div class="carousel-inner" role="listbox">
                                <div class="item active">
                                    <a href="process.py#content"><img src="imageLib/lucidChartMap.jpg" alt="First draft sight map"></a>
                                </div>
                                <div class="item">
                                    <a href="projects.py#content"><img src="imageLib/CurrentProject.jpg" alt="Current Project"></a>
                                </div>
                                <div class="item">
                                    <a href="hobbies.py#content"><img src="imageLib/Hobbies.jpg" alt="Current Project"></a>
                                </div>
                            </div>

                            <!-- Controls -->
                            <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>
                        <div>
                            <br>
                            <p>As you have probably already guessed my name is Jacob Knight and I want to program your next solution for you. I am a hard working professional developer and first class problem solver. I got my first Bachelor's Degree in THeoretical Physics and am working on a second degree in Computer Science. I have been an industrial technician, physics teacher, mathematics programmer, program analyst and now your professional Solutions Expert.</p>
                            <br>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
HTML.getFoot()

