# 🩺 Breast Cancer Prediction System

A Machine Learning web application that predicts whether a breast tumor is **Benign** or **Malignant** using the **K-Nearest Neighbors (KNN)** algorithm. The application is built using **Python**, **Scikit-learn**, and **Streamlit** to provide an interactive and user-friendly interface.

---

## 🌐 Live Demo

🚀 **Try the application here:**

**Live App:** https://bhumit-breast-cancer-prediction.streamlit.app/

---

## 📂 GitHub Repository

**Source Code:** https://github.com/BhumitKalal/breast-cancer-prediction

---

## 📖 Project Overview

This project uses the **Breast Cancer Wisconsin Dataset** to classify breast tumors based on **30 medical features**.

Users can enter the required medical measurements through a simple web interface, and the trained KNN model instantly predicts whether the tumor is:

- ✅ **Benign (Non-Cancerous)**
- ⚠️ **Malignant (Cancerous)**

The application also displays prediction probabilities for both classes.

> **Disclaimer:** This project is developed for educational and portfolio purposes only and should not be used as a substitute for professional medical diagnosis.

---

## 🚀 Features

- Interactive Streamlit Web Application
- Breast Cancer Prediction using K-Nearest Neighbors (KNN)
- StandardScaler for Feature Scaling
- Label Encoding for Target Variable
- Real-time Prediction
- Prediction Probability
- Organized Input Sections (Mean, SE & Worst Features)
- Responsive User Interface
- Error Handling
- Live Deployment using Streamlit Community Cloud

---

## 📊 Dataset Information

**Dataset:** Breast Cancer Wisconsin Dataset

**Number of Features:** 30

**Target Variable**

| Label | Meaning |
|--------|---------|
| B | Benign |
| M | Malignant |

---

## 🤖 Machine Learning Model

### Algorithm

- K-Nearest Neighbors (KNN)

### Data Preprocessing

- Removed unnecessary columns (`id`, `Unnamed: 32`)
- Label Encoding
- StandardScaler

### Train-Test Split

- 80% Training
- 20% Testing

### Model Accuracy

**96.49%**

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Seaborn
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
git clone https://github.com/BhumitKalal/breast-cancer-prediction.git
```

### Navigate to the project directory

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

> *(Screenshots will be added soon.)*

---

## 📈 Example Prediction

| Input | Prediction |
|--------|------------|
| Patient Medical Features | ✅ Benign (No Cancer Detected) |
| Patient Medical Features | ⚠️ Malignant (Cancer Detected) |

---

## 🎯 Future Improvements

- Compare KNN with Random Forest and SVM
- Add feature importance visualization
- Upload CSV file for batch prediction
- Improve UI with custom CSS
- Add prediction history

---

## 👨‍💻 Developer

**Bhumit Kalal**

Aspiring Data Analyst | Machine Learning Enthusiast

**GitHub**

https://github.com/BhumitKalal

**LinkedIn**

https://www.linkedin.com/in/bhumitkalal/

---

## ⭐ Support

If you found this project useful, please consider giving this repository a ⭐ on GitHub.

---

## 📜 License

This project is created for educational and portfolio purposes.
