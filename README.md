
---

## ⚙️ **README — Predictive Maintenance for Electric Vehicles**

```markdown
# 🧠 Predictive Maintenance for Electric Vehicles

A machine learning-based Streamlit dashboard that predicts **potential EV component failures** before they occur.  
It analyzes sensor data such as motor temperature, controller temperature, voltage, and vibration levels to classify vehicle health.

---

## 📊 Overview
The project aims to reduce **maintenance costs and downtime** by predicting component failures early.  
The model identifies risky patterns in sensor readings and alerts users when the EV system shows potential failure indicators.

---

## 🧠 Features
- Predict whether an EV system requires maintenance using classification model  
- Interactive web UI built with Streamlit  
- Visual insights through boxplots and analytics charts  
- Synthetic data simulation of real-world EV sensors  

---

## 🧩 Tech Stack
- **Python 3.9+**
- **Libraries:** Pandas, NumPy, Scikit-learn, Streamlit, Seaborn, Matplotlib, Joblib
- **Model:** Random Forest Classifier

---


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/predictive-maintenance-ev.git
cd predictive-maintenance-ev
pip install -r requirements.txt
python generate_data.py
python train_model.py
streamlit run app.py
```


## 📁 Folder Structure
