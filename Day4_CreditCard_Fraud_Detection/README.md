⚠️ **Disclaimer**

🚨 **Note:** The dataset is too large to upload directly. You can download the dataset from the following link:

🔗 [Click here to download](https://drive.google.com/file/d/1xr3VkhG0KECO4zsPboHuFsGgjV_ssIEc/view)

# 💳 CreditCard Fraud Detection

## 📚 Overview
"Fraud" means unauthorized and unwanted usage of an account by someone other than the owner of that account. In the ever-evolving landscape of finance and technology, credit card fraud has become a significant concern for individuals, businesses, and financial institutions.Here comes the machine learning to the rescue.

## 🔍 Data Description
some important columns which are used to predict the output:
| Column | Description |
|--------|-------------|
| **trans_date_trans_time** | Date and Time when the transaction occurred in the format DD-MM-YYYY HH:MM |
| **cc_num** | The credit card number used for the transaction, provided in scientific notation - toatal 16 digits |
| **Category** | Type of goods or services purchased like shopping,travelling,gold,house |
| **merchant** | seller where the transaction took place|
| **amt** | Amount |
| **trans_num** | A unique identifier for each transaction.Alphanumeric codes,unique,tracking individual transactions|
| **is_fraud** | target variable - A binary indicator (0 or 1) specifying whether the transaction is fraud (1) or not (0) |
| **job** | Occupation |
| **unix_time** | Time change between current and previous transaction |
| **lat,long** |Lattitude and Longitude basically merchants and cardholders location |

## 🧩 Key Features
**Data Preprocessing**:
- Handling missing values
- Handling imbalanced Dataset
- Feature Engineering
**Model Training**
- Random Forest
- K-Nearest Neighbours
**Evaluation Metrics**
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Curve

## 🔍 **Points to Note**:
**Handling Imbalanced Dataset**:
- Resampling Techniques:
  - **Oversampling**: Increase the number of instances in the minority class (fraudulent transactions) by duplicating them or generating synthetic samples (e.g., using SMOTE - Synthetic Minority Over-sampling Technique).
  - **Undersampling**: Reduce the number of instances in the majority class (legitimate transactions) to balance the classes.
- Use Ensemble Algorithm
- Do not rely solely on Accuracy,use other metrices like Precision,Recall,f1-Score,ROC-AUC

## 🤔**On what basis model is identifying which transaction is fraud or not?**:
- Model learns patterns and relationships in the dataset features.For example - 'unix_time' - transactions occurring at odd hours or unusual timings like midnight
- Other features like - 'category,' and 'job,'.example – middle class because poor don’t have credit cards.For example - job is sweeper and category is international trip 
- multiple transactions from multiple locations within a short time frame.
- If there is a change in cardholder's regular spending locations.




