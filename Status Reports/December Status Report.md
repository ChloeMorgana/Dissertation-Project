
## Extracting Relations Between Chemicals and Genes in Biomedical Text 
#### Chloe Smart 
#### 2439047s 

## Proposal
### Motivation
* Manually processing an abundance of biomedical data can prove to be extremely costly and inefficient, and often causes bottlenecks within the processes of drug discovery, design and repurposing. This project attempts to mitigate these problems by evaluating relation extraction methods using natural language processing and deep learning. Those methods predict whether two chemical-gene entities are associated and what their association is.

### Aims
* This project aims to investigate different refinements that can be made to HuggingFace transformers in order to produce more accurate results in the context of relation extraction. This includes changing the kinds of embeddings used in the classification part of the pipeline, the models used, and applying several external libraries. It also aims to explore the reasons for different error values, and attempts to devise strategies to mitigate these errors. 


## Progress
* Background research on different relation extraction methods.
* Investigated different datasets.
* Decided on using Python and HuggingFace transformers.
* Decided on using the DrugProt dataset and researched previous implementations.
* Implemented relation extraction pipelines for CLS embeddings and for entity start embeddings.
* Performed binary classification on these embeddings.


## Problems and risks
### Problems
* Research was very time-consuming, and therefore progress was slower than anticipated.
* There was a learning curve with finding out how each aspect of the transformer and pytorch worked.
* HuggingFace consistently update their packages, so sometimes certain models produced unexpected results since it would be working with obsolete libraries.


### Risks
* Underestimation of time taken to complete tasks. Solution is to start early and adjust accordingly.
* Having too many ideas on what to add to the implementation. Solution is to prioritise important ones and make a list of extra ones that can be added if there is time.
* Coming across an error that takes too long to fix. Solution is to use all resources at my disposal and change my approach if required.


## Plan
January: 
* Finalise the implementation
* Start doing literature reviews on all of the research texts I have cited
* Start writing introduction and background sections of dissertation

February:
* Write the requirements, design and implementation sections of the dissertation

March:
* Write the evaluation and conclusion sections of the dissertation
* Refine the dissertation

