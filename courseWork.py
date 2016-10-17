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
                <div class="col-xs-1 col-md-2">
                    <a name="content"></a>
                </div>
                <div id="Main" class="col-xs-10 col-md-8">
                    <div class="panel panel-success">
                                  <!-- Default panel contents -->
                        <div class="panel-heading"><h1>Course Work</h1></div>
                                  <div class="panel-body">
                    <div class="col-xs-3">
                        <!-- required for floating -->
                        <!-- Nav tabs -->
                        <ul class="nav nav-tabs tabs-left">
                            <li class="active"><a href="#CS1030" data-toggle="tab">CS1030 Intro to Computer Sci</a></li>
                            <li><a href="#CS1400" data-toggle="tab">CS1400 Programming I</a></li>
                            <li><a href="#CS1410" data-toggle="tab">CS1410 Programming II</a></li>
                            <li><a href="#CS2350" data-toggle="tab">CS2350 Web Programming</a></li>
                        </ul>
                    </div>

                    <div class="col-xs-9">
                        <!-- Tab panes -->
                        <div class="tab-content">
                            <div class="tab-pane active" id="CS1030">                                
                                <div class="panel panel-default">
                                  <!-- Default panel contents -->
                                  <div class="panel-heading"><h2>1030 Intoro to Computer science</h2></div>
                                  <div class="panel-body">
                                      <p>A first course in computer science. This course covers a broad range of topics from computer arcetecture and transisters to data storage and basic programming.</p><p>This class focused on Python3 programming so I will provide source code only since python is a scripted language and it is hard to package as an exicutable file.</p>
                                  </div>
                                  <!-- Table -->
                                  <table class="table">
                                        <thead>
                                            <tr>    
                                                <th>Assignemnt</th><th>Source Code</th><th colspan="2">Description</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>100 Factorial</td><td><a href="ScoolWork/CS1030/100Fac.py" download>100Fac.py</a></td><td>A symple program to calcuate 100 Factorial</td>
                                            </tr>
                                      </tbody>
                                  </table>
                                </div>
                            </div>
                            <div class="tab-pane" id="CS1400">
                                <h2>1400 Programming I</h2>
                            </div>
                            <div class="tab-pane" id="CS1410">
                                <h2>1410 Programming II</h2>
                                <h3>Object Orented Programming</h3>
                            </div>
                            <div class="tab-pane" id="CS2350">
                                <h2>Web Programming I</h2>
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

