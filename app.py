import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page setup
st.set_page_config(page_title="students_social_media_addiction", layout="wide")

# Title and description
st.title("📱 students_social_media_addiction Dashboard")
st.markdown("""
Welcome! This app visualizes students’ social media usage, sleep patterns, and addiction scores using interactive charts.
""")

# Load the dataset
st.subheader("📂 Load Dataset")
file_path = "students_social_media_addiction.csv"
try:
    df = pd.read_csv(file_path)
    st.success(f"✅ Loaded '{file_path}' successfully!")
except FileNotFoundError:
    st.error(f"❌ Could not find the file '{file_path}'. Please make sure it's in the same folder as app.py.")
    st.stop()

# Show a preview
st.subheader("👀 Dataset Preview")
st.dataframe(df.head())

# Plot 1: Daily usage histogram
st.subheader("📊 Daily Social Media Usage (Hours)")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='Avg_Daily_Usage_Hours', bins=10, kde=True, ax=ax1)
ax1.set_title("Distribution of Daily Social Media Usage")
ax1.set_xlabel("Hours")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# Plot 2: Addiction Score by Gender
st.subheader("🧠 Addiction Score by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Gender', y='Addicted_Score', palette='Set2', ax=ax2)
ax2.set_title("Addiction Score by Gender")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Addiction Score")
st.pyplot(fig2)

# Plot 3: Sleep Hours vs. Addiction Score
st.subheader("💤 Sleep Hours vs. Addiction Score")
fig3, ax3 = plt.subplots()
sns.lineplot(data=df, x='Sleep_Hours_Per_Night', y='Addicted_Score', ax=ax3)
ax3.set_title("Sleep Hours vs. Addiction Score")
ax3.set_xlabel("Sleep Hours")
ax3.set_ylabel("Addiction Score")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("👩‍🎓 Created with ❤️ by Maria & Team | Reichman University 2025")
