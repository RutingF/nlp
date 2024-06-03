# NLP Projects 

This repo contains common NLP projects such as the following:
* Sentiment Classification 
* Topic Modeling
* Extracting dates out of raw text

## Extracting Dates 
Using RegEx to extract dates in various formats from raw text. 

### Files 
Function and demonstration are in the same Jupyter Notebook: <b>date_extraction_RegEx.ipynb </b>

## Sentiment Classification 
Evaluating 5 different combinations of models & features: 
* Multinomial Naive Bayes classifier model w/ Count Vectorizer
* Multinomial Naive Bayes classifier model w/ TFI-DF Vectorizer 
* SVM w/ TF-IDF Vectorizer and an additional feature (document length)
* Logistic Regression model w/ Tfidf Vectorizer 
    * Additional Features:
        * Document length
        * Number of digits per document 

* Logistic Regression model w/ Count Vectorizer
    * Additional Features:
        * Document length
        * Number of digits per document
        * Number of non-word characters 

### Measurement
AUC (Area Under the Curve)

### Files 
<b> sentiment_classification.py </b>

Python module storing functions for sentiment models and features 

<b> sentiment_analysis.ipynb </b>

Jupyter notebook demonstrating the usages of <b> sentiment_classification.py </b>






