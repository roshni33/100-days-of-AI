# 🏠 House Price Prediction Project

## 📚 Overview
In the Boston House Price Prediction Project, we are building a predictive model to evaluate the price of a house with provided parameters.

The parameters taken into consideration are - Per Capita Crime Rate by Town, Nitric Oxide Concentration, Weighted Distances to five Boston Employment Centres, Tax, etc.

## 🧩 Key Features
- Analyzed and visualized data to understand correlations between variables.
- Employed various regression algorithms to find the most accurate predictions.
- Evaluated model performance using metrics such as R-squared and Mean Absolute Error (MAE).

## 🔍 Data Description
The dataset includes the following columns:

| Column | Description |
|--------|-------------|
| **CRIM** | Per capita crime rate by town |
| **ZN** | Proportion of residential land zoned for lots over 25,000 sq.ft. |
| **INDUS** | Proportion of non-retail business acres per town |
| **CHAS** | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
| **NOX** | Nitric oxides concentration (parts per 10 million) |
| **RM** | Average number of rooms per dwelling |
| **AGE** | Proportion of owner-occupied units built prior to 1940 |
| **DIS** | Weighted distances to five Boston employment centres |
| **RAD** | Index of accessibility to radial highways |
| **TAX** | Full-value property-tax rate per $10,000 |
| **PTRATIO** | Pupil-teacher ratio by town |
| **B** | 1000(Bk - 0.63)² where Bk is the proportion of blacks by town |
| **LSTAT** | % lower status of the population |
| **MEDV** | Median value of owner-occupied homes in $1000's |

## 🔄 Data Preprocessing
No data preprocessing was required as there were no null values in the dataset.

## 📊 Correlation Analysis
Understanding the correlation between variables is essential for predicting the target variable. A heatmap was plotted to visualize these relationships.



The heatmap analysis reveals that the number of rooms (RM) has a strong positive correlation (0.7) with house prices, indicating that more rooms lead to higher prices. Conversely, the percentage of lower status populations (LSTAT) shows a strong negative correlation (-0.74), suggesting that higher percentages result in lower prices. Additionally, nitric oxides concentration (NOX) has a moderate negative correlation (-0.43) with prices, while radial highway accessibility (RAD) has a moderate positive correlation (0.39), indicating better accessibility can increase prices. Lastly, the age of houses (AGE) has a slight negative correlation (-0.38), implying older houses are generally priced lower than newer ones. These insights are crucial for feature selection in building a predictive model for house prices.

## 🧪 Model Development
Multiple regression algorithms were tested, including:
- **Linear Regression**
- **Support Vector Machine (SVM)**
- **Decision Trees**
- **K-Nearest Neighbors (KNN)**
- **Random Forest Regressor**
- **XGBoost Regressor**

## 📈 Performance Metrics
The following table summarizes the performance of each model based on R-squared and Mean Absolute Error:

| Model                  | R-squared (Train) | R-squared (Test) | Mean Absolute Error (Train) | Mean Absolute Error (Test) |
|------------------------|--------------------|------------------|------------------------------|-----------------------------|
| **Linear Regression**  | 0.728              | 0.778            | 3.384                        | 3.113                       |
| **K-Nearest Neighbor** | 0.679              | 0.658            | 3.570                        | 3.919                       |
| **Support Vector Machine** | 0.999          | 0.204            | 0.098                        | 5.862                       |
| **Decision Tree**      | 1.0                | 0.723            | 0.0                          | 3.485                       |
| **Random Forest**      | 0.982              | 0.894            | 0.816                        | 2.097                       |
| **XGBoost**            | 0.962              | 0.924            | 1.403                        | 1.960                       |

## 🔍 Insights
- **KNN**: Reasonable learning with R² scores around 66-67%, but could improve with hyperparameter tuning.
- **SVM**: High training performance but suffers from overfitting.
- **Random Forest vs. XGBoost**: Random Forest shows high training performance, while XGBoost generalizes better to unseen data.
- **Linear Regression**: Good fit with slight overfitting.
- **Decision Trees**: Perfect fit on training data but significant overfitting.

## 🏆 Best Model
The **XGBoost Regressor** outperformed other algorithms, achieving the best balance between training and testing performance.

## 🚀 Conclusion
This project demonstrates the importance of model selection and evaluation in predictive analytics. The XGBoost algorithm proved to be the most effective for predicting house prices in Boston.

