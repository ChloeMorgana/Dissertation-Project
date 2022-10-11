from bioc import biocxml
import spacy

with open("CDR.xml", 'r') as fp:
    collection = biocxml.load(fp)