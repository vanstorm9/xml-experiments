editorStr = """
<div id="page-content-wrapper">
                <div id="div_editorpanel">
                    <div id="span_currentfolder"> 
                        <!-- Current folder: -->
                        <span id="span_currentfolderid">
                            <?php 
                                if (isset($_SESSION["currentfolder"])) {
                                    echo $_SESSION["currentfolder"];
                                }
                            ?>
                        </span> 
                    </div>
                    <div id="span_currentfile"> 
                        Current file:
                        <span id="span_currentfileid">
                            <?php 
                                if (isset($_SESSION["currentfile"])) {
                                    echo $_SESSION["currentfile"];
                                } else {
                                    echo "untitled";
                                }
                            ?>
                        </span> 
                    </div>

                    <div id="div_fontsize">
                        <span> Font size: </span>
                        <select id="select_fontsize">
                            <option value="8">8px</option>
                            <option value="12" selected="selected">12px</option>
                            <option value="18">18px</option>
                            <option value="24">24px</option>
                            <option value="36">36px</option>
                            <option value="72">72px</option>
                        </select>
                    </div>

                    <!-- <div id="page-content-wrapper"> -->
                    <div id="editor"></div>
                </div>
                <div id="column-resizer"></div>
                <div id="results"></div>
                <!-- </div> -->
            </div>
        </div> <!-- wrapper -->
"""

bottomJS = """

<!-- **** END OF LOGIN **** -->

        <!-- NAVBAR RESPONSE HANDLER -->
        <script src="scripts/navbar-response.js" type="text/javascript" charset="utf-8"></script>

        <!-- EASYTREE -->
        <script src="scripts/easyTree.js" type="text/javascript" charset="utf-8"></script>
        <script src="scripts/easytree-response.js" type="text/javascript" charset="utf-8"></script>

        <!-- LOGIN RESPONSE -->
        <script src="scripts/login-response.js" type="text/javascript" charset="utf-8"></script>

        <!-- COLUMN RESIZER -->
        <script src="scripts/resizer.js" type="text/javascript"></script>

        <!-- INITIATING SCRIPT, ON ALL REFRESH -->
        <script src="scripts/init.js" type="text/javascript"></script>

        <!-- ANSWER SET OUTPUT XSLT PLUGIN -->
        <script type="text/javascript" src="jquery.xslt.js"></script> 
        <!-- <script>
            $("#menu-toggle").click(function(e) {
                e.preventDefault();
                $("#wrapper").toggleClass("toggled");
            });
        </script> -->

"""
navTemplate = """
<div id="wrap">
<div id="navbar">
<header>
<nav class="navbar navbar-default">
<div class="container-fluid">
<div class="collapse navbar-collapse">

"""

navTemplateEnd = """
</div> <!-- /.nav-collapse -->
</div>
</nav>
</header>
</div>
</div>
"""
loginBut = """
<li> <a class="btn btn-launch" href="javascript:;" data-toggle="modal" data-target="#loginModal" data-username="" id="login"> Log-in </a> </li>
"""
configBut = '<a class="btn btn-launch" href="javascript:;" data-toggle="modal" data-target="#configModal" data-username="" id="configButton"> <span class="glyphicon glyphicon-wrench"></a> '

configModal = """
 <div class="modal fade" id="configModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true" >
    <div class="modal-dialog">
    <div class="modal-content login-modal">
        <div class="modal-header login-modal-header">Welcome to my configuration file</div>
        <div class="modal-body">
             <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
"""

configModalEnd = """
</div>
<div class="modal-footer"></div>
</div>
</div>
</div>
"""
saveSettingsBut = '<button type="button" id="saveSettings" class="btn btn-primary" onclick="saveSettings();" >Save settings</button>'