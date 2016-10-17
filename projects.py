#!/usr/bin/python3
import cgi
import HTML

print("Content-type: text/html\n\n")

HTML.getHead("Projects")
HTML.getHeader()
print("""
    <div class="container-float">
        <div class="row">
            <div class="col-xs-12">
                <div class="row">
                    <div class="col-xs-1 col-md-2">
                        <a name="content"></a>
                    </div>
                    <div id="Main" class="col-xs-10 col-md-8">
                        <h1>Project: Dragon Quest</h1>
                        <div>
                            <br>
                            <p>Dragon quest is an amazing table top game. This game is fun but it is complex and the math involved can be combersome even a deal breakter for some people. I was thinking of different solutions. Get smarter friends... Provide ti-83 calcualtors as DM... Switch do D&D... None of these sounded good. So I decided to make a solution that could do the math for us. This is not to replace a DM or dice. It is just to keep track of stats and percent chances so that the game can be fluidly played. If you click the picture below a PDF of the rules will download. Get aquainted with them.</p>
                            <br>
                            <div class="row">
                                <div class="col-xs-12">
                                    <a href="#"><img id="DQrul" class="img-responsive" src="imageLib/DragonQuestCover.jpg" alt="Dragon Quest Rule Book"></a>
                                </div>
                            </div>
                            <br>
                            <br>
                        </div>
                        <h1>Dragon Quest Nerrowing the problem down</h1>
                        <br>
                        <div>
                            <p>There are two roles in Dragon quest. Players who each play one or more charicters, and a GM(Game Master) The player has to keep track of his players stats, items health fatigue and about 20 other things to play. The DM has to keep track of Non Player Charicters, monsters, map, story, and players all at once. There are lots of places where we could use computers to make the game easier to play but I chose to focus on Charicter sheets. The GM and players use them and eventually we can integrate them into a full scale game tracker with everything a GM and player could need.</p>
                        </div>
                         <h1>Lets break down a charicter sheet</h1>
                        <div>
                            <p>Next we need to hack out what is needed for this application to be useful and define the minimum list of features that can accomplish the task. In order for a charicter sheet to really work we need the sheet itself to be a web aplication. 1 It needs to show the sheet in a format that players are used to. 2 It needs to let players buld sheets and 3 level/modify built sheets. 4 It needs to keep track of who built each sheet and 5 allow them to reach the sheets they built.</p>
                            <p>The first task I think needs to be focused on is building a sheet that can present test data pulled from a database. I think the best format for this is a web application with linked database for storage of Charicters. The tools I will be using are HTML 5, CSS 3, JavaScript, Angular, mySQL, and python or node.JS server. </p>
                        </div>
                            <br>
                        <h1>Basic Charicter Sheet</h1>
                        <div class="row">
                            <div class="col-md-6">
                                <p>The basic charicter sheet can be broken into the following sections. Each section needs to be layed out in HTML with css to make it so that it looks good and is easy to read. Then each cell needs to be either filled wiht data pulled from the database or calcuated from other pieces of data that are already on the sheet. We also need to setup a database to keep track of charicters and all the data that belons to each one as well as who it belings too.</p>
                            </div>
                            <div class="col-md-6">
                                <img id="CSBreakdown" src="imageLib/CharSheetBreakdown.jpg" alt="Charicter Sheet Break Down">
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <br>
                            <div class="col-md-6">
                                <img id="DataBase" src="imageLib/database.jpg">
                            </div>
                            <div class="col-md-6">
                                <p>This is the ER Diagram for the database that is being used. The database is laied out and the sheet is begining to take shape I have already built the database and linked it the the Primary stats. Heres a Link to the <a href="">Work in Progress</a></p>
                            </div>
                        </div>
                        <a name="knight"></a>
                        <br>
                        <br>
                        <h1>Knight Programming</h1>
                        <br>
                        <div>
                            <p>Knight Programming is my small websight devoted to holding my and other students portfolios in an inviroment that allwos them to be built and maintained by students as well as have acces to all the inerds of a server. So far it is just me but I hope it will grow.</p>
                        </div>
                        <br>
                        <br>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
HTML.getFoot()

