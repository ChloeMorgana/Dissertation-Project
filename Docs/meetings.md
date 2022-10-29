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
    * I asked Jake for more information about the differences between BioBERT and PubMedBERT, and he explained that BioBERT was pretrained using generic data from the English language, then fine-tuned using PubMed articles, whilst PubMedBERT was pretrained and fine-tuned using PubMed atricles.
    * I then asked about whether or not I should use PubMedBERT pretrained on abstracts or the entire text. He said that the abstract version might be good because it might pick up on language specific to abstracts, however the full text may provide more context overall and to experiment.
    * Jake then advised me to be aware of how the tensors change size depending on the number of input dimensions.

## Week 5
* 25/10/2022 [- mins]
    * The meeting this week was conducted via email, therefore wasn't under any particular timeframe.
    * This meeting involved Jake answering some of my concerns with the encoding step of my implementation, such as how BERT recognises tagged text e.g. Tagging @DRUG$ and @Prot$, and how that would behave differently compared to using start and end tags within the text to identify the beginning and the end of each entity.
    * I then asked if relations were bidirectional within the text and if it mattered which one was classed as the head entity and which is classed as the tail entity. He said to keep it consistent and that they aren't generally bidirectional.
    * I then asked why the classification layer should be specifically applied to the CLS token, and Jake explained how there are several ways to classify sentences, either by averaging all of the context vectors within the sentence, or by training the CLS token to capture meaning relevant to what you are trying to classify.