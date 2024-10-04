# 📈 Stock Price Prediction Project

## 📝 Overview
This project aims to **predict stock prices** using historical market data. It leverages **machine learning algorithms** to forecast future prices based on key financial indicators. The approach includes **data preprocessing**, **feature engineering**, and **model training** to deliver an accurate predictive system.

This is a **time-series data** project where each data point is associated with a specific point in time, such as daily, weekly, or monthly intervals.


## 📊 Dataset Columns and Description
| Column         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `Date`         | The date of the stock trading session.                                       |
| `Open`         | The price of the stock at the beginning of the session.                      |
| `High`         | The highest price of the stock during the session.                           |
| `Low`          | The lowest price of the stock during the session.                            |
| `Close`        | The price of the stock at the end of the session.                            |
| `Volume`       | The number of shares traded during the session.                              |
| `Adjusted Close`| The stock’s closing price adjusted for dividends and stock splits.           |


## 🛠️ Steps Involved

### 1. **Data Preprocessing** 🔧
- Handling missing values and cleaning the dataset.
- Creating technical indicators like:
  - **MA (Moving Average)**: Calculates the average price over a certain period (e.g., 20 days, 50 days).
  - **RSI (Relative Strength Index)**:
    - **RSI < 30**: Price may rise soon (buying signal).
    - **RSI > 70**: Price may fall soon (selling signal).
  - **MACD (Moving Average Convergence Divergence)**:
    - **Trends**: Identify whether prices go up, down, or remain stable.
    - **Momentum**: Determine how fast prices change.
    - **Signal Line**: If the MACD crosses the signal line, prices may go up (buying signal).
- Generating lag features to include previous day's prices.
- Scaling features using **StandardScaler** for better model performance.

### 2. **Data Visualization** 📉
- Plotting the stock's **closing prices** and **moving averages**.
- **Heatmap** to visualize the correlation between features.

### 3. **Train-Test Split** 📂
- The dataset is split into **training (80%)** and **testing (20%)** sets.

### 4. **Modeling** 🤖
- **Linear Regression**: A simple model for predicting stock prices.
- **Random Forest Regressor**: An ensemble method using multiple decision trees.
- **Support Vector Regressor (SVR)**: A kernel-based regression technique to capture nonlinear relationships.



## 📏 Model Evaluation
- **Mean Squared Error (MSE)**: Measures the average squared difference between the predicted and actual values.
- **Mean Absolute Error (MAE)**: Measures the average absolute difference between predicted and actual values.
- **R-squared Score**: Indicates the proportion of variance in the dependent variable that is predictable from the independent variables.


## 🎯 Key Features
- 📈 **Technical Indicators**: Incorporates popular indicators like **MA**, **RSI**, and **MACD**.
- 🔄 **Tried Multiple Models**: Linear Regression, Random Forest, and SVR.
- 📊 **Data Visualization**: Includes heatmaps and graphical representations of stock prices.
- 📊 **Performance Metrics**: Includes MSE, MAE, and R-squared scores for model comparison.


## 🔍 Conclusion
Among the models tested, **Linear Regression** performed better compared to others based on evaluation metrics.

