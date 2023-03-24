# Status Report 4

## Work Done

* Investigated Pytorch
* Evaluated each stage of the tokenisation process for BERT
* Read [this blog](https://medium.com/@dhartidhami/understanding-bert-word-embeddings-7dc4d2ea54ca) on BERT word embeddings.
* Read [this blog](https://www.analyticsvidhya.com/blog/2021/05/all-you-need-to-know-about-bert/#:~:text=The%20BERTBase%20model%20uses,has%20around%20110M%20trainable%20parameters.) on BERT.
* Started to base implementation on [this paper](https://biocreative.bioinformatics.udel.edu/media/store/files/2021/Track1_pos_3_BC7_submission_130.pdf) and [this paper](https://biocreative.bioinformatics.udel.edu/media/store/files/2021/Track1_pos_2_BC7_submission_172.pdf)

## Findings

* Will probably divide the text into fragments and then classify each fragment as opposed to each token
* A linear classifier is a model that makes a decision to categories a set of data points to a discrete class based on a linear combination of its explanatory variables. 
* Highest F1-scores received by adding stuff to encoding part.
* Focus on relations within sentences since <1% of relations cross multiple sentences.
* Using entity marking as opposed to entity masking
* Split the abstracts into sentences using segtok
* Finding a way to ensure that it only contains relevant sentences.
* Tagging Drugs and proteins within text
* Might figure out how to use dropout to prevent overfitting.

## Questions

* I noticed that one implementation used tags before each drug and protein e.g. @DRUG$. How does this work with BERT? Surely you would need to specify the ending of the entity?
* Are relations bidirectional? As in can we have Chemical RELATION Gene and Gene RELATION chemical? I ask because a lot of implementations take head entity as chemical and tail entity as gene.
* For the classification part, I've noticed people using a softmax layer. What is this?
* Why would the classification layer be applied specifically to the CLS token?
