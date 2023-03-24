# Work Done
* Started re-structuring my dissertation
* Started introducing the development set into the mix
* Found [this paper](https://link.springer.com/chapter/10.1007/978-3-030-76508-8_11#chapter-info) that tested different dropout hyperparameters on BERT

# Findings
* Initial difference of 32 between embeddings and labels
* I read up more about dropout with BERT and it would seem that dropout applies to all layers of BERT, with default probability of 0.1
* Bert has two dropout parameters: attention_probs_dropout_prob which applies dropout to BERT's attention layers and hidden_dropout_prob, which applies to all of BERT's hidden layers.
* According to the paper above, performance tends to degrade with dropout probabilities past 0.6, though I read that apparently the most effective parameters lie between 0.5 and 0.8.
* The difference in embeddings and labels for the development set is only 4 (4 more labels)

# Questions
* What should I do about the weird dataset issue I'm having? (i.e. Some entities and indexes being all wack)
* When I classify the relations, it (quite fairly) predicts the vast majority of them as having no relation. What I'm doing is classifying the relations that the model has considered as having a positive relation into specific relations. It just seems a bit sloppy. Is there a way of improving this?