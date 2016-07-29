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
                
                for butProp in xmlElement:
                        if butProp.tag == 'id':
                                butID = butProp.text
                        elif butProp.tag == 'text':
                                butTxt = butProp.text
                        elif butProp.tag == 'behavior':
                                for behaveChildren in butProp:
                                        z = 1 + 1
                                        #print behaveChildren.tag
                
                buttonHTML = '<button '+ butClass +'id="'+ butID +'">'+ butTxt +'</button>'
                print ' <li>'
                print '    ', buttonHTML
                print ' </li>'


def configCheck(xmlElement):
        if xmlElement.tag == 'config':
                print configBut
                
                print configModal
                
                for child in xmlElement:
                        if child.tag == 'option':
                                configOptionID = child.get('name')

                                for options in child:
                                        if options.tag == 'optionvalues':
                                                print '<select id="'+configOptionID+'" style="color:black"> '
                                                for li in options:
                                                        if li.tag == 'li':
                                                                optionSolver = li.text
                                                                optionStr = '<option value="'+optionSolver+'">' + optionSolver + '</option>'
                                                                print optionStr
                                                print '</select></br></br>'
                                        elif options.tag == 'optionInput':
                                                chosenInt = options.text
                                                print '<select id="'+configOptionID+'" style="color:black"> '
                                                
                                                for i in range(1,int(chosenInt)+1):
                                                        print '<option value="'+str(i)+'">' + str(i) + '</option>'
                                                print '</select></br></br>'     
                
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
print '</body>'
print '</html>'








