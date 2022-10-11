# Status Report 2

## Work Done

* Read [Different ways of doing Relation Extraction from text](https://medium.com/@andreasherman/different-ways-of-doing-relation-extraction-from-text-7362b4c3169e)
* Read [Overview of the CDR Task](https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDRoverview.pdf)
* Read [Overview of the DrugProt Task](https://biocreative.bioinformatics.udel.edu/media/store/files/2021/Track1_pos_1_BC7_overview.pdf)
* Read [Annotating chemicals, diseases and interactions in biomedical literature](https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDRcorpus.pdf)
* Looked at [BioC Library](https://bioc.sourceforge.net/)
* Read [Unsupervised Text Mining Method for Relation Extraction](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0102039#s1)
* Read [Biomedical Relation Extraction](https://www.hindawi.com/journals/cmmm/2014/298473/)
* Read about [DNorm and pLTR](https://academic.oup.com/bioinformatics/article/29/22/2909/312804)
* Read about [KGen](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-020-01341-5)
* Read about [A neural joint model for entity and relation extraction from biomedical text](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1609-9)
* Played around with the CDR corpus

## Findings

* Discovered several corpora, including AImed, BioInfer, HPRD50, IEPA, and LLL
* I did more research on CDR compared to DrugProt
* NLP faces problems such as negative sentences, with potential solutions lying in pattern-based approaches.
* Low performance of existing systems can be attributed to lack of annotated data, which could be resolved by using semi supervised approaches.
* Pipeline models tend to suffer from error propagation and not able to utilise interactions between subtasks, with potential solutions in neural joint models.

## Potential Technologies for Pipeline

* CDR corpus: Dataset
* BioC: Text interchange format
* Spacy: Preprocessing, NER
* DNorm: Normalise disease names
* Pytorch

## Questions

* What other technologies would you recommend?
* Are there other research papers that I might find useful?