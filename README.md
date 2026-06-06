### Live App Link : https://abhaybh025-real-estate-analytics-web-app.streamlit.app/

# 🏠 Gurgaon Real Estate Analytics Platform

An end-to-end Real Estate Analytics Platform built using Machine Learning, Data Analysis, and Streamlit.

This application helps users analyze the Gurgaon real estate market through interactive visualizations, property price prediction, market insights, and intelligent property recommendations.

---

## 🚀 Features

### 📈 Property Price Prediction

Predict property prices using multiple property attributes including:

- Sector / Location
- Property Type
- Built-up Area
- Bedrooms
- Bathrooms
- Luxury Category
- Floor Category
- Additional Property Features

---

### 📊 Real Estate Analytics Dashboard

Explore the Gurgaon real estate market through:

- Sector-wise Price Analysis
- Price per Sq. Ft. Analysis
- Interactive Geospatial Maps
- Property Distribution Analysis
- Feature Word Clouds
- Area vs Price Comparisons
- BHK-wise Price Distribution

---

### 🏡 Property Recommendation System

Discover properties similar to a selected property using a content-based recommendation engine powered by cosine similarity.

The recommendation engine considers:

- Location Similarity
- Amenities Similarity
- Property Characteristics

to provide personalized recommendations.

---

### 📍 Location-Based Search

Find properties within a specified radius of important locations and landmarks.

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Data Analysis & Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn

### Data Visualization

- Plotly
- Matplotlib
- Seaborn
- WordCloud

### Web Application

- Streamlit

---

## 📂 Project Structure

```text
real_estate_project/
│
├── app.py
│
├── pages/
│   ├── analytics.py
│   ├── prediction.py
│   └── recommendation.py
│
├── data/
│   └── data_viz1.csv
│
├── models/
│   ├── model.pkl
│   ├── feature_text.pkl
│   ├── location_distance.pkl
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   └── cosine_sim3.pkl
│
├── requirements.txt
│
└── README.md
```

---

## 🧠 Machine Learning Workflow

### Data Preprocessing

- Missing Value Handling
- Data Cleaning
- Feature Engineering
- Categorical Encoding
- Feature Scaling

### Price Prediction

A machine learning model is trained on Gurgaon real estate data to predict property prices based on property characteristics.

### Recommendation Engine

The recommendation system uses weighted cosine similarity matrices to identify properties with similar characteristics.

Combined Similarity Score:

```python
0.5 * Location Similarity
+ 0.8 * Amenities Similarity
+ 1.0 * Property Characteristics Similarity
```

The system then returns the top most similar properties.

---

## 📸 Application Modules

### 🏠 Home Page

Overview of the platform and its functionalities.

### 📈 Price Prediction

Estimate property prices using property details.

### 📊 Analytics Dashboard

Analyze market trends through interactive charts and visualizations.

### 🏡 Recommendation System

Find similar properties and search nearby properties within a specified radius.

---

## 📈 Business Value

This platform can help:

- Property Buyers
- Real Estate Investors
- Real Estate Consultants
- Market Analysts

make data-driven real estate decisions.

---

## 🔮 Future Improvements

- Docker Integration
- Model Versioning
- MLflow Tracking
- CI/CD Pipelines
- Cloud Deployment
- Advanced Recommendation Systems
- Real-Time Data Integration

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/real-estate-analytics.git
```

Navigate to the project directory:

```bash
cd real-estate-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```
---

## 📷 Screenshots

