# Work Done
* I did some debugging for my classifiers
* I wrote the introduction and parts of other sections for my dissertation.
* I wrote the code for the multiclass classification section.
* You can view my overleaf dissertation template [here](https://www.overleaf.com/read/sffzvhfckzyd)

# Findings
* The F1 score for CLS binary classification increased from 0.69 to 0.84. The issue I was having was that some of my tags weren't separated by whitespace, so they weren't picked up by the tokenizer. This meant that the labels weren't assigned to the correct entities.
* I found out that some of the indexes for my entity labelling function weren't bounded correctly by sentence, so it was duplicating various entity labels.
* I found out that some sentences didn't have both start and end tags in it, and the locations of some of the tags were offset for some reason, so it was impacting the cartesian product function, causing a different in the number of embeddings and labels.
* One problem I noticed when debugging is that several of the entities annotated within the text appeared across sentences or weren't annotated correctly. E.g. for one with pubmed id 17006762, one of the genes was labelled "rat brain. LDH1", which I'm fairly certain is a mistake. Consequently the entity was determined to be in the wrong sentence, causing the cartesian product to be calculated incorrectly. Another one is "SUR1. 6." in pubmed 9647478, where '6.' is a numbered bullet in the abstract.
* Another problem I noticed as that some entities have '.' in their name which segtok is mistaking for a full stop. For example, "Bacillus circulans ssp. alkalophilus phosphoserine aminotransferase" is being split into two sentences. The relevant document hasn't got any relations in it but it is still possible that similar examples will cause extra cartesian product calculations where there aren't any, causing an imbalance in the number of labels and the number of embeddings.
* A quick fix for this was to replace all '.' with whitespace within entities, however the labelled indices for the entity still occur across two sentences. This did reduce the difference in the number of embeddings and labels so it's an improvement.

# Notes
* My plan is to draft specific sections of the dissertation and show them to you so I can get some feedback. This month will likely focus on the introduction and background sections specifically. I'll probably ask you some general questions about the rest of it this month too.
* Since I haven't completed my implementation yet, I'm planning on doing it as I go and writing the relevant sections once I'm done with a specific part.
* Parts of the implementation I haven't finished yet
    * Having a fully functional entity tag pipeline (The foundations are down but there's some debugging to do)
    * Running the pipeline with some dropout
    * Running the pipeline with the entity names omitted
    * Potentially more regularisation methods etc if I have time

# Questions
* What could I improve with what I've written in my dissertation so far?
* I'm planning on running the pipeline with different levels of dropout to compare. Is it ok to just use the dropout parameter for the BERT model or am I missing something?
* Is it ok if I use the diagrams from other papers if I reference them or should I just create my own?
* Are comparing architectures, entity marking/masking and applying dropout sufficient enough or do I need to come up with more things to compare? 
* What should I do about entities that are labelled across sentences?
* How crazy am I to go with the slides for Friday?