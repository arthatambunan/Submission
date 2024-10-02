import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from matplotlib.gridspec import GridSpec

# Set the style for Seaborn plots
sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/arthatambunan/Submission/refs/heads/main/dasboard/day_data.csv")

# Set page configuration for Streamlit
st.set_page_config(page_title="BIKERS",
                   page_icon="🚴‍♂️",
                   layout="wide")
st.markdown("---")

# Title and Subheaders for the Dashboard
st.title("Bike Sharing Analysis")
st.markdown("---")
st.subheader("Dataset Jumlah Penyewa Sepeda")

# Display DataFrame in Streamlit
st.dataframe(day_df.head())

# Visualisasi penyewa sepeda berdasarkan "Season"
st.subheader("Jumlah Penyewa Berdasarkan Musim")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=day_df, hue='season', palette="Set2", ax=ax1)
ax1.set_xlabel("Musim", fontsize=12)
ax1.set_ylabel("Jumlah Penyewa", fontsize=12)
ax1.set_title("Perbandingan Penyewa Berdasarkan Musim", fontsize=15)
st.pyplot(fig1)

# Visualisasi penyewa sepeda berdasarkan "workingday"
st.subheader("Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=day_df, estimator=sum, palette='Set2', ax=ax2)
ax2.set_title('Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur', fontsize=16)
ax2.set_xlabel('Hari Libur vs Hari Kerja', fontsize=12)
ax2.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
ax2.ticklabel_format(style='plain', axis='y')
st.pyplot(fig2)

# Section for Conclusion
st.subheader("Kesimpulan")
st.write("""
1. Dari Visualisasi data, dapat dilihat bahwa musim berpengaruh pada jumlah peminjam sepeda. Jumlah peminjaman sepeda paling banyak pada Fall Season (musim gugur) disusul dengan Winter Season, Summer Season, Springer Season.
2. Dari visualisasi data tersebut dapat dilihat bahwa jumlah peminjaman sepeda lebih banyak saat hari kerja daripada hari libur.
""")
st.caption('Copyright (c), created by Juni Artha Tambunan')

