import xml.etree.ElementTree as ET
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


print '<html>'

print '<body>'
for child in root:
        #print child.tag, child.attrib
        #print child.tag

        # We are going to try to e
        if child.tag == 'navbar':
            for navbarChild in child:
                #print navbarChild.tag

                if navbarChild.tag == 'left':
                    print '<ul class="nav navbar-nav navbar-left">'
                    for leftElement in navbarChild:

                        buttonCheck(leftElement, navbarChild.tag)
                    print '</ul>'
                elif navbarChild.tag == 'right':
                    print '<ul class="nav navbar-nav navbar-right">'
                    for rightElement in navbarChild:
                        buttonCheck(rightElement, navbarChild.tag)
                    print '</ul>'

print '</body>'
print '</html>'








