import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import skew, kurtosis

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(page_title="Distribution Guessing Game", layout="centered")

st.title("Statistics Distribution Guessing Game")
st.write("Look at the histogram and guess the probability distribution.")

# -----------------------------
# Distribution generators
# -----------------------------
distributions = {

    "Normal": lambda: np.random.normal(0,1,1000),
    "Student-t": lambda: np.random.standard_t(5,1000),
    "Cauchy": lambda: np.random.standard_cauchy(1000),

    "Exponential": lambda: np.random.exponential(1,1000),
    "Gamma": lambda: np.random.gamma(2,2,1000),
    "Lognormal": lambda: np.random.lognormal(0,1,1000),
    "Weibull": lambda: np.random.weibull(1.5,1000),
    "Chi-Square": lambda: np.random.chisquare(4,1000),

    "Uniform": lambda: np.random.uniform(0,1,1000),
    "Beta": lambda: np.random.beta(2,5,1000),

    "Poisson": lambda: np.random.poisson(3,1000),
    "Binomial": lambda: np.random.binomial(10,0.5,1000),
    "Geometric": lambda: np.random.geometric(0.3,1000),
    "Negative Binomial": lambda: np.random.negative_binomial(5,0.5,1000),

    "Pareto": lambda: np.random.pareto(3,1000)+1,
    "Gumbel": lambda: np.random.gumbel(0,1,1000),

    "Rayleigh": lambda: np.random.rayleigh(1,1000),
    "Laplace": lambda: np.random.laplace(0,1,1000)
}

# -----------------------------
# Session state
# -----------------------------
if "data" not in st.session_state:
    dist = random.choice(list(distributions.keys()))
    st.session_state.data = distributions[dist]()
    st.session_state.answer = dist
    st.session_state.score = 0
    st.session_state.rounds = 1

# -----------------------------
# Plot histogram
# -----------------------------
fig, ax = plt.subplots()

ax.hist(st.session_state.data, bins=30, color="skyblue", edgecolor="black")
ax.set_title("Histogram")

st.pyplot(fig)

# -----------------------------
# Guess selection
# -----------------------------
guess = st.selectbox(
    "Select your guess:",
    list(distributions.keys())
)

# -----------------------------
# Buttons
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    submit = st.button("Submit Guess")

with col2:
    new_round = st.button("New Distribution")

with col3:
    show_stats = st.button("Show Statistics")

# -----------------------------
# Submit guess logic
# -----------------------------
if submit:

    if guess == st.session_state.answer:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Wrong! Correct answer: {st.session_state.answer}")

    st.write(f"Score: {st.session_state.score} / {st.session_state.rounds}")

# -----------------------------
# New round logic
# -----------------------------
if new_round:

    dist = random.choice(list(distributions.keys()))
    st.session_state.data = distributions[dist]()
    st.session_state.answer = dist
    st.session_state.rounds += 1

    st.rerun()

# -----------------------------
# Statistics hints
# -----------------------------
if show_stats:

    data = st.session_state.data

    st.subheader("Statistical Clues")

    st.write("Mean:", round(np.mean(data),4))
    st.write("Variance:", round(np.var(data),4))
    st.write("Skewness:", round(skew(data),4))
    st.write("Kurtosis:", round(kurtosis(data),4))