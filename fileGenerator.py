import xml.etree.ElementTree as ET
from headString import headStr
from hardcodeStrings import *


#tree = ET.parse('country_data.xml')
tree = ET.parse('sparc_sample.xml')
root = tree.getroot()

text_file = open("../../test.php", "w")

ajaxList = []
ajaxParam = []

def buttonCheck(xmlElement, direction):
        # Going to generate HTML buttons
        # <button type="submit" class="btn btn-default navbar-btn" id="btn_getDrawing" value="getDrawing">  Draw</button>
        if xmlElement.tag == 'button':
                
                butID = ''
                butTxt = ''
                butClass = 'class="btn btn-default navbar-btn"'
                inputID = ''
                onclick = ''
                editorSelect = ''
                programSelect = ''

                inputField = ''
                inputFieldID = ''
                
                form = False

                textFieldList = []
                textFieldIDList = []

                for butProp in xmlElement:
                        # Iterate through the tags in the button
                        if butProp.tag == 'id':
                                butID = butProp.text
                                ajaxList.append(butID)
                        elif butProp.tag == 'text':
                                butTxt = butProp.text
                        elif butProp.tag == 'inputField':
                                inputTxt = butProp.text
                                form = True
                                textFieldList.append(inputTxt)
                                text_file.write('')
                        elif butProp.tag == 'behavior':
                                for behaveChildren in butProp:
                                        if behaveChildren.tag == 'program':
                                                programSelect = behaveChildren.text
                                        elif behaveChildren.tag == 'editor':
                                                editorSelect = behaveChildren.text
                                        elif behaveChildren.tag == 'inputFieldId':
                                                inputFieldID = behaveChildren.text
                                                textFieldIDList.append(inputFieldID)


                if form:
                        butClass = 'class="btn btn-default"'
                        buttonHTML = '<button type="button" '+ butClass +' id="'+ butID +'">'+ butTxt +'</button>'
                        text_file.write('<div class="navbar-form navbar-left" id="qform">')
                        i = 0
                        for inputTxt in textFieldList:
                                text_file.write('<input type="text" class="form-control" placeholder="'+inputTxt+'" name="txt_query" id="'+textFieldIDList[i]+'">')
                                i += 1
                        text_file.write(buttonHTML)
                        text_file.write('</div>')

                        text_file.write('<script>')
                        text_file.write("$('#"+butID+"').click(function(e) {")
                        text_file.write('e.preventDefault();')
                        text_file.write('var editorValue = editor.getValue();')
                        i = 0
                        paramStr = ""
                        for textFieldID in textFieldIDList:
                                text_file.write("var queryValue"+str(i)+" = $('#"+textFieldID+"').val();")
                                paramStr = paramStr + ",'p"+str(i)+"': queryValue"+str(i) 
                                i += 1
                        ajaxParam.append([butID,i])
			paramStr = paramStr + '};'
                        text_file.write("var data = {'action': \""+butID+"\",'editor': editorValue, 'numPar':"+str(i)+" " + paramStr)
                        text_file.write('$.post(ajaxurl, data, function(response) {setResultsToString(response);});')
                        text_file.write('});')
                        text_file.write('</script>')
                        
                else:
                        buttonHTML = '<button '+ butClass +'id="'+ butID +'">'+ butTxt +'</button>'
                        text_file.write('<li>')
                        text_file.write(buttonHTML)
                        text_file.write('</li>')

                        text_file.write('<script>')
                        text_file.write("$('#"+butID+"').click(function(e) {")
                        text_file.write('e.preventDefault();')
                        text_file.write('var editorValue = editor.getValue();')
                        i = 0
                        text_file.write("var data = {'action': \""+butID+"\",'editor': editorValue};")
                        text_file.write('$.post(ajaxurl, data, function(response) {setResultsToString(response);});')
                        text_file.write('$.post(compilerurl, data, function(response) {setResultsToString(response);});')
                        text_file.write('});')
                        text_file.write('</script>')


