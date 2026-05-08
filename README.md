# 🏥 Medical Appointment No-Show Prediction 

## 📌 Project Scope
This project aims to predict whether a patient will miss a scheduled medical appointment (No-show) using machine learning techniques applied to healthcare appointment data.

## 📊 Dataset Source
The dataset used is the **Medical Appointment No Shows** dataset from Kaggle.

Main file:
- KaggleV2-May-2016.csv

## ⚙️ Project Workflow
1. Data loading and inspection  
2. Data cleaning and preprocessing  
3. Feature engineering  
4. Exploratory Data Analysis (EDA)  
5. Model training  
6. Model evaluation  
7. Model comparison  

## 🤖 Models Used
- Logistic Regression  
- Balanced Logistic Regression  
- Random Forest  
- XGBoost  

## 📈 Key Findings
- The dataset is imbalanced  
- WaitingDays was the most influential feature  
- XGBoost achieved better recall for identifying no-show patients  

## How to Run the Project

1. Clone the repository:
   git clone git clone https://github.com/zeenah-bio/medical-appointment-no-show-prediction.git

2. Install dependencies:
   pip install -r requirements.txt

3. Open the notebook:
   Run NoShow_Project.ipynb using Google Colab or Jupyter Notebook.

4. Make sure the dataset is placed inside the data/ folder.

---

# 🤖 Interactive AI Dashboard

An interactive Streamlit dashboard was developed to demonstrate the trained XGBoost model in a more practical clinical setting.

### Dashboard Features
- Real-time no-show risk prediction
- Interactive patient input controls
- AI-based probability estimation
- Clinical interpretation and suggested actions
- Modern healthcare-inspired interface

### Run Locally

```bash
streamlit run app.py
```

### Required Packages

```bash
pip install -r requirements.txt
```

## 📁 Repository Contents
- NoShow_Project.ipynb → Full ML pipeline  
- KaggleV2-May-2016.csv → Dataset  
- requirements.txt → Dependencies

- 

## 🔄 Note
This repository is continuously updated based on feedback and improvements.
