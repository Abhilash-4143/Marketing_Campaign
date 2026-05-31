# Marketing Campaign Data Cleaning & Preprocessing

## Project Overview

This project focuses on **data cleaning and preprocessing** of the **Customer Personality Analysis (Marketing Campaign)** dataset using **Python, Pandas, and NumPy**.

The objective is to transform a raw marketing dataset into a clean, structured, and analysis-ready dataset by handling missing values, duplicates, inconsistent formats, outliers, and data type issues.

---

## Dataset

**Dataset:** Customer Personality Analysis – Marketing Campaign Dataset

The dataset contains customer demographic information, purchasing behavior, campaign responses, and spending patterns.

---

## Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**

---

## Data Cleaning & Preprocessing Steps

### 1. Dataset Loading

* Loaded dataset using `pandas.read_csv()`
* Used tab separator (`sep="\t"`)

### 2. Column Standardization

* Converted column names to lowercase
* Removed extra spaces
* Replaced special characters with underscores

### 3. Duplicate Handling

* Removed duplicate rows
* Removed duplicate customer IDs while keeping the first occurrence

### 4. Date Formatting

* Converted `dt_customer` column into datetime format
* Standardized output format to **dd-mm-yyyy**

### 5. Data Quality Improvements

* Removed unrealistic birth years (<1940)
* Created a new **age** feature from customer registration year and birth year

### 6. Categorical Data Cleaning

Standardized **marital status** categories:

* Married / Together → Partner
* Single / Divorced / Widow / Alone / Absurd / YOLO → Single

Standardized **education** values:

* Graduation → Graduate
* 2n Cycle → Master

### 7. Missing Values & Outlier Treatment

* Detected income outliers (>200000)
* Converted outliers to missing values
* Filled missing income values using the **median**

### 8. Feature Engineering

Created new features:

* **total_spend** → Sum of all spending categories
* **children** → Total children at home (`kidhome + teenhome`)

### 9. Column Removal

Dropped unnecessary columns:

* `z_costcontact`
* `z_revenue`

### 10. Data Type Correction

* Converted **age** → Integer
* Converted **income** → Float

---

## Output Files

After preprocessing, the project generates:

* `cleaned_marketing_campaign.csv` → Cleaned dataset
* `cleaning_summary.txt` → Summary of performed cleaning operations

---

## Project Structure

```bash
Marketing_Campaign/
│── marketing_campaign.csv
│── cleaned_marketing_campaign.csv
│── cleaning_summary.txt
│── data_cleaning.py
│── README.md
```

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Handling missing values
* Removing duplicate records
* Standardizing categorical data
* Managing outliers
* Working with datetime formats
* Feature engineering
* Preparing datasets for analysis and machine learning