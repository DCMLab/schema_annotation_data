from lxml import etree
import argparse

testfile = '/home/chfin/Uni/phd/data/schema_annotation_data/mozart_sonatas/musicxml/K279-1.xml'

def load_with_ids(filename, keep=False):
    xml = etree.parse(filename)
    for i,note in enumerate(xml.findall('.//note')):
        # we need to use the {namespace} syntax instead of 'xml:' with lxml
        if not (keep and ('{http://www.w3.org/XML/1998/namespace}id' in note.keys())):
            note.attrib['{http://www.w3.org/XML/1998/namespace}id'] = 'note'+str(i)
    return xml

def save(filename, xml):
    with open(filename, 'wb') as out:
        xml.write(out)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    xml = load_with_ids(args.input)
    save(args.output, xml)

if __name__ == "__main__":
    main()
