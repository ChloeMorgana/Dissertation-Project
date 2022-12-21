# Work Done
* I did some debugging for my classifiers
* I wrote the introduction and parts of other sections for my dissertation

# Findings
* The F1 score for CLS binary classification increased from 0.69 to 0.84. The issue I was having was that some of my tokens weren't separated by whitespace, so they weren't picked up by the tokenizer. This meant that the labels weren't assigned to the correct entities.
* Now the difference between embeddings and labels are 64 for the entity tags.

# Questions