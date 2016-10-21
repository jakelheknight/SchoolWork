#!/usr/bin/python3
import cgi
import HTML

print("Content-type: text/html\n\n")

HTML.getHead("Course Work")
HTML.getHeader()
print("""
<div class="container-float">
    <div class="row">
        <div class="col-xs-12">
            <div class="row">
                <div class="col-xs-0 col-md-2">
                    <a name="content"></a>
                </div>
                <div id="Main" class="col-xs-12 col-md-8">
                    <div class="panel panel-success">
                        <!-- Default panel contents -->
                        <div class="panel-heading">
                            <h1>Course Work</h1></div>
                        <div class="panel-body">
                            <div class="col-xs-3">
                                <!-- required for floating -->
                                <!-- Nav tabs -->
                                <ul class="nav nav-tabs tabs-left">
                                    <li><a href="#CS1030" data-toggle="tab">CS1030 Intro to Computer Sci</a></li>
                                    <li><a href="#CS1400" data-toggle="tab">CS1400 Programming I</a></li>
                                    <li><a href="#CS1410" data-toggle="tab">CS1410 Programming II</a></li>
                                    <li class="active"><a href="#CS2350" data-toggle="tab">CS2350 Web Programming</a></li>
                                </ul>
                            </div>

                            <div class="col-xs-9">
                                <!-- Tab panes -->
                                <div class="tab-content">
                                    <div class="tab-pane" id="CS1030">
                                        <div class="panel panel-default">
                                            <!-- Default panel contents -->
                                            <div class="panel-heading">
                                                <h2>1030 Intoro to Computer science</h2></div>
                                            <div class="panel-body">
                                                <p>A first course in computer science. This course covers a broad range of topics from computer architecture and transistor to data storage and basic programming.</p>
                                                <p>This class focused on Python3 programming so I will provide source code only since python is a scripted language and it is hard to package as an executable file.</p>
                                            </div>
                                            <!-- Table -->
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th>Assignemnt</th>
                                                        <th>Source Code</th>
                                                        <th colspan="2">Description</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>100 Factorial</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/100Fac.py" target="_blank">100Fac.py</a></td>
                                                        <td>A program to calculate 100 Factorial</td>
                                                    </tr>
                                                    <tr>
                                                        <td>BillCalculator</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/BIllCalcuator.py" target="_blank">BillCalcuator.py</a></td>
                                                        <td>A program to calculate Tax and Tip</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Grade Calculator</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/GradCalc.py" target="_blank">GradeCalc.py</a></td>
                                                        <td>A program to calculate grades</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Farinheight to Celsius</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/FarToCel3.py" target="_blank">FerToCel.py</a></td>
                                                        <td>A program to convert from F to C and C to F</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Pay Calculator</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/PayCalculator.py" target="_blank">PayCalculator.py</a></td>
                                                        <td>A program to calculate paychecks</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Pizza Price</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/PizzaPrice.py" target="_blank">PizzaPrice.py</a></td>
                                                        <td>A program to calculate Pizza cost</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Register</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/Register.py" target="_blank">Register.py</a></td>
                                                        <td>A program to keep track of registration.</td>
                                                    </tr>
                                                    <tr>
                                                        <td>Final</td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/blob/master/SchoolProjects/CS1030/Final.py" target="_blank">Final.py</a></td>
                                                        <td>A program to keep track of car sales</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="CS1400">
                                        <div class="panel panel-default">
                                            <!-- Default panel contents -->
                                            <div class="panel-heading">
                                                <h2>1400 Programming I</h2>
                                                <h3>Java Programming</h3></div>
                                            <div class="panel-body">
                                                <p>A first course in programming. Mainly focused on Java. There was a lot of fun stuff including introduction go GUI's</p>
                                            </div>
                                            <!-- Table -->
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th>Assignemnt</th>
                                                        <th>Source Code</th>
                                                        <th colspan="2">Description</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td colspan="4">Coming Soon</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="CS1410">
                                        <div class="panel panel-default">
                                            <!-- Default panel contents -->
                                            <div class="panel-heading">
                                                <h2>1410 Programming I</h2><h3>Object Oriented Programming</h3></div>
                                            <div class="panel-body">
                                                <p>An introduction to Object oriented programming taught in C++.</p>
                                            </div>
                                            <!-- Table -->
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th>Exicutable</th>
                                                        <th>Source Code</th>
                                                        <th colspan="2">Description</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td colspan="4">Coming soon</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div class="tab-pane active" id="CS2350">
                                        <div class="panel panel-default">
                                            <!-- Default panel contents -->
                                            <div class="panel-heading">
                                                <h2>2350 Web Programming</h2></div>
                                            <div class="panel-body">
                                                <p>An introductory course in HTML CSS JavaScript and JQuery. It's this course I wrote this site for.</p>
                                            </div>
                                            <!-- Table -->
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th>Assignemnt Link</th>
                                                        <th>Source Code</th>
                                                        <th colspan="2">Description</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td><a href="SchoolProjects/CS2350/A1-2/index.html"> Assignment 1-2</a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/tree/master/SchoolProjects/CS2350/A1-2" target="_blank">About Me</a></td>
                                                        <td>Getting to know you.</td>
                                                    </tr>
                                                    <tr>
                                                        <td><a href="SchoolProjects/CS2350/A2-2/A2-2.html"> Assignment 2 </a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/tree/master/SchoolProjects/CS2350/A2-2" target="_blank">New Yourk</a></td>
                                                        <td>A basic Document made in HTML</td>
                                                    </tr>
                                                    <tr>
                                                        <td><a href="SchoolProjects/CS2350/A3-1/index.html"> Assignment 3</a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/tree/master/SchoolProjects/CS2350/A3-1" target="_blank">Forms and Tables</a></td>
                                                        <td>Forms and Tables :)</td>
                                                    </tr>
                                                    <tr>
                                                        <td><a href="SchoolProjects/CS2350/A4-1/index.html"> Assignment 4 </a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/tree/master/SchoolProjects/CS2350/A4-1" target="_blank">CSS practice</a></td>
                                                        <td>A scary site with way to much CSS.</td>
                                                    </tr>
                                                    <tr>
                                                        <td><a href="SchoolProjects/CS2350/A5-1/index.html"> Assignment 5 </a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork/tree/master/SchoolProjects/CS2350/A5-1" target="_blank">Wildcat CS</a></td>
                                                        <td>A fake Weber state CS page.</td>
                                                    </tr>
                                                    <tr>
                                                        <td><a href="index.py">Portfolio</a></td>
                                                        <td><a href="https://github.com/jakelheknight/SchoolWork" target="_blank">Portfolio</a></td>
                                                        <td>Mid term Portfolio Project</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
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

