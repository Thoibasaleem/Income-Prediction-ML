# 💸 Income Prediction Using Machine Learning

This project predicts whether a person earns more than $50K per year based on demographic and employment data, using various classification algorithms trained on the UCI Adult Income dataset.

Built as part of my **AI/ML internship project** at ICT Academy, this notebook showcases my end-to-end understanding of the ML pipeline — from preprocessing to model tuning and evaluation.

---

## 🔧 Tools & Libraries

- **Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost  
- **Platform**: Google Colab (Jupyter Notebook)

---

## 🤖 Machine Learning Models Used

| Model | Notes |
|-------|-------|
| Logistic Regression | Baseline classifier |
| k-Nearest Neighbors (kNN) | Distance-based |
| Support Vector Machine (SVM) | Kernel trick for non-linearity |
| Decision Tree | Tree-based, easy to interpret |
| Random Forest | Ensemble of trees |
| Gradient Boosting | Boosted sequential learning |
| **XGBoost** | Extreme boosting, regularized |

---

## 🏆 Best Performing Model

| Metric        | Value     |
|---------------|-----------|
| **Model**     | Gradient Boosting |
| **Accuracy**  | 83.8%     |
| **Precision** | 0.83      |
| **Recall**    | 0.84      |
| **F1-Score**  | 0.83      |

✅ Gradient Boosting outperformed other models based on balanced precision and recall, making it ideal for real-world income prediction tasks.

---

##  Key Steps

1. **Data Cleaning**: Handled missing values & whitespace in categorical fields  
2. **EDA**: Visualized distributions, correlations (e.g., income vs. education)  
3. **Feature Encoding**: Used Label Encoding & One-Hot Encoding  
4. **Feature Scaling**: Standardized numerical features  
5. **Model Training**: Trained & tuned 7+ classification algorithms  
6. **Evaluation**: Compared metrics using confusion matrix & cross-validation

---

## 📁 How to Run

> Open `income_prediction_ML.ipynb` in Google Colab  
> Run each cell step-by-step to see:
- Dataset loading
- Preprocessing
- Model training
- Evaluation & results

📌 No installation needed — runs entirely in Colab.

---

## 📊 Dataset Info

- **Source**: UCI Adult Census Income Dataset  
- **Features**: Age, Workclass, Education, Marital Status, Occupation, Hours per Week, etc.  
- **Target**: Income > 50K or ≤ 50K

---

##  Real-World Application

This project mimics real-world binary classification problems such as:
- Credit risk prediction
- Loan approval systems
- Customer segmentation

---



 
- ## 📇 Connect With Me

- 💼 [LinkedIn](https://www.linkedin.com/in/thoiba-saleem/)
- 📬 Email: thoibasaleem389@gmail.com
- 💻 GitHub: [ThoibaSaleem](https://github.com/ThoibaSaleem)
