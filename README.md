 <h1><img src=https://i.imgur.com/QPFf1hw.png style="float: left; margin: 10px;"> 

# Topic Modeling to Identify Women's Health Concerns on Online Forums

**Author:** Jocelyn Lutes

## Project Background

Citizen science is an emerging field of research in which members of the public volunteer to participate in scientific research [(1)](https://www.citizenscience.gov/about/#). One of the most well-known, crowd-sourced citizen science is projects is [American Gut](https://msystems.asm.org/content/3/3/e00031-18), a citizen science project designed to better understand the human microbiome. For this project, citizens interested in contributing to the project paid $99 to receive a sample collection kit and were given instructions to submit the sample [(2)](https://anesthesiology.duke.edu/?p=846744). Within approximately five years, it was estimated that American Gut received samples from over 11,000 people in 45 different countries [(2)](https://anesthesiology.duke.edu/?p=846744), illustrating the willingness of individuals to participate in research and the power of citizen science for generating large datasets that can answer important research questions.

The field of developmental neurotoxicology is interested in understanding the developmental origins of the nervous system throughout the lifespan [(3)](https://www.dntshome.org). Within this field, a substantial amount of research is dedicated to understanding how events that occur during a woman's pregnancy (e.g. illness, treatment with medication, psychological distress, etc.) impact the development of the baby's brain and behavior. Traditional research within the field of maternal health and infant development has relied on maternal report of any events that occurred during pregnancy through regularly-scheduled interviews with a trained research assistant or counselor. Although these interviews provide important information for the studies, the accuracy of reporting depends on the ability of the expecting mother to recall any important events that happened during her pregnancy. 

In order to eliminate any gaps in reporting and to gain a more-representative picture of a woman's life and pregnancy, we would like to to plan a citizen science project in which women who are interested in participating can download a mobile application that would allow them to log important events during their pregnancy in real time. However, understanding that this will be a large time commitment for participating women, we would also like to provide them with specially curated, expert-contributed resources related to women's health concerns. 

## Problem Statement
In order to ensure that any resources that are provided in the application are relevant to potential users, the project leads have proposed that we use an open-ended survey or multiple focus groups to identify several women's health concerns. However, surveys and focus groups can be costly in terms of both time and money, and the project is operating on a limited budget and needs to be completed as quickly as possible. Additionally, it is possible that the small number of women who would be invited to join a focus group or to receive a survey would not be representative of the larger population of women who could opt to particpate in the research. Therefore, the data science team was tasked to uncover an alternate way to identify women's health concerns.

In this project, **I will use natural language processing and unsupervised techniques, such as clustering and topic modeling, to identify women's health concerns from posts in online forums.** Specific concerns will be identified for general women's health and fertility and pregnancy. Topic quality will be examined using scoring metrics and by assessing interpretability.

## Executive Summary

### Data Collection
Data was collected on August 7, 2020 using the [Pushshift Reddit API](https://github.com/pushshift/api). This API allows for easy aggregation of posts from Reddit.com. For each health domain, data was collected that spanned from February 16, 2019 to August 7, 2020 (a period of approximately 17.5 months).    

**1. General Women's Health Data:**  
* Posts relating to general women's health concerns were collected from [r/WomensHealth](https://www.reddit.com/r/WomensHealth/), [r/obgyn](https://www.reddit.com/r/obgyn/), and [r/thegirlsurvivalguide](https://www.reddit.com/r/TheGirlSurvivalGuide/). 
* This resulted in a total of 31,385 posts from 19,753 unique users.

**2. Fertility and Pregnancy Data:**  
* Posts relating to fertility and pregnancy were collected from [r/TryingForABaby](https://www.reddit.com/r/TryingForABaby/), [r/pregnant](https://www.reddit.com/r/pregnant/), and [r/BabyBumps](https://www.reddit.com/r/BabyBumps/). 
* This resulted in a total of 98,138 posts from 35,127 unique users.


### Data Cleaning and Preprocessing
Once data was in hand, all data was cleaned to check for missing values and inappropriate data types. HTML tags, Reddit-specific tags (e.g. "[removed]", "[deleted]"), URLs, and digits were removed from the text. 

Once the data was cleaned, a custom list of stop words was defined, and posts were lemmatized using ***spaCy***. (Lemmatization refers to the process of reducing a word to its base root.) 

Prior to modeling, a document term matrix was created using the tf-idf vectorizer by ***Sklearn***. (Tf-idf creates a bag of words with a weight for each word that is based upon the number of times a word appears in a post and the number of posts that it appears in. If a word appears in many documents, it will receive a low ranking.) If a ***Gensim*** model was used, the document term matrix was further processed to create a ***Gensim*** corpus. 

### Topic Modeling
Topics of concern related to women's health were identified using K-Means Clustering and Latent Dirichlet Allocation (LDA). For each model, the number of clusters or topics chosen are believed to represent a balance between a scoring metric (Silhouette Score for K-Means and UMass Cohesion for LDA), topic separation (as illustrated by pyLDAvis for LDA), and interpretability. 

## Contents of Repository
* [**Assets**](https://github.com/jlu90/Identifying-Womens-Health-Concerns/tree/master/assets)   
* [**Code**](https://github.com/jlu90/Identifying-Womens-Health-Concerns/tree/master/code):
    * [Data Collection](https://github.com/jlu90/Identifying-Womens-Health-Concerns/blob/master/code/01_Data_Collection.ipynb)
    * [Main Project Notebook (LDA)](https://github.com/jlu90/Identifying-Womens-Health-Concerns/blob/master/code/02_Main_Project_Notebook.ipynb)
    * [Determining the Optimum Number of Topics/Clusters](https://github.com/jlu90/Identifying-Womens-Health-Concerns/blob/master/code/03_grid_search_models.ipynb)
    * [Supplemental Modeling (K-Means)](https://github.com/jlu90/Identifying-Womens-Health-Concerns/blob/master/code/04_supplemental_modeling_notebook.ipynb)
* [**Data**](https://github.com/jlu90/Identifying-Womens-Health-Concerns/tree/master/data)   
* [**Presentation**](https://github.com/jlu90/Identifying-Womens-Health-Concerns/tree/master/presentation)   


## Data Dictionary
The cleaned and preprocessed data for both domains follows the following format:
Column | Data Type| Description
-|-|-
subreddit| string| Name of subreddit from which the post was obtained
author | string| Username of post author
timestamp| datetime| Date of post (YYYY-MM-DD)
total_text| string| Original text of the post
lemma_text| string| Text that has been lemmatized using spaCy
sentiment_score| float| Normalized sentiment polarity of post, ranging from -1 (Negative) to 1 (Positive) 

## Product Recommendations

Overall, these analyses have shown that concerns related to women's health at various life stages can be identified using topic modeling techniques, such as Latent Dirichlet Allocation. 

Based on the identified clusters, I recommend that the following areas of women's health would benefit from having expert-provided advice and should therefore be considered for inclusion in the mobile application:

**For Non-Pregnant Users**
1. Menstrual Cycle Abnormalities
2. Feminine Hygiene Products
3. Birth Control Options
4. Symptoms of Infections
5. Common Gynecological Issues (Including pains)
6. Fertility Options

**For Pregnant Users**
1. Determination of pregnancy and early pregnancy symptoms
2. Coping with pregnancy life changes
3. Dealing with nausea and vomiting during pregnancy and sleep disruptions
4. Obstetrics Appointments (Including pain and body changes)
5. What to expect during labor and delivery


Understanding the serious nature of these areas of concern, for any pain, gynecological and obstetric issues, or mental health struggles, we will also emphasize that any content within the mobile application is not meant to replace discussions with a health care provider and will encourage users to seek help from their physician. 

## Conclusion

* This project provides proof-of-concept that, given the correct data, topic modeling with Latent Dirichlet Allocation can provide important insights into information that is normally gained through user surveys or focus groups and could become an important step in product development. 

* K-Means Clustering was not a successful technique for identifying topics in this data.

* In comparison to focus groups or surveys, this project was able to analyze data from 19,753 unique users in the General Women's Health Data and 35,127 unique users in the Fertilty and Pregnancy data. Collecting the same quantity of data using surveys or focus groups would likely cost more financially and in terms of time.

* The biggest limitation to topic modeling is interpretation of clusters, but adequate research and background knowledge can facilitate this process.

* Next Steps:
    * Topic Modeling of concerns during Postpartum/Early Parenthood period
    * Identification of concerns for data collected pre- and post-COVID-19
    * Topic modeling within previously-identified topics

## References

[American Gut](https://msystems.asm.org/content/3/3/e00031-18)  
[Citizen Science](https://www.citizenscience.gov/about/#)  
[DNTS](https://www.dntshome.org)  
[First Major Results of “American Gut Project” Published](https://anesthesiology.duke.edu/?p=846744)  
[Latent Dirichlet Allocation](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)  
[Stemming and Lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)  

### Helpful Tutorials and Resources
[Coherence Scores - StackOverflow](https://stackoverflow.com/questions/54762690/coherence-score-0-4-is-good-or-bad)  
[Document Clustering with Python by Brandon Rose](http://brandonrose.org/clustering#Hierarchical-document-clustering)  
[KMeans Text Clustering by Learn Python](https://pythonprogramminglanguage.com/kmeans-text-clustering/)  
[Natural Language Processing in Action by Hobson Lane](https://www.amazon.com/gp/product/1617294632/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)  
[NLP in Python Tutorial by A Dash of Data](https://github.com/adashofdata/nlp-in-python-tutorial)  
[Natural Language Processing with Python by Jose Portilla](https://www.udemy.com/course/nlp-natural-language-processing-with-python/)  
[Topic Modeling with Gensim by Machine Learning Plus](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)   





