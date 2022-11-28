## Work Done
* Added my own tokens to the tokenizer
* Changed entity function so it only does [E1] and [E2] because my previous method was too complex
* Found a way to determine whether a sentence contains a relation or not
* Did binary classification for CLS embeddings
* Wrote a function to find the cartesian product of all of the entity tags in a sentence and concatenate their embeddings.
* Started trying to do binary classifications for entity start embeddings

## Findings
* Got a score of around 0.7 for logistic regression for a small subset of the [CLS] embeddings
* Had a problem with finding the labels for the specific relation.

## Questions
* When do you want the status report?
* I noticed that my tokenizer didn't add tokens when I was using BertTokenizer rather than AutoTokenizer. Why is this?
* Would there be any discrepancies if I were to continue using BertModel with the AutoTokenizer as opposed to AutoModel?
* Is there a reason why my tokenizer converts all of my entity tags to lowercase despite being defined in uppercase? This doesn't seem to happen for other special tokens or in your colab example.