## Work Done
* I adapted my addEntity function to deal with sentences that contain multiple relations
* I made my relevantText function more general
* I researched transformer heads and existing implementations for them
* I investigated how I can extract specific embeddings

## Findings
* I had to go about how I am tagging entities differently, since I was tagging every single mention of any chemical or gene in text instead of the ones involved in relations.
* My attempt to extract embeddings went as follows: 
    * Note the indices of entity tag tokens (This is hard as I don't know which specific entities I am trying to find, since they are all tagged [En] where n is arbitrary)
    * Extract the embeddings at those indices and concatenate them (This is also hard because I would also need to find out which entity tags are related to each other)
    * Feed them through some sort of scikit classifier
* I realised that my tokeniser isn't familiar with the syntax of my entity tags, so it's splitting them up when tokenising.
* In the meantime, I decided to try the standard embedding extraction method using the [CLS] tokens

## Questions
* Is there a way to add tokens to a pretrained tokeniser so that the elements of the tags aren't tokenised separately e.g [E1] -> [E1] instead of [E1] -> '[', 'e1', ']'?
* Is there some sort of library where you can specify which embeddings you want to use?
