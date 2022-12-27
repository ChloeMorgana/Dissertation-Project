# Work Done
* I did some debugging for my classifiers
* I wrote the introduction and parts of other sections for my dissertation.

# Findings
* The F1 score for CLS binary classification increased from 0.69 to 0.84. The issue I was having was that some of my tags weren't separated by whitespace, so they weren't picked up by the tokenizer. This meant that the labels weren't assigned to the correct entities.
* Now the difference between embeddings and labels are 64 for the entity tags.
* I found out that some of the indexes for my entity labelling function weren't bounded correctly by sentence, so it was duplicating various entity labels.
* I found out that some sentences didn't have both start and end tags in it, and the locations of some of the tags were offset for some reason, so it was impacting the cartesian product function, causing a different in the number of embeddings and labels.
* One problem I noticed when debugging is that at least one of the entities annotated within the text appeared across sentences or weren't annotated correctly. E.g. for one with pubmed id 17006762, one of the genes was labelled "rat brain. LDH1", which I'm fairly certain is a mistake. Consequently the entity was determined to be in the wrong sentence, causing the cartesian product to be calculated incorrectly. Another one is "SUR1. 6." in pubmed 9647478, where '6.' is a numbered bullet in the abstract.
* Another problem I noticed as that some entities have '.' in their name which segtok is mistaking for a full stop. For example, "Bacillus circulans ssp. alkalophilus phosphoserine aminotransferase" is being split into two sentences. The relevant document hasn't got any relations in it but it is still possible that similar examples will cause extra cartesian product calculations where there aren't any, causing an imbalance in the number of labels and the number of embeddings.
* A quick fix for this was to replace all '.' with whitespace within entities, however this might produce less accurate results later on with BERT.


# Questions
* What could I improve with my introduction?
* What should I do about entities that are labelled across sentences?