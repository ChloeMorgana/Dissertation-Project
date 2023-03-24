## Code Description

* loadDrugProt: Combines the entities, abstracts and relations together from the drugprot dataset
* Removal of document exceeding 512 tokens
* isRelation: Takes in two relations returns their relation type if they are related
* find_sent_idxs: Finds the start and end indexes of each sentence in the document text
* find_entity_labels: Finds the entities within the bounds of each sentence and finds the cartesian product of all chemicals and genes. The relevant representation structure is then added to the text.
* addEntityTags: Finds the sentences, labels and order of chemicals and genes from each sentence
* bert_text_prep: Prepares the text for input into BERT e.g. tokenisation, [CLS]/[SEP] tags etc.
* get_bert_embeddings: Returns the embeddings for each token.
* findEmbedding: Finds the entity representations from the text and concatenates them (Entity markers)
* findMasks: Finds the entity representations from the text and concatenates them (Entity masks)
* get_embeddings: Finds both the [CLS] and entity representations for each sentence and returns them in two lists

## Instructions

* This code is in an ipynb format and can be run using software supporting this file type. Any functions that take an excessive amount of time to run are flagged. If you wish to run these, please remove these flags from the beginning of each cell. Due to size constraints, the data files are not included within the submission, and can be obtained by running the get_embeddings function.
