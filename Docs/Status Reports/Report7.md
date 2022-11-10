## Work Done
* I adapted my addEntity function to deal with sentences that contain multiple relations
* I made my relevantText function more accurate and general
* I researched transformer heads and existing implementations for them
* I investigated how I can extract specific embeddings

## Findings
* I realised that my tokeniser isn't familiar with the syntax of my entity tags, so it's splitting them up when tokenising.
* I might have to go about how I am tagging entities differently, since I am tagging every single mention of any chemical or gene in text instead of the ones with actual relations.

## Questions
* Would it be a problem if you had the same entity tag names across sentences? e.g. If I tag one entity in one sentence with [E1] and then another entity in a different sentence with [E1] as well.
* If there are entities which aren't part of a relation, do we still tag them?
* Is there a way to add tokens to a pretrained tokeniser so that the elements of the tags aren't tokenised separately e.g [E1] -> [E1] instead of [E1] -> '[', 'e1]'