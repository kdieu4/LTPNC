from xml.dom.minidom import parse

dom = parse("students.xml")

for node in dom.getElementsByTagName("student"):
    print(node.getAttribute("id"))
    print(node.getElementsByTagName("name")[0].firstChild.nodeValue)
    print(node.getElementsByTagName("age")[0].firstChild.nodeValue)
    print(node.getElementsByTagName("class")[0].firstChild.nodeValue)