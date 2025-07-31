import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Visualization")

# Sample visualization
st.subheader("Calories Burnt by Duration")
durations = [0.5, 1, 1.5, 2]
calories = [150, 300, 450, 600]

plt.plot(durations, calories, marker='o')
plt.xlabel("Exercise Duration (hrs)")
plt.ylabel("Estimated Calories")
st.pyplot(plt)
