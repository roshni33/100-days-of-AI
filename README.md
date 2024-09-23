# 🛳️ Titanic Survival Prediction Project

**Topics Covered**: Data cleaning, exploratory data analysis (EDA), feature engineering, classification algorithms (e.g., Logistic Regression).

## 📚 Overview
The **Titanic Survival Prediction** project aims to predict passenger survival using machine learning techniques. This project covers key concepts in data preprocessing, exploratory data analysis (EDA), feature engineering, and classification algorithms.

**Columns**
- **Survived**: 0 = No, 1 = Yes
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Cabin**: Cabin number
- **Embarked**: Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)


## 🧹 Data Preprocessing
Preprocessing is essential for preparing the data for analysis. Here are the key steps:

### **Dropping Unnecessary Columns:**
Identify and remove columns that do not contribute to the prediction.

### **Handling Missing Values:**
- **Mean**: Best for normally distributed data without outliers.
- **Median**: Useful for skewed data or when outliers are present.
- **Mode**: Ideal for categorical data; replaces missing values with the most frequent value.
- **Null Strings**: Replace missing values in string columns with an empty string.

```python
df.fillna(df.mean(), inplace=True)  # Example for mean
```
- **Encoding Categorical Variables** : Transform categorical variables into numerical format.

```
df.replace({'Sex': {'male': 0, 'female': 1}}, inplace=True)
```

## 📊 Exploratory Data Analysis (EDA)

EDA focuses on understanding the data through visualization and summary statistics.

There is a **difference between preprocessing and EDA(Exploratory Data Analysis)**
EDA (Exploratory Data Analysis) focuses on understanding the data through visualization and summary statistics

## 🧮 Algortihmic overview
In cases where the output is binary (e.g., 0/1 or Yes/No), the problem is classified as a binary classification problem. Among the various classification algorithms available, **Logistic Regression** is particularly well-suited for this type of analysis due to its effectiveness in modeling the probability of a categorical outcome.

## 📈 Visual Insights
The counterplot visualizations reveal:

- Fewer people survived compared to those who died.
- Among all passengers, more males than females were aboard.
- Despite having fewer females, a higher proportion of them survived.