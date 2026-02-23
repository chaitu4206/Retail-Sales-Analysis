# 🛒 Retail Sales Data Analysis

## 📌 Project Overview

This project focuses on analyzing retail transaction data to uncover meaningful insights about sales performance, customer behavior, and product trends. The analysis is performed using Python libraries such as Pandas and Matplotlib.

The dataset contains over 10,000 transaction records with information about customers, products, and sales.

---

## 🎯 Objectives

* Clean and preprocess raw retail data
* Perform exploratory data analysis (EDA)
* Analyze sales trends and customer behavior
* Visualize insights using charts
* Derive actionable business insights

---

## 🗂 Dataset Description

The dataset contains the following columns:

* Transaction ID
* Date
* Customer ID
* Gender
* Age
* Product Category
* Quantity
* Price per Unit
* Total Amount

---

## 🧹 Data Cleaning

Performed using **Pandas**:

* Removed missing values
* Dropped duplicate records
* Converted date column to datetime format
* Checked and corrected data inconsistencies

---

## 📊 Exploratory Data Analysis

### 1. Sales Analysis

* Monthly sales trends
* Category-wise revenue
* Total sales distribution

### 2. Customer Analysis

* Gender-wise spending patterns
* Age group segmentation
* High-value customers

### 3. Trend Analysis

* Seasonal sales patterns
* Peak revenue months

---

## 📈 Visualizations

The project includes the following charts:

* Monthly Sales Trend
* Category-wise Sales
* Gender-wise Sales
* Age Group Sales

All visualizations are saved in the **outputs/** folder.

---

## 🧠 Key Business Insights

* Sales show seasonal variation with peaks in certain months
* Electronics is the top-performing category
* Age group 45–60 contributes the highest revenue
* Female customers tend to spend more
* A small group of customers contributes significantly to total revenue
* Some product categories have low performance and require marketing focus

---

## 🛠 Tech Stack

* Python
* Pandas
* Matplotlib
* NumPy
* Microsoft Excel (optional)

---

## 📁 Project Structure

```
Retail-Sales-Analysis/
│
├── data/
│   ├── retail_sales.csv
│   └── cleaned_retail_sales.csv
│
├── src/
│   ├── data_cleaning.py
│   └── analysis.py
│
├── outputs/
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── gender_sales.png
│   └── age_sales.png
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run data cleaning

```
python src/data_cleaning.py
```

### 4. Run analysis

```
python src/analysis.py
```

---

## 📌 Future Improvements

* Build an interactive dashboard using Streamlit
* Add machine learning for sales prediction
* Deploy the project as a web application
* Integrate SQL for data storage

---
⭐ If you like this project, don't forget to give it a star!
