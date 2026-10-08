import os
import xml.sax
os.system('clear')

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.data = {}
        
    def startElement(self, name, attrs):
        self.current_element = name
        if name == "student":
            self.data['id'] = attrs.getValue('id')
    
    def endElement(self, name):
        if name == "student":
            print (f"Student: {self.data}")
            self.data = {}
            
    def characters(self, content):
        string_content = content.strip()
        current_element = self.current_element
        if current_element and string_content:
            self.data[current_element] = string_content

def main():
    parser = xml.sax.make_parser()
    handler = MyHandler()
    parser.setContentHandler(handler)
    parser.parse("students.xml")
    
if __name__ == "__main__":
    main()