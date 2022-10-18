# Status Report 3

## Work Done

* Looked at [BioBERT](https://huggingface.co/dmis-lab/biobert-v1.1)
* Looked at [PubMedBERT])(https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract)
* Made a [Colab notebook](https://colab.research.google.com/drive/1yRgVRRmwfxSzHuKIhCUOVJ-3tYl9oDL3?usp=sharing) and played with the DrugProt dataset and PubMedBERT.
* Analysed the [Overview of the DrugProt Task](https://biocreative.bioinformatics.udel.edu/media/store/files/2021/Track1_pos_1_BC7_overview.pdf) and read a couple of the cited papers to observe different RE methods with BERT.
* Looked at this [GitHub repo](https://github.com/NLPatVCU/BioCreative-VII-Track1/blob/main/BERT.ipynb) and several others to see example implementations.
* Read [this paper](https://link.springer.com/protocol/10.1007/978-1-0716-2305-3_12) that provides information about BioBERT and RE.

## Findings

* The teams that implemented this modelled it as either a text classification task or an NER task.
* [This blog](https://www.microsoft.com/en-us/research/blog/domain-specific-language-model-pretraining-for-biomedical-natural-language-processing/#:~:text=Not%20surprisingly%2C%20BioBERT%20is%20the,over%20BioBERT%20in%20most%20tasks.) seems to suggest that PubMedBERT is superior to BioBERT.
* The information you provided was very helpful :)

## Questions

* I'm not quite sure how to format the dataset in a 'nice' way i.e. converting all the nested dictionaries into a nice dataframe. Do you have any suggestions?
* What are the differences between BioBERT and PubMedBERT? Is it the number of PubMed articles they've been pretrained with?
* Would I only need PubMedBERT pretrained on abstracts and not the entire text since it is only the title and abstracts I am embedding? Would there be any disadvantages to using the full text?
* I'll probably focus on learning how to use PyTorch this week since I'm still not quite solid on how everything works. Do you know any good resources?



