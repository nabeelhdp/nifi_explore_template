
import xml.etree.ElementTree as ET
from __future__ import print_function

tree = ET.parse('rootpg.xml')
root = tree.getroot()
root = tree.getroot()

THRESHOLD=1

for child in root:
  if child.tag=='snippet':
    for elements in child:
      if elements.tag=='processGroups':
        for process_groups in elements:
          pg_name=elements.findall('./name')[0].text
          pg_id=elements.findall('./id')[0].text
          title_flag=1
          for pg_elements in process_groups:
            if pg_elements.tag=='processors':
              concurrentlySchedulableTaskCount="Undefined"
              processor_name=pg_elements.findall('./name')
              task_count=pg_elements.findall('./config/concurrentlySchedulableTaskCount')
              if int(task_count[0].text) > THRESHOLD:
                if title_flag==1:
                  print("\nName: {} [ ID: {} ]".format(pg_name,pg_id))
                  title_flag=0
                print("    {} : {}".format(processor_name[0].text,task_count[0].text))
                  
