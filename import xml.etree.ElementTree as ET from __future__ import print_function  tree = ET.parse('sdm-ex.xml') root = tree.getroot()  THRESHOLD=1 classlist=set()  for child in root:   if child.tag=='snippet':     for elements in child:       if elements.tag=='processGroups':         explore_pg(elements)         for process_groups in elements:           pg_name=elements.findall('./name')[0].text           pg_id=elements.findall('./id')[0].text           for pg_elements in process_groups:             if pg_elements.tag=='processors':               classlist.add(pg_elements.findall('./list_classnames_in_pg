
import xml.etree.ElementTree as ET
from __future__ import print_function

tree = ET.parse('sdm-ex.xml')
root = tree.getroot()

THRESHOLD=1
classlist=set()

for child in root:
  if child.tag=='snippet':
    for elements in child:
      if elements.tag=='processGroups':
        for process_groups in elements:
          pg_name=elements.findall('./name')[0].text
          pg_id=elements.findall('./id')[0].text
          for pg_elements in process_groups:
            if pg_elements.tag=='processors':
              classlist.add(pg_elements.findall('./type')[0].text)
          print("\nName: {} [ ID: {} ]".format(pg_name,pg_id))
          print("  Classes used : \n        {}".format("\n        ".join(classlist)))
