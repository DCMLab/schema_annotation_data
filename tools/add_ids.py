from bs4 import BeautifulSoup #, NavigableString
import argparse

testfile = '/home/chfin/Uni/phd/data/schema_annotation_data/mozart_sonatas/musicxml/K279-1.xml'

def load_with_ids(filename, keep=False):
    with open(filename, 'r') as f:
        xml = BeautifulSoup(f.read(), 'xml')
    for i,note in enumerate(xml('note')):
        if not (keep and note.has_attr['xml:id']):
            note['xml:id'] = "note"+str(i)
    return xml

def save(filename, xml):
    with open(filename, 'w') as f:
        f.write(xml.prettify())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    xml = load_with_ids(args.input)
    save(args.output, xml)

if __name__ == "__main__":
    main()
