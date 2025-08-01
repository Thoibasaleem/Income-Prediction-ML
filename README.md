# 💸 Incometer: Income Prediction Tool

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-brightgreen)
![Machine Learning](https://img.shields.io/badge/Model-Gradient%20Boosting-orange)

Predict whether a person earns **more than \$50K per year** based on demographic and employment data, using multiple classification algorithms trained on the **UCI Adult Income dataset**.

---

## 🔥 Project Highlights

- Built as part of my **AI/ML Internship Project at ICT Academy**
- Complete pipeline: **Data Cleaning → EDA → Model Training → Evaluation → Deployment**
- Integrated **Streamlit UI** for real-time predictions

---

## 🚀 Live Demo
[**Try the App Here →**](https://income-prediction-ml-jqdcoaxciev89y6h6t22o7.streamlit.app/)

---

## 🖼 Preview

![Screenshot](https://github.com/user-attachments/assets/0531032c-7709-4d1e-b1c2-0117589712e1)


---

## 🔧 Tools & Libraries

- **Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost  
- **Deployment**: Streamlit  
- **Platform**: Google Colab (for training) + Local/Cloud (for deployment)

---

## 🤖 Machine Learning Models Used

| Model                  | Notes                             |
|------------------------|-----------------------------------|
| Logistic Regression    | Baseline classifier               |
| k-Nearest Neighbors    | Distance-based                     |
| Support Vector Machine | Kernel trick for non-linearity     |
| Decision Tree          | Easy to interpret                  |
| Random Forest          | Ensemble of trees                  |
| Gradient Boosting      | Boosted sequential learning        |
| **XGBoost**            | Extreme boosting, regularized      |

---

## 🏆 Best Performing Model

| Metric        | Value     |
|---------------|-----------|
| **Model**     | Gradient Boosting |
| **Accuracy**  | 83.8%     |
| **Precision** | 0.83      |
| **Recall**    | 0.84      |
| **F1-Score**  | 0.83      |

✅ Gradient Boosting achieved the best balanced performance, making it ideal for income prediction tasks.

---

📊 Dataset Info
Source: UCI Adult Census Income Dataset
Features: Age, Workclass, Education, Marital Status, Occupation, Hours per Week, etc.
Target: Income > 50K or ≤ 50K

##  Key Steps in Notebook

1. **Data Cleaning**: Missing values, whitespace removal in categorical features  
2. **EDA**: Visualized distributions, correlations (e.g., income vs. education)  
3. **Feature Encoding**: Label Encoding & One-Hot Encoding for categorical data  
4. **Feature Scaling**: Standardized numerical features  
5. **Model Training**: Tested 7+ algorithms  
6. **Evaluation**: Confusion matrix, precision/recall, F1-score

---

## 📁 Repository Structure

Income-Prediction-ML/
│
├── app.py # Streamlit web app
├── income_pipeline.pkl # Trained pipeline (preprocessing + model)
├── requirements.txt # Dependencies
├── Income_Prediction_ML.ipynb # Notebook (EDA + model training)
└── README.md # Project documentation


---

## 🏗 How to Run Locally

### Run Notebook (Model Training)
- Open `Income_Prediction_ML.ipynb` in **Google Colab**
- Execute step-by-step for:
  - Data loading
  - Preprocessing
  - Model training & evaluation

### Run Streamlit UI (Prediction)
# Clone repo
git clone https://github.com/Thoibasaleem/Income-Prediction-ML.git
cd Income-Prediction-ML

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
##  Real-World Application

#This project mimics real-world binary classification problems such as:
- Credit risk prediction
- Loan approval systems
- Customer segmentation

## 📇 Connect With Me

- 💼 [LinkedIn](https://www.linkedin.com/in/thoiba-saleem/)
- 📬 Email: thoibasaleem389@gmail.com
- 💻 GitHub: [ThoibaSaleem](https://github.com/ThoibaSaleem)
