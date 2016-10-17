#!/usr/bin/python3
import cgi
import HTML

print("Content-type: text/html\n\n")

HTML.getHead("Resume")
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
                        <a name="resume"></a>
                        <iframe src="imageLib/JacobKnightResume.html"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
HTML.getFoot()