def configCheck(xmlElement):
        if xmlElement.tag == 'config':
                text_file.write(configBut)
                
                text_file.write(configModal)
                
                for child in xmlElement:
                        if child.tag == 'option':
                                configOptionID = child.get('name')

                                for options in child:
                                        if options.tag == 'optionvalues':
                                                text_file.write(configOptionID)
                                                text_file.write('<select id="'+configOptionID+'" style="color:black"> ')
                                                for li in options:
                                                        if li.tag == 'li':
                                                                optionSolver = li.text
                                                                optionStr = '<option value="'+optionSolver+'">' + optionSolver + '</option>'
                                                                text_file.write(optionStr)
                                                text_file.write('</select></br></br>')
                                        elif options.tag == 'optionInput':
                                                text_file.write(configOptionID)
                                                chosenInt = options.text
                                                text_file.write('<select id="'+configOptionID+'" style="color:black"> ')
                                                
                                                for i in range(1,int(chosenInt)+1):
                                                        text_file.write('<option value="'+str(i)+'">' + str(i) + '</option>')
                                                text_file.write('</select></br></br>')
                                
                text_file.write(saveSettingsBut)
                text_file.write(configModalEnd)


text_file.write('<!DOCTYPE html>')
text_file.write('<html lang="en">')
text_file.write(headStr)
text_file.write('<body>')
text_file.write("<script>var ajaxurl = 'ajax.php'; var compilerurl = './compiler/compiler.php'</script>")
for child in root:
        # We are going to try to e
        if child.tag == 'config':
                configCheck(child)
        
        if child.tag == 'navbar':
            for navbarChild in child:
                text_file.write(navTemplate)
                if navbarChild.tag == 'left':
                    
                    text_file.write('<ul class="nav navbar-nav navbar-left">')
                    for leftElement in navbarChild:

                        buttonCheck(leftElement, navbarChild.tag)
                    text_file.write('</ul>')
                elif navbarChild.tag == 'right':
                    text_file.write('<ul class="nav navbar-nav navbar-right">')
                    for rightElement in navbarChild:
                        buttonCheck(rightElement, navbarChild.tag)
                    text_file.write(loginBut)
                    text_file.write('</ul>')
            text_file.write(navTemplateEnd)

            
        text_file.write(beginLoginModal)

text_file.write(editorStr)
text_file.write(bottomJS)
text_file.write('</body>')
text_file.write('</html>')

text_file.close()

# Now going to generate mock copy of ajax.php
fileAjax = open("../../ajax.php", "w")

fileAjax.write(ajaxPHPbegin)
fileAjax.write(ajaxCaseBegin)


#fileAjax.write('$numPar = helper_getPost("numPar");')

# The place where we write our switch statement functions


for but in ajaxList:
        
	fileAjax.write("case '"+but+"':")
	fileAjax.write("echo cp_"+but+"();")
	fileAjax.write("break;")
     
fileAjax.write(ajaxCaseEnd)
fileAjax.write(ajaxPHPSemiEndingBegin)
# Insert our function here
# Based on amount of buttons
for but in ajaxList:
        
	fileAjax.write('function cp_'+but+'(){')
	fileAjax.write("$output = executeBashCmd_"+but+"();")
	fileAjax.write("return $output;")
	fileAjax.write('}')

fileAjax.write(ajaxPHPEndingTag)

fileAjax.close()


fileCompile = open("../../compiler/compiler.php", "w")

fileCompile.write(compileBegin)


#fileCompile.write('function executeBashCmd(){ return "Hello World";}')

for but in ajaxList:
	fileCompile.write('function executeBashCmd_'+but+'(){')
	for name,i in ajaxParam:
		# If the name in ajaxParam matches the name of clicked button
		# Variable i is the number of arguments
		if name == but:
			numOfParam = int(i)
			for x in range(0,i):
				# Get string that is in parameter p0, p1, etc
				tempStr =  'echo "p'+str(x)+': ".helper_getPost("p'+str(x)+'")."</br>";'

	fileCompile.write('return "Hello World";}')

###### Stuff to do for compiler.php #####

'''
for but in ajaxList:
        
	fileAjax.write("case '"+but+"':")
        fileAjax.write("echo '<h1>Executing "+but+".exe</h1>';")
        fileAjax.write("echo '<h2>Parameters: </h2>';")
	for name,i in ajaxParam:
		# If the name in ajaxParam matches the name of clicked button
		# Variable i is the number of arguments
		if name == but:
			numOfParam = int(i)
			for x in range(0,i):
				# Get string that is in parameter p0, p1, etc
				tempStr =  'echo "p'+str(x)+': ".helper_getPost("p'+str(x)+'")."</br>";'
				fileAjax.write(tempStr)
			fileAjax.write("echo '<h2>Code:</h2> ' . $code . '</br>';")
	fileAjax.write("break;")
'''     


fileCompile.write(compileEnd)


fileCompile.close()


print 'Done'
