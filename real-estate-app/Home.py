import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Gurgaon Real Estate Analytics Platform")

st.markdown("""
### Smart Property Analysis and Price Prediction

This platform helps users analyze the Gurgaon real estate market using
Machine Learning, Data Analytics, and Property Recommendation Systems.

Use the sidebar to explore different modules of the application.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 📈 Price Prediction
    
    Predict property prices using a trained Machine Learning model using multiple property attributes including:
    - Location & Sector
    - Property Type
    - Built-up Area
    - Bedrooms & Bathrooms
    - Amenities
    - Luxury Features
    - Additional Property Characteristics
    """)

with col2:
    st.success("""
    ### 🔍 Market Insights
    
    Explore:
    - Price Trends
    - Sector-wise Analysis
    - Property Distributions
    - Market Statistics
    """)

with col3:
    st.warning("""
    ### 🏡 Property Recommendations
    
    Discover similar properties based on:
    - Budget
    - Location
    - Features
    - Property Characteristics
    """)

st.divider()

st.subheader("🚀 Project Highlights")

st.markdown("""
✅ End-to-End Machine Learning Pipeline

✅ Interactive Data Visualizations

✅ Property Recommendation Engine

✅ Real Estate Market Analytics

✅ Streamlit Multi-Page Application

✅ Built using Python, Pandas, Scikit-Learn, Plotly, and Streamlit
""")

st.sidebar.success("Select a module from the sidebar.")