## ⚠️ **Disclaimer**

🚨 **Note**: The dataset is too large to upload directly. You can download the dataset from the following link:

🔗 [Click here to download](https://drive.google.com/file/d/1cCkwiVv4mgfl20ntgY3n4yApcWqqZQe6/view)



# 🎬 **Content-Based Movie Recommendation System** 🎬

Welcome to the **Content-Based Movie Recommendation System**! This project is designed to suggest movies to users by analyzing movie attributes such as **genre**, **cast**, and **director** and comparing them with what the user has enjoyed before to provide personalized movie recommendations. he system uses **Machine Learning**,**Natural Language Processing (NLP)**


### 📋 **Key Features**:
- **Content-Based Filtering**: Recommends movies similar to the ones the user has liked based on attributes like **genre**, **cast**, and **director**.
- **TF-IDF Feature Extraction**: Converts textual movie descriptions (e.g., genre, cast) into numerical feature vectors.
- **Cosine Similarity**: Measures the similarity between two movies based on their feature vectors, providing ranked movie recommendations.

---

## 🔍 **Points to Note**:
- If the **target variable** is categorical (e.g., **0/1**, **yes/no**), or numerical, preprocessing is required.
- If the dataset contains **string-based features**, perform **feature extraction** (converting string data into numerical vectors).
- **Recommendation Types**:
  1. **Content-Based**: Analyzes similarities in attributes like **genre**, **cast**, and **director**.
  2. **Collaborative Filtering**: Based on user behavior and similar user preferences.
  3. **Popularity-Based**: Based on overall popularity and ratings of movies.
- **Key Focus**: The **genre** of the movie (e.g., action, thriller, romance, etc.) is a significant feature in this system.
  
**📝 Note**: This project is implemented using **Content-Based Filtering**.

---

## 🏗️ **Model Development Process**

1. **Importing Libraries**: Use **Pandas**, **NumPy**, **Scikit-learn (TF-IDF, Cosine Similarity)**.
2. **Loading Dataset**: Load the movie dataset using Pandas.
3. **Feature Selection**: Focus on 5 main features: **genre**, **title**, **keywords**, **cast**, and **director**.
4. **Preprocessing**: Replace missing values with empty strings.
5. **Feature Extraction**: Convert textual data into numerical vectors using **TF-IDF** **(ohter ways - count vectorization(Bag of Words),Word Embeddings-word2vec,Glove,FastText)**
6. **Cosine Similarity**: Calculate similarity between movies based on their feature vectors.
7. **User Input**: Accept the movie name as input from the user.
8. **Movie Existence Check**: Ensure the movie is in the dataset and find its index.
9. **Calculate Similarity Scores**: Find the similarity between the input movie and all other movies.
10. **Recommendations**: Return the top 10 most similar movies.


## 🛠️ **Errors and Solutions**

### ⚠️ **Error 1**: Extra Columns (1264 columns instead of 24)
- **Problem**: The dataset contains 1264 columns instead of the expected 24.
- **Solution**: Filter out unnamed columns using the following command:
  
    ```python
    df.loc[:, ~df.columns.str.contains('^Unnamed')]
    ```
    This will drop the unnamed columns and keep the original 24.

---

### ⚠️ **Error 2**: `float has no len()`
- **Cause**: NaN values were not fully removed after preprocessing.
- **Solution**: Drop the columns that contain NaN values:

    ```python
    df.dropna(axis=1, inplace=True)
    ```

---

### ⚠️ **Error 3**: Cosine Similarity Error (Direct Movie Name Lookup)
- **Problem**: Cosine similarity can only be calculated between feature vectors, not movie names directly.
- **Solution**: Ensure proper feature extraction is performed before calculating cosine similarity.

---

## 🔄 **Improvements Made**

- The system now accounts for variations in user input:
  - **Input**: `"iron man"`
    - **Output**: `"Iron Man"`, `"Iron Man 2"`, `"Iron Man 3"`, `"Avengers"`, etc.
  - **Input**: `"ironman"` (without space)
    - **Output**: Correct set of movies, including the entire **Iron Man** series.

---

## 👀**Must Watch It - **
🔗 [Click here](https://youtu.be/n3RKsY2H-NE?si=b9jl3DnNX-Q3QpkC)

---

## 🌟 **Future Improvements**

- **Frontend Deployment**: Connect the recommendation model to a user-friendly interface to enhance usability.
- **Improved UI/UX**: Add colors, emojis, and a professional design to make the system more engaging and interactive for the user.
- **Enhanced Output**: Present the recommendations in an attractive, well-organized manner with professional formatting for readability and ease of use.




