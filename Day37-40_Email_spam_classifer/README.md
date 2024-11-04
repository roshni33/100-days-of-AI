# 🛍️ Project: Email Spam Classification

## 🔹 Overview
The **Spam Mail Classification** project is a web-based application that uses machine learning to classify emails as spam or ham (non-spam).


## 🧹 Data Cleaning
- Dropped unnecessary columns
- Renamed column names for better understanding
- Applied label encoding


## 📊 Exploratory Data Analysis (EDA)
- **Pie Chart**: Shows the percentage of spam vs. ham messages (ham messages are more frequent)
- **Distribution Analysis**: Analyzed the number of characters, words, and sentences in the overall dataset, as well as specifically for spam and ham emails; visualized with histograms
- **Correlation Analysis**: Used a heatmap to understand feature correlations


## 🧼 Text Preprocessing ✍️
- **Lowercasing** and **Tokenization**
- Removed special characters, stopwords, and punctuation
- **Stemming** (reduced words to their root form)
- **Word Cloud**: Displayed the most repeated words in spam and ham emails
- Extracted the top 30 unique words in both spam and ham emails


## 🛠️ Model Building
- Converted text to vectors using **TF-IDF** and **Bag of Words**
- Transformed sparse arrays into dense arrays
- Implemented multiple algorithms:
  - Multinomial Naive Bayes
  - Bernoulli Naive Bayes
  - Gaussian Naive Bayes
  - Logistic Regression
  - Support Vector Classifier (SVC)
  - AdaBoost Classifier
  - XGB Classifier
  - Decision Tree Classifier
  - Random Forest Classifier
  - K-Neighbors Classifier


## 📈 Model Evaluation
- Compared performance metrics: accuracy and precision
- **Best Performer**: Multinomial Naive Bayes with 100% precision and 95% accuracy

## 🤔 Why is Naive Bayes particularly effective for classifying emails into "spam" or "ham"?
👉 Check out this video to learn more: [Why Naive Bayes is Effective for Spam Classification](https://youtu.be/O2L2Uv9pdDA?si=BfPdWJdyyWURiNlv)



## 🚀 Model Improvement
- Adjusted `max_features` parameter of TF-IDF to ignore irrelevant words
- Applied scaling techniques
- Combined models using ensemble methods with SVC and Multinomial Naive Bayes



