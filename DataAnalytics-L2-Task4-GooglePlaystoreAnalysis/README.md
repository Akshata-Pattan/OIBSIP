# OIBSIP – Oasis Infobyte Internship

## Level 2 – Task 4: Google Play Store App Analytics

### 📌 Internship Task

As part of my **Oasis Infobyte Internship**, I completed Level 2 – Task 4, which focuses on analyzing Google Play Store applications and user reviews to extract meaningful insights related to app categories, ratings, installations, pricing, revenue, and user sentiment.

### 🎯 Objective

The objective of this task was to perform exploratory data analysis on Google Play Store app data and user reviews, identify important patterns, and present the findings through meaningful visualizations.

### 📂 Datasets Used

Two datasets were used for this analysis:

- **Google Play Store Apps Dataset** – Contains information about app categories, ratings, reviews, size, installs, price, content rating, genres, and other app details.
- **Google Play Store User Reviews Dataset** – Contains user reviews along with sentiment, sentiment polarity, and sentiment subjectivity.

### 🛠️ Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Google Colab

### 🔍 Data Preprocessing

The datasets were cleaned and prepared before analysis.

The preprocessing steps included:

- Handling missing values
- Removing duplicate records
- Converting numerical columns to appropriate data types
- Converting app size into numerical MB values
- Converting installs and prices into numerical values
- Preparing the user reviews dataset for sentiment analysis

After preprocessing:

- Apps Dataset: **10,346 records and 13 columns**
- User Reviews Dataset: **29,692 records and 5 columns**

### 📊 Analysis Performed

#### 1. App Category Analysis

Analyzed the distribution of applications across different categories to identify highly populated and competitive categories.

**Key Insight:**  
The **FAMILY** category had the highest number of apps, followed by **GAME** and **TOOLS**.

#### 2. Ratings Analysis

Analyzed the distribution of app ratings and calculated the average rating for each category.

**Key Insight:**  
Most apps had ratings concentrated between approximately **4.0 and 4.8**, indicating generally positive user ratings.

#### 3. Size and Installs Analysis

A scatter plot was used to examine the relationship between app size and the number of installs.

The calculated correlation was **0.1688**, indicating a **weak positive relationship** between app size and installs.

#### 4. Pricing Analysis

Analyzed free and paid applications, the price distribution of paid apps, and estimated revenue by category.

**Key Insights:**
- The majority of apps are free.
- Most paid apps are concentrated in the lower price range.
- The **FAMILY** category had the highest estimated revenue among the analyzed paid apps.

> Estimated revenue was calculated using listed app price × estimated installs. It represents potential gross revenue and may differ from actual revenue due to factors such as platform fees, taxes, refunds, and discounts.

#### 5. Sentiment Analysis

Analyzed user reviews to understand overall user sentiment.

The sentiment distribution was:

- **Positive:** 19,015 reviews
- **Negative:** 6,321 reviews
- **Neutral:** 4,356 reviews

Sentiment was also compared across app categories.

**Key Insight:**  
Positive sentiment was dominant across most categories, while categories such as **Games** and **Social** showed comparatively higher proportions of negative reviews.

### 📈 Visualizations

The project includes visualizations for:

- App distribution by category
- Rating distribution
- Average rating by category
- App size vs. installs
- Free vs. paid apps
- Paid app price distribution
- Estimated revenue by category
- Overall sentiment distribution
- Sentiment by app category
- Interactive sentiment analysis using **Plotly**

### 💡 Key Takeaways

This analysis demonstrates how exploratory data analysis and sentiment analysis can be used to understand the Google Play Store ecosystem.

The findings can help developers evaluate:

- Category competition
- User satisfaction
- Pricing strategies
- Potential revenue opportunities
- User sentiment and areas for improvement

### 📌 Internship Outcome

Through this task, I gained practical experience in:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization
- Correlation analysis
- Sentiment analysis
- Interactive visualization using Plotly
- Extracting business-oriented insights from real-world datasets

---

⭐ If you found this project useful, feel free to **star the repository**.
