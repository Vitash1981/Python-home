import xml.etree.ElementTree as ET
import re


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = ET.iterparse(filename, ('start', 'end'))
    # Skip root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
#code for task 1 Country name and goverment with out duplicates

lines_seen = set()
country_government = []
countries = parse_and_remove('mondial-3.0.xml', 'country')
for country in countries:
    government = country.attrib['government'].split(' ')[0]
    name = country.attrib['name']
    new_country = re.compile(r"[A-Z]")
    new_name = new_country.findall(name)

    for n in new_name:
        if country not in lines_seen:
            lines_seen.add(country)
            print(name, ':', government, end=',')


#code for task 2 Country name consit of mnimum two part and goverment with out duplicates
'''
lines_seen = set()
country_government = []
countries = parse_and_remove('mondial-3.0.xml', 'country')
for country in countries:
    government = country.attrib['government'].split(' ')[0]
    name = country.attrib['name']
    new_country = re.compile(r"[A-Z]*\s[A-Za-z]*")
    new_name = new_country.findall(name)

    for n in new_name:
        if country not in lines_seen:
            lines_seen.add(country)
            print(name, ':', government, end=',')
'''
