import xml.etree.ElementTree as ET
from headString import headStr
from hardcodeStrings import *


#tree = ET.parse('country_data.xml')
tree = ET.parse('sparc_sample.xml')
root = tree.getroot()

text_file = open("../../github/asp/test.html", "w")

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
                        paramStr = paramStr + '};'
                        text_file.write("var data = {'action': \""+inputID+"\",'editor': editorValue " + paramStr)
                        text_file.write("alert(editorValue);")
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
                        text_file.write("alert('"+butID+"');")
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







