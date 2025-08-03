# Project8
This project analyzes the information of trips (trips amount,company name, date of starting and ending trips) performed by a taxi service. The information is in 3 different datasets. Visualizations and hypotheses tests are performed.

**Objective:** To clean data and create data (from the cleaned one) to perform hypotheses tests (Levene and T tests) to make decisive decisions.

## Overview
First, the exploratory data analysis (EDA) is performed to show the data in the non-cleaned datasets. Second, the data preprocessing is made, which consist of filling null values, dropping duplicates, verifying if data format is correct and processing the outliers. Third, to create data from the previously cleaned one. Fourth, the formal Levene and T tests are performed to determine if the following hypothesis is true:

• Average trip duration in raining saturdays != Average trip duration in non-raining saturdays.

Finally, some decisive conclusions are given.

🛠️**Libraries used**: Pandas, Matplotlib, NumPy, SciPy.

The Jupyter Notebook is in scripts/project8.ipynb.

## 🚀 Installation
1. Clone this repository:
```
git clone https://github.com/arteaga7/Project8.git
```
2. Set virtual environment and install dependencies:
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
3. Run Jupyter Notebook in scripts/project8.ipynb.