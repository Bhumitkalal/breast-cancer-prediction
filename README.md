# 🩺 Breast Cancer Prediction System

A Machine Learning web application that predicts whether a breast tumor is **Benign** or **Malignant** using the **K-Nearest Neighbors (KNN)** algorithm. The application is built with **Python**, **Scikit-learn**, and **Streamlit** to provide an interactive and user-friendly interface.

---

## 📖 Project Overview

This project uses the **Breast Cancer Wisconsin Dataset** to classify tumors based on **30 medical features**.

Users can enter the required feature values through a simple web interface, and the trained KNN model instantly predicts whether the tumor is:

- ✅ **Benign (Non-Cancerous)**
- ⚠️ **Malignant (Cancerous)**

The application also displays the prediction probability for both classes.

---

## 🚀 Features

- Interactive Streamlit web application
- Breast cancer prediction using K-Nearest Neighbors (KNN)
- StandardScaler for feature normalization
- Label Encoding for target labels
- Real-time prediction
- Prediction confidence (probability)
- Organized feature input using expandable sections
- Error handling for smooth user experience
- Clean and responsive interface

---

## 📊 Dataset Information

**Dataset Name:** Breast Cancer Wisconsin Dataset

**Total Features:** 30

**Target Variable:**

| Label | Meaning |
|-------|---------|
| B | Benign |
| M | Malignant |

---

## 🤖 Machine Learning Model

**Algorithm**

- K-Nearest Neighbors (KNN)

**Preprocessing**

- Removed unnecessary columns (`id`, `Unnamed: 32`)
- Label Encoding
- StandardScaler

**Train-Test Split**

- 80% Training
- 20% Testing

**Model Accuracy**

**96.49%**

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```text
breast-cancer-prediction/
│
├── app.py
├── Cancer_model.ipynb
├── Cancer_Data.csv
├── cancer_model.pkl
├── scaler.pkl
├── label.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💻 Installation

### Clone the repository

```bash
git clone https://github.com/Bhumitkalal/breast-cancer-prediction.git
```

### Go to the project folder

```bash
cd breast-cancer-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🖥️ Application Preview

### Home Page

> Add a screenshot of your application's home page here.

### Prediction Result

> Add a screenshot showing the prediction result here.

---

## 📈 Example Prediction

| Input | Output |
|-------|--------|
| Patient medical feature values | ✅ Benign (No Cancer Detected) |
| Patient medical feature values | ⚠️ Malignant (Cancer Detected) |

---

## 🎯 Future Improvements

- Deploy on Streamlit Community Cloud
- Add charts for prediction probabilities
- Improve UI with custom CSS
- Add model comparison (KNN vs Random Forest vs SVM)
- Allow CSV file upload for batch predictions

---

## 👨‍💻 Developer

**Bhumit Kalal**

Aspiring Data Analyst | Machine Learning Enthusiast

**GitHub**

https://github.com/Bhumitkalal

**LinkedIn**

https://www.linkedin.com/in/bhumitkalal

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is created for educational and portfolio purposes.
