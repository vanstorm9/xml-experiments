import xml.etree.ElementTree as ET
from headString import headStr
from hardcodeStrings import *


#tree = ET.parse('country_data.xml')
tree = ET.parse('sparc_sample.xml')
root = tree.getroot()

text_file = open("../../test.php", "w")

ajaxList = []
ajaxParam = []
settingsOpt = []
selectOptionList = [] 
selectOptionParam = []

selectNumList = []
selectNumParam = []

solverList = []
solverStr = ''


def buttonRunCheck(xmlElement):
        global solverStr
	butClass = 'class="btn btn-default navbar-btn"'
	
	if xmlElement.tag == 'buttonRun':
		# For each button
		runID = ''
		runText = ''
	
		for subTags in xmlElement:
			# For each subtag
			if subTags.tag == 'text':
				runText = subTags.text
			elif subTags.tag == 'id':
				runID = subTags.text
                

		buttonHTML = '<button '+ butClass +'id="'+ runID +'">'+ runText +'</button>'
		

                text_file.write('<li>')
		text_file.write(buttonHTML)
                text_file.write('</li>')


		text_file.write('<script>')
		text_file.write("$('#"+runID+"').click(function(e) {")
		text_file.write('e.preventDefault();')
		text_file.write('var editorValue = editor.getValue();')
		
		paramOptionStr = ""
		j = 0	
		for optionID in selectOptionList:
			text_file.write("var selectOptionValue"+str(j)+" = $('#"+optionID+"').val();")
			paramOptionStr = paramOptionStr + ",'o"+str(j)+"': selectOptionValue"+str(j) 
			j += 1
		selectOptionParam.append([optionID, j])			

		k = 0
		paramNumStr = ""
		for optionNumID in selectNumList:
			text_file.write("var selectNumberValue"+str(k)+" = $('#"+optionNumID+"').val();")
			paramNumStr = paramNumStr + ",'n"+str(k)+"': selectNumberValue"+str(k) 
			k += 1

		selectNumParam.append([paramNumStr, k])			
		text_file.write('var solve_e = document.getElementById("'+solverStr+'");')
		text_file.write('var solverStr = solve_e.options[solve_e.selectedIndex].value;')
		text_file.write("var data = {'action': \"ourGetAnswerSets\", 'id': \""+runID+"\", 'solver': solverStr ,'editor': editorValue};")
		text_file.write('$.post(ajaxurl, data, function(response) {setResultsToString(response);});')
		text_file.write('$.post(compilerurl, data, function(response) {setResultsToString(response);});')
		text_file.write('alert(solverStr);')
		text_file.write('});')
		text_file.write('</script>')



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
                        for textFieldID in textFieldIDList:
                                text_file.write("var queryValue"+str(i)+" = $('#"+textFieldID+"').val();")
                                paramStr = paramStr + ",'p"+str(i)+"': queryValue"+str(i) 
                                i += 1
                        ajaxParam.append([butID,i])

			j = 0
                        paramOptionStr = ""
                        for optionID in selectOptionList:
                                text_file.write("var selectOptionValue"+str(j)+" = $('#"+optionID+"').val();")
                                paramOptionStr = paramOptionStr + ",'o"+str(j)+"': selectOptionValue"+str(j) 
                                j += 1
			selectOptionParam.append([optionID, j])			

			k = 0
                        paramNumStr = ""
                        for optionNumID in selectNumList:
                                text_file.write("var selectNumberValue"+str(k)+" = $('#"+optionNumID+"').val();")
                                paramNumStr = paramNumStr + ",'n"+str(k)+"': selectNumberValue"+str(k) 
                                k += 1

			selectNumParam.append([paramNumStr, k])			

                        text_file.write("var data = {'action': \""+butID+"\",'editor': editorValue, 'program': '"+programSelect+"', 'numPar':"+str(i)+" " + paramStr + ", 'selectOption':"+str(i)+" " + paramOptionStr)
			text_file.write('};')
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
                        
			paramOptionStr = ""
			j = 0	
                        for optionID in selectOptionList:
                                text_file.write("var selectOptionValue"+str(j)+" = $('#"+optionID+"').val();")
                                paramOptionStr = paramOptionStr + ",'o"+str(j)+"': selectOptionValue"+str(j) 
                                j += 1
			selectOptionParam.append([optionID, j])			

			k = 0
			paramNumStr = ""
                        for optionNumID in selectNumList:
                                text_file.write("var selectNumberValue"+str(k)+" = $('#"+optionNumID+"').val();")
                                paramNumStr = paramNumStr + ",'n"+str(k)+"': selectNumberValue"+str(k) 
                                k += 1

			selectNumParam.append([paramNumStr, k])			

                        text_file.write("var data = {'action': \""+butID+"\",'editor': editorValue, 'program': '"+programSelect+"'};")
                        text_file.write('$.post(ajaxurl, data, function(response) {setResultsToString(response);});')
                        text_file.write('$.post(compilerurl, data, function(response) {setResultsToString(response);});')
                        text_file.write('});')
                        text_file.write('</script>')


