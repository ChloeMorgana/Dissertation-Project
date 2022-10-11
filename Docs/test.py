from bioc import biocxml

with open("CDR", 'r') as fp:
    collection = biocxml.load(fp)