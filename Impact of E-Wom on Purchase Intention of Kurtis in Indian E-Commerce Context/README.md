# IMPACT OF E-WOM ON PURCHASE INTENTION OF KURTIS IN INDIAN E-COMMERCE CONTEXT: A MIXED METHOD APPROACH

Online shopping has changed the current structure of shopping for many customers. Shopping
from e-commerce websites is not only confined as a trend, but it's the utmost need of the hour.
The current study will be done in two phases. In phase one, a conceptual model will be made,
which will be used for testing the impact of online reviews belonging to Indian ethnic dresses
on the purchase decision of the consumer. The conceptual model will be tested using a surveybased primary data collection. A descriptive analysis and hypothesis testing would be
performed based on the data collected. In the second phase of the study, the online review will
be web-scrapped from the different e-commerce portals like Amazon and Flipkart.
Different levels of analysis will be performed for textual and image
datasets. Once the textual reviews are retrieved, the data is pre-processed both computationally
and to some extent manually.The next analytical
steps involved would be product feature extraction, emotional classification of the reviews, text
classification model for a recommendation, and topic modelling. 

## Motivation for the Study
The impact of electronic word-of-mouth (e-WOM) on the online purchase decision is a wellresearched area. However, the impact of e-WOM on the purchase of Indian ethnic dresses have
not been given due importance in past literature. Additionally, the insights hidden in the online
reviewers regarding the behavioural characteristics of female buyers, especially in the context
of Indian ethnic dresses, is not yet studied in extant literature. In fact, this is the motivation for
the current study to understand the factors that impact the purchase decision of buyers during
e-buying of Kurtis and further examine the e-WOM or online reviews scrapped by prominent
e-retailers in India by adopting a text mining approach.

## Scope of the Study
The study's scope is limited to just female Kurtis from all Indian ethnic garments. For this
study, the online reviews are analyzed from only three e-commerce portals: Amazon, Flipkart,
and Snapdeal.

## Research objectives
For the research, the following objectives are defined:
1. Study the factors that impact the purchase decision of buyers of e-retail stores in the
context of Indian ethnic wear
2. Develop a conceptual model to abstract the relationship of online purchase decision and
its impacting factors
3. Identify the key product features that are more discussed in online reviews for Kurtis
4. Extract the sentiment polarity of various product features from online reviews and
building a relationship on customer satisfaction
5. Develop an online purchase recommendation model based on textual features
6. Perform latent semantic analysis to identify critical factors that affect customer
satisfaction
7. Explore the impact of extracted topics on consumers’ evaluations

## Conceptual Model and Hypothesis
![hypo](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/hypo.png?raw=true)

## RESEARCH METHODOLOGY
### Research Study 1
This study is a causal investigation into the impact of Review quality, Negative reviews,
Positive reviews, Textual reviews, Image reviews, Video reviews, and Perceived value on eWOM engagement and Purchase intention in ecommerce portal. This study’s participants are
female Facebook users. This study’s population includes any female who has a Facebook
account and is a frequent and active user.

###  Sampling Technique used
Snowball or Judgmental sampling technique.
### Research Instrument
[Quetionaire](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Quetionaire.pdf) is prepared.

### Data Collection
A closed-ended questionnaire was used to obtain information. To collect data, a web-based
questionnaire was distributed among the respondents. “Google forms” were constructed to
collect data.

## Research Study 2
### Data Collection
The dataset of customer reviews was extracted from 2 websites, Flipkart and Amazon. Total of 17,000 review were [scrapped](https://github.com/VISHVAJITK/-PersonalProjects/tree/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Scrapping).

### Data Pre-processing
- Manual labeling as – ‘Recommended’ or ‘Not
Recommended’ 
- Data cleaning (checked for any misspelled words and use of Hinglish )
- tokenization (words tokanise and sentences tokanise, using
nltk.sent_tokenize and nltk.word_tokenize). 
- stemming and Lemmatization using
Porter Stemmer, nltk.stem.
 WordNetLemmatizer.

- Stopwords are removed from the data except ‘not’, because ‘not’ is a very important influencer
through negation.
- Data Balancing (upsampled the negative class data)

check the [Data anlysis](https://github.com/VISHVAJITK/-PersonalProjects/tree/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Data_analysis) notebooks for implementaion.

## DATA ANALYSIS AND RESULTS
### For Research Study 1
#### Demographic data

![dempgraphic](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/demographic.png?raw=true)

#### Test carried out
- Reliability Test (Cronbach's alpha)
- Convergent Validity
- discriminant Validity
- Confirmatory Factor Analysis (chi-square,RMSE etc.)

####  Hypothesis Testing

![hypothsis](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/hypothsis.png?raw=true)

### For Research Study 2
####  Word Cloud Analysis
![cloud](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Images/Recommended%20wordcloud.png?raw=true)

#### Emotion Analysis
Emotion analysis for each review is performed using the library file, text2emotion. Upon the
analysis, the function returns scores for each of the emotions, angry, sad, happy, surprise, and
fear. It is observed that for certain entries, all the fields are observed to be 0, so it is labeled as
neutral. check the [notebook](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Data_analysis/word_cloud.ipynb) for details.

![emotion1](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Images/Emotion%20for%20recommendation.png?raw=true)
![emotion2](https://github.com/VISHVAJITK/-PersonalProjects/blob/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/Images/emotion%20for%20non%20recomedation.png?raw=true)

## Text Classification Model for Recommendation
Take the two classes Recommender (Class 1) and Not-Recommended (Class 2) for classification. Accuracy, F1-score,
sensitivity, and specificity are the performance metrics used in this study. All of this is used to
determine the performance of our model.
check the [notebook](https://github.com/VISHVAJITK/-PersonalProjects/tree/main/Impact%20of%20E-Wom%20on%20Purchase%20Intention%20of%20Kurtis%20in%20Indian%20E-Commerce%20Context/classification) for details.

The BERT model for 100 epochs is built for recommendation with 93.42 % accuracy.

## 7.1 Conclusion
The primary goal of the study was to determine the factors that affects e-WOM engagement
and purchase intention of Indian consumers. From all the factors, only five were considered to
be of greater importance. Review quality, positive reviews, video reviews, perceived value,
and e-WOM engagement were found to be important factors whereas factors like negative
reviews, textual reviews, and image reviews found to be insignificant. The study highlights the
importance of e-WOM towards the formation of intentions for online purchase. These findings
are vital for the online shopping sites to help them make customers buy products from their
websites. In addition, people satisfaction/dissatisfaction about a particular product analysed
through online reviews. Through Sentiment and emotional analysis, it is known that people are
happier and giving more positive reviews to a product. Still, we can’t ignore the negative
reviews provider and those customers who provide sad/angry/fear as emotions. Companies
should take there queries very seriously and resolve their issues. Companies should focus more
on customer feedback and the trend, then changes in there product according to the customers
requirement.
## Future Research
This study only focuses on the Kurtis from all Indian ethnic dresses. So, there is a scope
to study on other Indian ethnic dresses. Factors like negative reviews, textual reviews and
image reviews comes insignificant but previous studies says that these are the most important
factor. So, there is a scope to analyse these factors, why it is coming as insignificant. Other
limitations may be, as the sample size is only restricted to 250 due to time constraint, the factors
might not come as significant. So, by increasing the sample size, further analysis can be done.
In this study, only textual reviews are analysed. So, there is further scope to analyse image or
video reviews. The image data that is collected from the reviews can be treated for computer
vision methods wherein an image comparison analysis is performed between the images
depicted by the retailer and the actual product received. 
