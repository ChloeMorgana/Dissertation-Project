# Work Done
* Did some more debugging
* Refactored my code so now it's a lot better and (hopefully) functions as anticipated.

# Findings
* (Multiclass CLS): Precision: 0.74, recall: 0.35, f1-score: 0.39
* (Multiclass entity tags): Precision: 0.81 , recall: 0.56 , f1-score: 0.61
* Seems to be a significant improvement using entity embeddings compared to cls embeddings
* Still a class imbalance issue though

# Questions
* For entity masking is it typical to use the same token to replace both entities e.g. [MASK] or a different one for each e.g. [CHEM] ,[GENE]?
* Do I need to use the validation set for anything?
* If I'm merging my analysis and design sections, are there any other sections that you would recommend apart from intro, background, implementation and evaluation?
* Technically I'm not using a softmax layer or a linear classification layer but should I still write about it in my dissertation? I feel like I'd just be going "Yeah this is a cool idea but let's not do that"
* How gross are my results allowed to be?
