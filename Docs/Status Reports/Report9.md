## Work Done
* Had a peruse of the dissertation template and attempted to fill in as much as I can
* Found a solution to finding the labels of the entity tags
* Got the pipeline working for the entity tagging architecture
* Ran the code across the entire corpus for the first time
* Fixed a problem with one sentence exceeding 512 tokens


## Findings
* I'm waiting for the university computers to work again because I started working on my progress report on there and didn't back it up, and I refuse to restart until I know for sure I have to.
* I ran it across the whole corpus and after an hour it moaned that one of the entries had embeddings that exceeded 512 tokens (had 606).
* Decided to experiment on the values when this sentence is removed compared to when it is split in half.
* Inconsistent number of entity-tag embeddings and labels found (64751 embeddings, 69627 labels). This is likely recording labels for documents that do not contain any relations.

## Questions
