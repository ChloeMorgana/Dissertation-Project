## Work Done 
* This week I focused on implementing the entity markers entity start architecture from [this paper](https://arxiv.org/pdf/1906.03158.pdf)
* I wrote an entity tagging function, which encloses each entity in entity start and end tags
* Started looking into how to implement the classification layer
* Read [this blog](https://machinelearningmastery.com/softmax-activation-function-with-python/) that explains softmax in python

## Findings
* I realised the tagging function I wrote produced an undesirable output so had to spend a while debugging
* I haven't yet modified my code to accomodate sentences that contain more than one relation.
* In order to truly find out which embedding options are the best, I will have to focus this week on creating the classification layer.
* Softmax layers converts a vector of numbers into a vector of probabilities.
* There would be a vector of size 14 (?) 

## Questions
* I'm not currently using branches in my repo. Will I get penalised for this?
* If a chemical is related to more than one gene in the one sentence, would I have to create separate sentences which tag different genes?
* Do the concatenated vectors need to be reduced down to 768 again? If so, how?
* Would the size of output of the softmax layer correspond to the size of the total number of the embeddings or the number of classes?
* Would the vector of probabilities produced for each embedding be size 14 (corresponding to the 13 relations we're looking out for and the 'no relationship' relation)?
