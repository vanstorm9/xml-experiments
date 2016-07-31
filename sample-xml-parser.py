import xml.etree.ElementTree as ET
from headString import headStr
from hardcodeStrings import *


#tree = ET.parse('country_data.xml')
tree = ET.parse('sparc_sample.xml')
root = tree.getroot()

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
                                print ''
                        elif butProp.tag == 'behavior':
                                for behaveChildren in butProp:
                                        #print behaveChildren.tag

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
                        print '<div class="navbar-form navbar-left" id="qform">'
                        i = 0
                        for inputTxt in textFieldList:
                                print '<input type="text" class="form-control" placeholder="'+inputTxt+'" name="txt_query" id="'+textFieldIDList[i]+'">'
                                i += 1
                        print buttonHTML
                        print '</div>'

                        print '<script>'
                        print "$('#"+butID+"').click(function(e) {"
                        print 'e.preventDefault();'
                        print 'var editorValue = editor.getValue();'
                        i = 0
                        paramStr = ""
                        for textFieldID in textFieldIDList:
                                print "var queryValue"+str(i)+" = $('#"+textFieldID+"').val();"
                                paramStr = paramStr + ",'p"+str(i)+"': queryValue"+str(i) 
                                i += 1
                        paramStr = paramStr + '}'
                        print "var data = {'action': \""+inputID+"\",'editor': editorValue " + paramStr
                        print "alert(editorValue);"
                        print '$.post(ajaxurl, data, function(response) {setResultsToString(response);});'
                        print '});'
                        print '</script>'
                        
                else:
                        buttonHTML = '<button '+ butClass +'id="'+ butID +'">'+ butTxt +'</button>'
                        print ' <li>'
                        print buttonHTML
                        print ' </li>'

                        print '<script>'
                        print "$('#"+butID+"').click(function(e) {"
                        print "alert('"+butID+"');"
                        print '});'
                        print '</script>'



def configCheck(xmlElement):
        if xmlElement.tag == 'config':
                print configBut
                
                print configModal
                
                for child in xmlElement:
                        if child.tag == 'option':
                                configOptionID = child.get('name')

                                for options in child:
                                        if options.tag == 'optionvalues':
                                                print configOptionID
                                                print '<select id="'+configOptionID+'" style="color:black"> '
                                                for li in options:
                                                        if li.tag == 'li':
                                                                optionSolver = li.text
                                                                optionStr = '<option value="'+optionSolver+'">' + optionSolver + '</option>'
                                                                print optionStr
                                                print '</select></br></br>'
                                        elif options.tag == 'optionInput':
                                                print configOptionID
                                                chosenInt = options.text
                                                print '<select id="'+configOptionID+'" style="color:black"> '
                                                
                                                for i in range(1,int(chosenInt)+1):
                                                        print '<option value="'+str(i)+'">' + str(i) + '</option>'
                                                print '</select></br></br>'
                                
                print saveSettingsBut
                print configModalEnd


print '<!DOCTYPE html>'
print'<html lang="en">'
print headStr
print '<body>'
for child in root:
        #print child.tag, child.attrib
        #print child.tag

        # We are going to try to e
        if child.tag == 'config':
                configCheck(child)
        
        if child.tag == 'navbar':
            for navbarChild in child:
                #print navbarChild.tag
                print navTemplate
                if navbarChild.tag == 'left':
                    
                    print '<ul class="nav navbar-nav navbar-left">'
                    for leftElement in navbarChild:

                        buttonCheck(leftElement, navbarChild.tag)
                    print '</ul>'
                elif navbarChild.tag == 'right':
                    print '<ul class="nav navbar-nav navbar-right">'
                    for rightElement in navbarChild:
                        buttonCheck(rightElement, navbarChild.tag)
                    print loginBut
                    print '</ul>'
            print navTemplateEnd
print editorStr, bottomJS

'''
print '<scipt>'


print 'function butManage(butValue){'
#print "if(butVal =='", 
print '}'


print '</script>'
'''

print '</body>'
print '</html>'








