# Meeting Log

## Week 2
* 03/10/22 [20 mins]
    * This was the introductory meeting in which Jake elaborated on the logistics of the project. We discussed the dataset that I’ll be using to perform extraction methods on and he agreed to send me several sources relating to different topics in the biomedical field to choose from. I’ve been tasked with using Google Scholar to look up various research papers relating to the topic.
    * Later this day, Jake sent me an email providing me with links to different datasets, in addition to some resources explaining relation extraction.

## Week 3
* 11/10/22 [20 mins]
    * We had a discussion about the type of dataset that I had chosen, namely the CDR corpus, and Jake informed me that using the DrugProt corpus may be more appropriate, since it indicates specific mentions of chemicals and diseases to focus on.
    * We discussed that using deep learning methodologies may be the most appropriate for this relation extraction task, and established that my goal for this week was to investigate BERT.
    * Jake also warned me about certain technologies that I had investigated, particularly DNorm, stating that sometimes it might be necessary to add some conditional statements to make it function appropriately.
    * I also need to investigate different error analysis techniques in order to observe different errors in the model I create.
    * Jake suggested I gain an account to use a GPU machine in order to process large amounts of data and not overwhelm my laptop, and also suggested that I use either Google Colab or Kaggle to write my code with.
    * Later that day, I was sent some links to Google Colab notebooks that he created explaining how to load the data for each dataset, in addition to a blog about working with contextual vectors with HuggingFace.

## Week 4
* 18/10/22 [20 mins]
    * I asked Jake about formatting the dataset into a pandas dataframe given a number of nested dictionaries. We discussed the pros and cons of using pandas to format data in a nice way. It tends to be good in a more general sense, however it doesn't provide much benefit to the specific requirements of this task.
    * I asked Jake for more information about the differences between BioBERT and PubMedBERT, and he explained that BioBERT was pretrained using generic data from the English language, then fine-tuned using PubMed articles, whilst PubMedBERT was pretrained and fine-tuned using PubMed articles.
    * I then asked about whether or not I should use PubMedBERT pretrained on abstracts or the entire text. He said that the abstract version might be good because it might pick up on language specific to abstracts, however the full text may provide more context overall and to experiment.
    * Jake then advised me to be aware of how the tensors change size depending on the number of input dimensions.

## Week 5
* 25/10/2022 [- mins]
    * The meeting this week was conducted via email, therefore wasn't under any particular timeframe.
    * This meeting involved Jake answering some of my concerns with the encoding step of my implementation, such as how BERT recognises tagged text e.g. Tagging @DRUG$ and @PROT$, and how that would behave differently compared to using start and end tags within the text to identify the beginning and the end of each entity.
    * I then asked if relations were bidirectional within the text and if it mattered which one was classed as the head entity and which is classed as the tail entity. He said to keep it consistent and that they aren't generally bidirectional.
    * I then asked why the classification layer should be specifically applied to the CLS token, and Jake explained how there are several ways to classify sentences, either by averaging all of the context vectors within the sentence, or by training the CLS token to capture meaning relevant to what you are trying to classify.

## Week 6
* 01/11/2022 [30 mins]
    * I asked Jake if there was any benefit to using entity masking over entity marking and he said that it reduces the risk of BERT learning patterns specifically referencing the entity names.
    * He then went on to discuss dropout, which essentially randomly removes neurons so that the transformer model learns to not be reliant on a particular neuron, promoting generalisation.
    * I asked Jake about mention pooling and entity start methods for using embeddings and to explain them more thoroughly and he referred me to a paper explaining them in more depth.
    * I then asked about presenting the data that I find and he said to emphasise error analysis.
    * I asked about whether or not the embeddings are independent from one another and he said that initially they are, but as you travel down the layers they take each other into account.

## Week 7
* 08/11/2022 [30 mins]
    * This meeting was mostly surrounding the classification step of the implementation. I asked questions about how I could arrange the entity start tags in sentences containing multiple relations, and we got onto the conversation of using transformer heads to adjust the existing neural network to train it more on the task of classifying relations.
    * I asked about the size of the softmax vectors produced after the softmax layer and he said that it's the (batch size * the number of labels)
    * I also asked if I would be penalised for not using branches in my repo and he said that it's fine not to use them
    * I asked if the vectors produced from concatenating the embeddings would have to be reduced back down to 768 and he said that isn't necessary

## Week 8
* 15/11/2022 [15 mins]
    * This meeting was to clarify certain issues I was having regarding my entity tags. The first was that I wanted to know how to create my own tokens to insert into the tokeniser. Apparently huggingface has one called add_special_tokens, which Jake said he would send me documentation for. He also suggested that I use convert_ids_to_tokens to verify that certain tokens are as intended.
    * I then talked about how the [CLS] embeddings wouldn't represent a singular relation in several circumstances and asked what I could do to rectify this, and he said that it is just the nature of [CLS] embeddings and that I can use this as a baseline to compare my other methods with.
    * I started talking about how several chemicals and genes can occur in one sentence, and that it wouldn't be convenient to concatenate all of the resulting vectors from these, and Jake said that I could just tag specific chemicals and genes and concatenate those.
    * The idea is to generate candidate relations by finding every combination of chemical and gene in a sentence and finding the embeddings for these relations.

