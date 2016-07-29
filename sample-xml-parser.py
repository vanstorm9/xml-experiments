import xml.etree.ElementTree as ET
#tree = ET.parse('country_data.xml')
tree = ET.parse('sparc_sample.xml')
root = tree.getroot()

for child in root:
        #print child.tag, child.attrib
        print child.tag

        # We are going to try to e
        if child.tag == 'navbar':
            for navbarChild in child:
                print navbarChild.tag

                if navbarChild.tag == 'left':
                    for leftElement in navbarChild:
                        print leftElement.tag

                    
                elif navbarChild.tag == 'right':
                    for rightElement in navbarChild:
                        print rightElement.tag
                    
        
 
