def getHead(title):
    print("""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>""", title, """</title>

        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
        <link rel="icon" href="imageLib/KnightLogoTB.gif" type="image/gif">
        <link rel="stylesheet" href="css/master.css" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Playfair+Display+SC" rel="stylesheet">
        <link rel="stylesheet" href="css/bootstrap.vertical-tabs.css">
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
            <![endif]-->
    </head>    
    """)
    
def getHeader():
    print("""<body>
        <div id="box" class="container-fixed">
            <div class="row">
                <div class="col-sm-12">
                    <nav class="navbar navbar-fixed-top navbar-inverse">
                        <div class="container">
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                    <span class="sr-only">Toggle navigation</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                                <a class="navbar-brand" href="../JacobKnight"><img src="imageLib/KnightLogoXS.gif" alt="Knight Programming Logo"></a>
                            </div>

                            <!-- Collect the nav links, forms, and other content for toggling -->
                            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                                <ul class="nav navbar-nav">
                                    <li><a href="resume.py#content">Resume</a></li>
                                    <li class="dropdown">
                                        <a href="process.py" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Process<span class="caret"></span></a>
                                        <ul class="dropdown-menu">
                                            <li><a href="process.py#content">Steps</a></li>
                                        </ul>
                                    </li>
                                    <li class="dropdown">
                                        <a href="projects.py" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Projects<span class="caret"></span></a>
                                        <ul class="dropdown-menu">
                                            <li><a href="projects.py#content">Dragon Quest</a></li>
                                            <li><a href="projects.py#knight">Knight Programming</a></li>
                                        </ul>
                                    </li>
                                    <li class="dropdown">
                                        <a href="hobbies.py" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Hobbies <span class="caret"></span></a>
                                        <ul class="dropdown-menu">
                                            <li><a href="hobbies.py#content">Hobbies</a></li>
                                        </ul>
                                    </li>
                                    <li><a href="courseWork.py#content">Course Work</a></li>
                                </ul>
                                <ul class="nav navbar-nav navbar-right">
                                    <li><a href="#" data-toggle="modal" data-target=".modalContact"> Contact</a></li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                </div>
            </div>
            <div class="modal fade modalContact" tabindex="-1" role="dialog" aria-labelledby="Contact Me">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="col-xs-1">
                    </div>
                    <div class="col-xs-10">
                    <form>
                        <div class="form-group">
                            <br>
                            <input type="text" class="form-control" id="ContactName" aria-describedby="nameHelp" placeholder="Enter Full Name">
                            <br>
                            <input type="email" class="form-control" id="ContactEmail" aria-describedby="emailHelp" placeholder="Enter email">
                            <br>
                            <input type="Subject" class="form-control" id="Subject" area-describedby="subject" placeholder="Subject">
                            <br>
                            <textarea class="form-control" rows="25" id="message">Enter Message</textarea>
                            <br>
                            <button class="btn btn-primary" name="submit">Send</button>
                        </div>
                    </form>
                    </div>
                </div>
              </div>
            </div>
            <div id="Title" class="row">
                <div class="col-xs-12">
                    <h1>Jacob Knight</h1>
                    <h2>Solution Development</h2>
                    <h3>Web/Software</h3>
                </div>
                <div id="down">
                    <a href="#content"><span class="glyphicon glyphicon-triangle-bottom" aria-hidden="true"></span></a>
                </div>
            </div>
        </div>
            <p><a name="content"></a></p>
    """)
    
def getFoot():
    print("""
        <footer id="FootNav" class="container-float">
            <div class="row">
                <div class="col-xs-12 col-md-3">
                    <img src="imageLib/siteMapMD.gif" alt="" usemap="#MapXS" />
                    <map name="MapXS" id="MapXS">
                        <area alt="Home" title="Home" href="index.py" shape="rect" coords="131,12,194,59" />
                        <area alt="Resume" title="Resume" href="resume.py" shape="rect" coords="28,74,90,112" />
                        <area alt="ResumeDoc" title="ResumeDoc" href="resume.py#content" shape="rect" coords="30,113,89,158" />
                        <area alt="Process" title="Process" href="process.py" shape="rect" coords="98,75,160,113" />
                        <area alt="Steps" title="Steps" href="process.py#content" shape="rect" coords="99,114,159,150" />
                        <area alt="Example" title="Example" href="process.py#eg" shape="rect" coords="97,152,159,198" />
                        <area alt="Projects" title="Projects" href="projects.py" shape="rect" coords="166,75,228,113" />
                        <area alt="DragonQuest" title="DragonQuest" href="projects.py#content" shape="rect" coords="165,114,228,150" />
                        <area alt="KnightProgramming" title="KnightProgramming" href="projects.py#content" shape="rect" coords="166,152,229,198" />
                        <area alt="Hobbies" title="Hobbies" href="hobbies.py" shape="rect" coords="236,75,298,112" />
                        <area alt="Programming" title="Programming" href="hobbies.py#content" shape="rect" coords="236,115,296,152" />
                        <area alt="Robotics" title="Robotics" href="hobbies.py#content" shape="rect" coords="237,154,296,190" />
                        <area alt="Music" title="Music" href="hobbies.py#content" shape="rect" coords="237,191,299,236" />
                    </map>
                </div>
                <div class="col-xs-12 col-md-9">
                    <div class="col-md-1">
                    </div>
                    <div class="col-md-11">
                    <table class="table table-hover">
                        <thead class="head-default">
                            
                        </thead>
                        <tbody>
                            <tr>
                                <th><a href="index.py">Home Page</a></th>
                                <th><a href="process.py">Process</a></th>
                                <th><a href="projects.py">Project</a></th>
                                <th><a href="hobbies.py">Hobbies</a></th>
                            </tr>
                            <tr>
                                <td scope="row"><a href="#" data-toggle="modal" data-target=".modalContact"> Contact</a></td>
                                <td><a href="process.py#content">Steps</a></td>
                                <td><a href="projects.py#content">Dragon Quest</a></td>
                                <td><a href="hobbies.py#content">Programming</a></td>
                            </tr>
                            <tr>
                                <td scope="row"><a href="resume.py">Resume</a></td>
                                <td><a href="process.py#demo">Demo</a></td>
                                <td><a href="projects.py#knight">Knight Programming</a></td>
                                <td><a href="hobbies.py#content">Music</a></td>
                            </tr>
                        </tbody>
                    </table>
                    </div>
                </div>
            </div>
        </footer>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    </body>

    </html>
    """)