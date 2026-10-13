# Eroski Retail: Implicit Recommendation Engine & Behavioral Segmentation

## Project Overview
This repository contains a Machine Learning pipeline developed to solve a retail recommendation and customer segmentation challenge using anonymized transaction data from Eroski (over 47,000 users, 2,936 products, and 5M interaction rows). Instead of relying on generic promotional campaigns, I built a data-driven personalization system designed to target cross-selling mathematically.

*Note: The raw datasets (`matriz.csv`, `tickets_dni.csv`, etc.) exceed GitHub's file size limits due to the volume of transactions (5M+ rows) and are stored locally. The notebooks demonstrate the end-to-end processing and modeling.*

## Tech Stack & Libraries
* Language: Python
* Data Processing: Pandas, NumPy, SciPy (Sparse Matrices)
* Machine Learning & Modeling:
  * implicit library (Alternating Least Squares - ALS algorithm)
  * Scikit-learn (PCA for dimensionality reduction, K-Means & DBSCAN clustering, StandardScaler)
  * Surprise (SVD baseline evaluation)
* Interactive Dashboard: Plotly, Dash

## Methodology & Technical Pipeline

### 1. Data Engineering & Preprocessing
* Handled massive tabular datasets by leveraging sparse matrix representations to optimize memory usage and processing speed.
* Implemented cryptographic hashing (SHA-256) to strictly anonymize customer DNI data while maintaining relational integrity across tickets.

### 2. Recommendation Engine: Implicit Collaborative Filtering
Retail transaction data represents implicit feedback (purchases made, not explicit ratings), which invalidates standard collaborative filtering methods. 
* I implemented ALS (Alternating Least Squares) optimized for sparse matrices using the implicit library.
* Validated the recommendation pipeline against a test set, evaluating model accuracy and tuning latent factors. ALS outperformed standard SVD in ranking metrics for sparse retail matrices.

### 3. Customer Behavior Segmentation
To design targeted marketing strategies without getting skewed by data noise:
* Filtered out the top ubiquitous products to find true behavioral variance among customers.
* Extracted latent user and item factors from the ALS model, scaled the features, and applied PCA retaining 95% of the variance.
* Executed K-Means and DBSCAN clustering (validated via Silhouette Score and elbow method) to isolate distinct behavioral cohorts and product groupings.

## Interactive Analytical Dashboard
A web application built using Plotly and Dash designed to visualize:
* Monthly sales trends and transaction volume peaks.
* Top traffic-driving products in the catalog.
* Cluster distribution and behavioral breakdowns.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone [https://github.com/ekaingutierrez/eroski-recommendation-engine.git](https://github.com/ekaingutierrez/eroski-recommendation-engine.git)
