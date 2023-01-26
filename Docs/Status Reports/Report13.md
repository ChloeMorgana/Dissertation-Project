# Work Done
* Did some more debugging

# Findings
* I figured one of the issues I was having was that the number of sentences considered for both embeddings and labels were different and that could have contributed to different results. The confusing thing was there were more embedding sentences than label sentences despite there being more labels than embeddings

# Questions
* For entity masking is it typical to use the same token to replace both entities e.g. [MASK] or a different one for each e.g. [CHEM] ,[GENE]?
* Do I need to use the validation set for anything?
* If I'm merging my analysis and design sections, are there any other sections that you would recommend apart from intro, background, implementation and evaluation?
