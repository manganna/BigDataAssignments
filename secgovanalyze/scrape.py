import requests
import xml.etree.ElementTree as ET

r = requests.get('url')
tree = ET.parse(r.text)
root = tree.getroot()
with open('data.xml', 'w') as f:
    f.write(r.text)
