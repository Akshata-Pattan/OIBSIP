# Customer Segmentation using K-Means Clustering

## Objective
This project aims to segment mall customers into distinct groups based on their **Annual Income** and **Spending Score** using the **K-Means Clustering** algorithm. Customer segmentation helps businesses understand customer behavior and develop targeted marketing strategies.

## Dataset
- **Dataset Name:** Mall Customers Dataset
- **Records:** 200
- **Features Used:**
  - CustomerID
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

## Project Workflow
1. Import required libraries.
2. Load the dataset.
3. Perform Exploratory Data Analysis (EDA).
4. Check dataset information and missing values.
5. Select Annual Income and Spending Score for clustering.
6. Standardize the selected features.
7. Use the Elbow Method to determine the optimal number of clusters.
8. Apply K-Means Clustering.
9. Visualize customer segments.
10. Interpret the clusters and provide business insights.

## Results
The Elbow Method indicated that **5 clusters** provide the optimal segmentation.

The identified customer groups are:

- **Cluster 0:** Medium Income – Medium Spending
- **Cluster 1:** High Income – High Spending
- **Cluster 2:** Low Income – High Spending
- **Cluster 3:** High Income – Low Spending
- **Cluster 4:** Low Income – Low Spending

## Business Insights
- High-income & high-spending customers are premium customers and should receive loyalty rewards.
- High-income but low-spending customers can be targeted with personalized offers.
- Low-income but high-spending customers respond well to attractive promotions.
- Medium-income customers contribute to stable revenue.
- Low-income & low-spending customers require budget-friendly marketing strategies.

## Conclusion
Customer segmentation using K-Means successfully grouped customers into five meaningful clusters. These insights can help businesses improve customer targeting, increase sales, and design effective marketing campaigns.

## Repository Structure

```
DataAnalytics-L1-Task2-CustomerSegmentation/
│── Customer_Segmentation_Analysis.ipynb
│── Mall_Customers.csv
│── README.md
```

## Author

**Akshata Pattan**
