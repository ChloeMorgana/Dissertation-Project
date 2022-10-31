# Status Report 5

## Work Done

* Started implementing the pre-processing step
* Started researching which type of layer to use for classification
* Found that using a [CV estimator](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator) may be better for this implementation.
* Looked at [this paper](https://arxiv.org/pdf/1906.03158.pdf) that explores different ways of getting contextual vectors from the text
* Ran the code using Fidra

## Findings

* I experimented with very small amounts of data to start with to ensure my implementation functions as expected
* A naive plan is to embed the sentence, take the CLS embedding and add it to a list, then use the binary classifier layer on these CLS embeddings
* Will experiment with the effect of using a sliding window to reduce the input
* Will see the effect of removing sentences that do not contain a relation
* Might start off with LogisticRegressionCV and see what happens

## Questions

* How long roughly do you think it would take to convert all of the corpus into embeddings?
* I'm a bit confused about the output of the binary classifier. Is it positive when it matches one of the pre-specified labels and then negative if it's a different relation?
* Is entity start similar to just using the CLS token, but instead with entity start tokens?
* Is mention pooling just taking the embeddings for the actual entity names? Would these be averaged together?
* Other than tables of F1-scores, confusion matrices etc, is there any other output you're looking for/would recommend?