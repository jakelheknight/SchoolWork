#!/usr/bin/python3
import cgi
import HTML

print("Content-type: text/html\n\n")

HTML.getHead("Process")
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
                    <br>
                    <h1>Process</h1>
                    <p>Solution development is more about the process than the coding. 80% of the process comes before you build anything. You need to start with a big box of questions and a good problem to sit down with.</p>
                    <div class="col-xs-1">
                    </div>
                    <div class="col-xs-10">
                        <br>
                        <div class="row">
                            <div class="col-xs-1">
                            </div>
                            <div class="col-xs-11">
                                <p><b>Step One:</b> Define the problem. Every problem needs to be well defined. It is important that you only define a problem. Don’t start trying to solve it yet.</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-11">
                                <p><b>Step Two:</b> You need to take that well defined problem and break it down. You need to chunk it out into sub problems that can be solved all by themselves.</p>
                            </div>
                            <div class="col-xs-1">
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-1">
                            </div>
                            <div class="col-xs-11">
                                <p><b>Step Three:</b> Next, I think of tests. I break <u>one</u> sub problem down into testable chunks. There is no mistake in breaking problems down that show up twice.</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-11">
                                <p><b>Step Four: </b>It’s time to really flesh out one testable chunk. This is also the time you will need to choose what tools you want to use and what should be included when you release Version 1 of your project. (If you don’t set a release point now your solution will never be released due to scope creep. When you revisit this step keep the scope from growing.)</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-1">
                            </div>
                            <div class="col-xs-11">
                                <p><b>Step five:</b> Now it’s time to ask 3 questions. What does this code need to do? How does this code interface with the rest of the project and the user? What does this code need in order to do what it is designed to do?</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-11">
                                <p><b>Step Six:</b> : Use the answers to the previous questions to break up the task again. Focus on one piece at a time. Map out large connections or a sight map and document data and necessary functions.</p>
                            </div>
                            <div class="col-xs-1">
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-1">
                            </div>
                            <div class="col-xs-11">
                                <p><b>Step Seven:</b>Now it’s time to write some pseudo code. Make diagrams and plan your approach. Talk to people and make sure you have a clear path.</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-11">
                                <p><b>Step Eight: </b>Write the code testing as you go. Document before you code then remove documentation as necessary. Don’t put the cart before the horse. Redesigning can take longer than doing it right the first time.</p>
                            </div>
                        </div>

                        <br>
                        <div class="row">
                            <div class="col-xs-1">
                            </div>
                            <div class="col-xs-11">
                                <p><b>Step Nine:</b> Repeat steps four through eight as needed. As you do this beware of scope creep, the number one killer of solutions. You can add versions with your great ideas after the first release.</p>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-xs-11">
                                <p><b>Step Ten: </b>: Finally, check to see if that solution works and move on to another sub problem or add features to the problem you've been working on.</p>
                            </div>
                        </div>
                        <a name="eg"></a>
                        <br>
                        <br>
                    </div>
                    <div class="row">
                        <h1>Example Coming Soon</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""")
HTML.getFoot()

