import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pathlib

st.set_page_config(page_title="Real Estate Analytics", layout="wide")

st.title('📊 Real Estate Analytics Dashboard')


# Load Data
current_dir = pathlib.Path(__file__).parent.resolve()
project_root = current_dir.parent.parent.resolve()

data_viz_path = project_root/ 'data_viz1.csv'
feature_text_path = project_root / 'models' / 'feature_text.pkl'

new_df = pd.read_csv(data_viz_path)

with open(feature_text_path, 'rb') as f:
    feature_text = pickle.load(f)


# Sector Price Per Sqft Map
st.header('📍 Sector Price per Sqft Geomap')

group_df = new_df.groupby('sector').mean(numeric_only=True)[
    ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
]

fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    hover_name=group_df.index,
    width=1200,
    height=700
)

st.plotly_chart(fig, use_container_width=True)


# Word Cloud
st.header('☁️ Property Features Word Cloud')

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='black',
    stopwords={'s'},
    min_font_size=10
).generate(feature_text)

fig_wc, ax_wc = plt.subplots(figsize=(8, 8))

ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis("off")

plt.tight_layout()

st.pyplot(fig_wc)


# Area vs Price
st.header('🏠 Area vs Price')

property_type = st.selectbox(
    'Select Property Type',
    ['flat', 'house']
)

filtered_df = new_df[new_df['property_type'] == property_type]

fig1 = px.scatter(
    filtered_df,
    x="built_up_area",
    y="price",
    color="bedRoom",
    title=f"Area vs Price ({property_type.title()})"
)

st.plotly_chart(fig1, use_container_width=True)


# BHK Pie Chart
st.header('🥧 BHK Distribution')

sector_options = sorted(new_df['sector'].dropna().unique().tolist())
sector_options.insert(0, 'overall')

selected_sector = st.selectbox(
    'Select Sector',
    sector_options
)

if selected_sector == 'overall':
    pie_df = new_df
else:
    pie_df = new_df[new_df['sector'] == selected_sector]

fig2 = px.pie(
    pie_df,
    names='bedRoom',
    title=f'BHK Distribution - {selected_sector.title()}'
)

st.plotly_chart(fig2, use_container_width=True)


# BHK Price Comparison
st.header('📦 BHK Price Comparison')

fig3 = px.box(
    new_df[new_df['bedRoom'] <= 4],
    x='bedRoom',
    y='price',
    title='BHK Price Range'
)

st.plotly_chart(fig3, use_container_width=True)


# Price Distribution by Property Type
st.header('📈 Property Price Distribution')

fig4, ax4 = plt.subplots(figsize=(10, 5))

sns.kdeplot(
    data=new_df[new_df['property_type'] == 'house'],
    x='price',
    label='House',
    fill=True,
    ax=ax4
)

sns.kdeplot(
    data=new_df[new_df['property_type'] == 'flat'],
    x='price',
    label='Flat',
    fill=True,
    ax=ax4
)

ax4.set_title('Price Distribution by Property Type')
ax4.set_xlabel('Price')
ax4.legend()

st.pyplot(fig4)