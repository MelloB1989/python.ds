from lxml import objectify

data_parsed = objectify.parse(open('data.xml'))
root = data_parsed.getroot()
print(root.getchildren())

for i in root.getchildren():
    #print(i.getchildren())
    for j in i.getchildren():
        print(j.tag, j.text)