## Week 9
* No meeting this week

## Week 10
* 29/11/2022 [15 mins]
    * This week primarily focused on issues with the tokenizer, which mostly boiled down to different behaviours stemming from different types of tokenizers and models.
    * I also asked Jake when I need to give him the progress report by and he said by Christmas.
    * I updated him with my progress and informed him that I now have a functional pipeline.

# Week 13
* 09/01/2023 [30 mins]
    * This week primarily involved admin regarding the structure of our meetings and approach to dissertation writing this semester.
    * I asked Jake about implementing dropout and he said to do some research on which layer the dropout is acting on and how to implement it with BERT
    * I asked if what I intend to implement is enough and he said that it's more than enough
    * He said to make sure that I reference where I got images from within my dissertation.
    * When I brought up potentially trying marking/masking he said he was very interested in the idea of using entity masking as a form of dropout, and that it could potentially be something that I investigate in my implementation.
    * In terms of the structure of my dissertation, he suggested that I merged the analysis and design sections and create a section that proposes a set of research questions that can be analysed further.

# Week 14
* 16/01/2023 [10 mins]
    * This week focussed on class imbalance solutions. I expressed concern about the results of my classifier, stating that it had mostly classified everything as having no relation since that was the case the majority of the time.
    * Potential solutions include adjusting the logistic regression class_weight parameter to 'balanced', or to perform data resampling.
    * I also asked about my method of using logistic regression twice to find the intended results, and he said that it could potentially manifest into an additional research question to put into my report.

# Week 15
* 23/01/2023 [20 mins]
    * The theme of this meeting was the structure of the dissertation. I was asking about how thorough I needed to be with the background section in terms of the explanation of concepts, and he said that it would be best to explain as much as possible and emphasise the link to the motivation and reasoning behind why certain parts have been explored.
    * I then asked how long I need to make the presentation and what I need to include.

# Week 16
* 30/01/2023 [20 mins]
    * I asked about whether or not I should create my own masked entities to represent each chemical or gene or just use a default mask. Jake said to start with the default one since BERT can recognise that one more easily.
    * I then asked about what I could use the validation set for and he said to change parameters for logistic regression, in particular the c parameter which performs regularisation.
    * I asked about a bonus section for the dissertation and he said to combine the design and implmentation sections
    * Finally, I asked about how terrible my values can be to still be acceptable, and he said that as long as the results aren't too extreme e.g. 0.0 or 0.99, then they are acceptable.
    
# Week 18
* 13/02/2023 [20 mins]
    * This week I expressed that I wanted to create an end-to-end system to compare with my existing results.
    * I asked Jake for recommendations regarding resources I could use to assist me in implementing fine-tuning for BERT, since the majority of the ones I found seemed unecessarily complex.
    * Jake sent me a number of resources to assist me in this endeavour, including HuggingFace special task outputs and custom heads.
    * Another resource he sent was on HuggingFace's Trainer, which provides an abstraction of the process of fine-tuning so it is less complicated to implement.

# Week 19 
* 20/02/2023 [20 mins]
    * This week I talked to Jake about issues I was having implementing fine-tuning. I was having different memory problems depending on which platform I was hosting my code on.
    * Jake said it is possible that my code was having memory problems, but it could also be the number of students implementing their projects on Fidra simultaneously.
    * Jake advised me that it might be best to abandon this part of the project since it might be a bit late to be able to implement it on time.

# Week 20
* 02/03/2023 [20 mins]
    * This week I asked Jake about questions regarding my dissertation write-up.
    * I asked when he would like the first draft by and he said the 13th of March.
    * I also asked how in depth I need to go when explaining the processes of my implementation, and he said to go fairly in depth, but to avoid getting to the point where I'm explaining specific methods within my code.
    * I also asked him how in depth I should go within my background section, and he said enoough that is relevant to my task, and I should specify the pros and cons of each paper.
    * He also said to include diagrams within my dissertation, as they can help elucidate key concepts to the reader.

# Week 21
* 08/03/2023 [20 mins]
    * I asked about how strict the page count is, and Jake said that he's not expecting me to write an entire 40 pages, and that somewhere around the early 30's is acceptable.
    * I then asked if 8 pages was too much for my background section, and he said that it might be a little bit too much, but it's dependent on the content.
    * I asked him about whether implementation issues could be included in the dissertation, and he said yes
    * He then told me that for my presentation I should explain the motivation in depth.


