# 🛍️ Customer Segmentation Project README 📊

---

## **🔍 Overview**

This project uses **K-means clustering** to group customers based on their annual income and spending habits. The goal is to understand customer behavior and create different customer segments for targeted marketing.

---

## **📑 Dataset**

The dataset contains the following columns:
- **🆔 CustomerID**: Unique customer number.
- **👤 Gender**: Customer's gender (Male/Female).
- **🎂 Age**: Customer's age.
- **💵 Annual Income**: How much the customer earns per year (in thousands).
- **💳 Spending Score**: How much the customer spends, rated on a scale of 1-100.

---

## **🛠️ Steps**

### **1️⃣ Data Preprocessing**
- The dataset is cleaned and the gender is converted into numbers (Male = 0, Female = 1).
- We use **Annual Income** and **Spending Score** to group customers.

### **2️⃣ Finding the Number of Clusters**
- We use the **Elbow Method** 📐 to find the best number of groups (clusters). A graph 📊 is plotted to show how the grouping works as the number of clusters changes.

### **3️⃣ Training the Model**
- We use **K-means clustering** 🧠 to split customers into 5 different groups.

### **4️⃣ Visualization**
- The customer groups are plotted in a 2D chart with different colors 🎨 for each group. The central points (centroids) ⚫ of each group are also shown.

---

## **✨ Key Features**
- **🔄 K-Means Clustering**: Groups customers into 5 categories based on their income and spending score.
- **📉 Elbow Method**: Helps decide the number of groups to create by showing the change in clustering efficiency.
- **📊 Cluster Visualization**: A simple 2D graph shows how customers are grouped.

---

## **🎯 Conclusion**

This project demonstrates how to group customers based on their income and spending habits, helping businesses create personalized marketing strategies. The visualizations make it easy to understand customer segments. To increase spending among low-income customers, businesses can use strategies like personalized discounts, flexible payment plans (e.g., "buy now, pay later"), redeemable points, coupons, bundled offers(1+1 offer), and seasonal promotions during peak periods like holidays or back-to-school seasons.