def configCheck(xmlElement):
	global solverStr
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
						selectOptionList.append(configOptionID)

                                        elif options.tag == 'optionInput':
                                                text_file.write(configOptionID)
                                                chosenInt = options.text
                                                text_file.write('<select id="'+configOptionID+'" style="color:black"> ')
                                                
                                                for i in range(1,int(chosenInt)+1):
                                                        text_file.write('<option value="'+str(i)+'">' + str(i) + '</option>')
                                                text_file.write('</select></br></br>')
						
						selectNumList.append(configOptionID)
					elif options.tag == 'commandSwitch':
						if options.text == '-solver':
							solverStr = configOptionID


                text_file.write(saveSettingsBut)
		# Here we will write the script that will generate the setting functions
		#for options in settingsOpt:	
                text_file.write(configModalEnd)
		

def filesystemCheck(xmlElement):
	if xmlElement.tag == 'filesystem':
		text_file.write(filesystemNavbar)
		text_file.write(dialog)



text_file.write('<!DOCTYPE html>')
text_file.write('<html lang="en">')
text_file.write(headStr)
text_file.write('<body>')
text_file.write("<script>var ajaxurl = 'ajax.php'; var compilerurl = './compiler/compiler.php'</script>")
for child in root:
        # We are going to try to e
        if child.tag == 'filesystem':
        	filesystemCheck(child)
	if child.tag == 'config':
                configCheck(child)
        
        if child.tag == 'navbar':
            for navbarChild in child:
                text_file.write(navTemplate)
                if navbarChild.tag == 'left':
                    
                    text_file.write('<ul class="nav navbar-nav navbar-left">')
                    for leftElement in navbarChild:

                        buttonCheck(leftElement, navbarChild.tag)
			buttonRunCheck(leftElement)
                    text_file.write('</ul>')
                elif navbarChild.tag == 'right':
                    text_file.write('<ul class="nav navbar-nav navbar-right">')
                    for rightElement in navbarChild:
                        buttonCheck(rightElement, navbarChild.tag)
			buttonRunCheck(rightElement)
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



fileAjax.write("case 'ourGetAnswerSets':")
fileAjax.write("echo cp_ourGetAnswerSets($code, helper_getPost('solver'));")
fileAjax.write("break;")

for but in ajaxList:
        
	fileAjax.write("case '"+but+"':")
	fileAjax.write("echo cp_"+but+"();")
	fileAjax.write("break;")

fileAjax.write(ajaxCaseEnd)
fileAjax.write(ajaxPHPSemiEndingBegin)

# Insert our function here
# Based on amount of buttons

fileAjax.write('function cp_ourGetAnswerSets($code, $solver){')
fileAjax.write('echo $solver;')
fileAjax.write('if(strcmp(strtolower($solver), "sparc") == 0){')
fileAjax.write('$rawAnswerSets = cp_getAnswerSets($code);')
fileAjax.write('$xmlAnswerSets = ps_parseSparc($rawAnswerSets);')
fileAjax.write('return $xmlAnswerSets;')
fileAjax.write('} else if(strcmp(strtolower($solver),"dlv")==0){')
fileAjax.write('$xmlAnswerSets = "Running DLV code";')
fileAjax.write('return $xmlAnswerSets;')
fileAjax.write("} else {return 'No code avaliable';}")
fileAjax.write('}')

for but in ajaxList:
        
	fileAjax.write('function cp_'+but+'(){')
	fileAjax.write("$output = executeBashCmd_"+but+"();")
	fileAjax.write("return $output;")
	fileAjax.write('}')

fileAjax.write(ajaxPHPEndingTag)

fileAjax.close()




###### Stuff to do for compiler.php #####


fileCompile = open("../../compiler/compiler.php", "w")

fileCompile.write(compileBegin)



for but in ajaxList:
	fileCompile.write('function executeBashCmd_'+but+'(){')
	fileCompile.write('$command = "./exe/".helper_getPost("program");')
	fileCompile.write('$output = "";')
	for name,i in ajaxParam:
		# If the name in ajaxParam matches the name of clicked button
		# Variable i is the number of arguments
		if name == but:
			numOfParam = int(i)
			for x in range(0,i):
				# Get string that is in parameter p0, p1, etc
				#tempStr =  'echo " ".helper_getPost("p'+str(x)+'")."</br>";'
				fileCompile.write('$command .= " ".helper_getPost("p'+str(x)+'");')
				#fileCompile.write(tempStr)
	fileCompile.write('echo "Executing bash command: ".$command."<br><br>";');
	#fileCompile.write('return "Hello World";}')
	fileCompile.write('$output = shell_exec($command);')
	fileCompile.write('echo "Output:<br>";')
	fileCompile.write('return $output;}')

fileCompile.write(compileEnd)


fileCompile.close()


print 'Done'
