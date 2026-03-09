import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import os
from scipy.stats import skew, kurtosis

st.set_page_config(page_title="Distribution Guessing Game", layout="centered")

st.title("Statistics Distribution Guessing Game")

# -----------------------------
# MODE
# -----------------------------

mode = st.sidebar.radio("Mode", ["Game Mode", "Explorer Mode"])

# -----------------------------
# DIFFICULTY
# -----------------------------

difficulty = st.sidebar.selectbox("Difficulty", ["Easy","Medium","Hard"])

if difficulty == "Easy":
    sample_size = 1000
elif difficulty == "Medium":
    sample_size = 300
else:
    sample_size = 80

# -----------------------------
# DISTRIBUTIONS
# -----------------------------

distribution_names = [

"Normal",
"Student-t",
"Cauchy",
"Exponential",
"Gamma",
"Uniform",
"Beta",
"Laplace",
"Lognormal",
"Weibull",
"Chi-Square",
"Pareto",
"Rayleigh",
"Gumbel",

"Poisson",
"Binomial",
"Geometric",
"Negative Binomial",
"Hypergeometric"

]

def generate_distribution(name,n):

    if name=="Normal":
        return np.random.normal(0,1,n)

    if name=="Student-t":
        return np.random.standard_t(5,n)

    if name=="Cauchy":
        return np.random.standard_cauchy(n)

    if name=="Exponential":
        return np.random.exponential(1,n)

    if name=="Gamma":
        return np.random.gamma(2,2,n)

    if name=="Uniform":
        return np.random.uniform(0,1,n)

    if name=="Beta":
        return np.random.beta(2,5,n)

    if name=="Laplace":
        return np.random.laplace(0,1,n)

    if name=="Lognormal":
        return np.random.lognormal(0,1,n)

    if name=="Weibull":
        return np.random.weibull(1.5,n)

    if name=="Chi-Square":
        return np.random.chisquare(4,n)

    if name=="Pareto":
        return np.random.pareto(3,n)+1

    if name=="Rayleigh":
        return np.random.rayleigh(1,n)

    if name=="Gumbel":
        return np.random.gumbel(0,1,n)

    if name=="Poisson":
        return np.random.poisson(3,n)

    if name=="Binomial":
        return np.random.binomial(10,0.5,n)

    if name=="Geometric":
        return np.random.geometric(0.3,n)

    if name=="Negative Binomial":
        return np.random.negative_binomial(5,0.5,n)

    if name=="Hypergeometric":
        return np.random.hypergeometric(7,13,5,n)


# -----------------------------
# EXPLORER MODE
# -----------------------------

if mode == "Explorer Mode":

    st.subheader("Distribution Explorer")

    dist = st.selectbox("Choose distribution", distribution_names)

    n = st.slider("Sample Size",50,5000,1000)

    if dist=="Normal":

        mean = st.slider("Mean",-5.0,5.0,0.0)
        std = st.slider("Std",0.1,5.0,1.0)

        data = np.random.normal(mean,std,n)

    elif dist=="Student-t":

        df = st.slider("Degrees of Freedom",1,30,5)
        data = np.random.standard_t(df,n)

    elif dist=="Cauchy":

        data = np.random.standard_cauchy(n)

    elif dist=="Exponential":

        scale = st.slider("Scale",0.1,5.0,1.0)
        data = np.random.exponential(scale,n)

    elif dist=="Gamma":

        shape = st.slider("Shape",0.5,5.0,2.0)
        scale = st.slider("Scale",0.1,5.0,2.0)
        data = np.random.gamma(shape,scale,n)

    elif dist=="Uniform":

        low = st.slider("Low",-5.0,0.0,-1.0)
        high = st.slider("High",0.0,5.0,1.0)
        data = np.random.uniform(low,high,n)

    elif dist=="Beta":

        a = st.slider("Alpha",0.5,5.0,2.0)
        b = st.slider("Beta",0.5,5.0,5.0)
        data = np.random.beta(a,b,n)

    elif dist=="Laplace":

        loc = st.slider("Location",-5.0,5.0,0.0)
        scale = st.slider("Scale",0.1,5.0,1.0)
        data = np.random.laplace(loc,scale,n)

    elif dist=="Lognormal":

        mean = st.slider("Mean",-2.0,2.0,0.0)
        sigma = st.slider("Sigma",0.1,2.0,1.0)
        data = np.random.lognormal(mean,sigma,n)

    elif dist=="Weibull":

        k = st.slider("Shape",0.5,5.0,1.5)
        data = np.random.weibull(k,n)

    elif dist=="Chi-Square":

        df = st.slider("Degrees of Freedom",1,20,4)
        data = np.random.chisquare(df,n)

    elif dist=="Pareto":

        a = st.slider("Shape",1.1,5.0,3.0)
        data = np.random.pareto(a,n)+1

    elif dist=="Rayleigh":

        scale = st.slider("Scale",0.1,5.0,1.0)
        data = np.random.rayleigh(scale,n)

    elif dist=="Gumbel":

        loc = st.slider("Location",-5.0,5.0,0.0)
        scale = st.slider("Scale",0.1,5.0,1.0)
        data = np.random.gumbel(loc,scale,n)

    elif dist=="Poisson":

        lam = st.slider("Lambda",1,10,3)
        data = np.random.poisson(lam,n)

    elif dist=="Binomial":

        trials = st.slider("Trials",1,50,10)
        p = st.slider("Probability",0.0,1.0,0.5)
        data = np.random.binomial(trials,p,n)

    elif dist=="Geometric":

        p = st.slider("Probability",0.05,0.9,0.3)
        data = np.random.geometric(p,n)

    elif dist=="Negative Binomial":

        r = st.slider("Successes",1,20,5)
        p = st.slider("Probability",0.1,0.9,0.5)
        data = np.random.negative_binomial(r,p,n)

    elif dist=="Hypergeometric":

        N = st.slider("Population Size",10,200,50)
        K = st.slider("Successes in Population",1,N-1,20)
        n_draw = st.slider("Draws",1,N,10)

        data = np.random.hypergeometric(K,N-K,n_draw,1000)

    fig, ax = plt.subplots()
    ax.hist(data,bins=30)
    ax.set_title(dist)

    st.pyplot(fig)

    st.stop()

# -----------------------------
# MULTIPLAYER
# -----------------------------

players = st.sidebar.number_input("Players",1,5,1)

if "player" not in st.session_state:
    st.session_state.player = 1

st.write(f"Player {st.session_state.player}'s turn")

# -----------------------------
# SESSION STATE
# -----------------------------

if "data" not in st.session_state:

    dist = random.choice(distribution_names)

    st.session_state.data = generate_distribution(dist,sample_size)
    st.session_state.answer = dist
    st.session_state.score = 0
    st.session_state.rounds = 1
    st.session_state.start = time.time()

# -----------------------------
# TIMER
# -----------------------------

elapsed = int(time.time()-st.session_state.start)

st.write(f"Time: {elapsed} seconds")

# -----------------------------
# HISTOGRAM
# -----------------------------

fig, ax = plt.subplots()

ax.hist(st.session_state.data,bins=30)

st.pyplot(fig)

# -----------------------------
# GUESS
# -----------------------------

guess = st.selectbox("Guess Distribution",distribution_names)

col1,col2,col3,col4 = st.columns(4)

with col1:
    submit = st.button("Submit")

with col2:
    stats = st.button("Statistics")

with col3:
    ml = st.button("ML Hint")

with col4:
    new = st.button("Next Round")

# -----------------------------
# SUBMIT
# -----------------------------

if submit:

    if guess == st.session_state.answer:

        st.success("Correct")
        st.session_state.score += 1

    else:

        st.error(f"Wrong — answer was {st.session_state.answer}")

    st.write(f"Score {st.session_state.score}/{st.session_state.rounds}")

# -----------------------------
# STATS
# -----------------------------

if stats:

    data = st.session_state.data

    st.write("Mean",np.mean(data))
    st.write("Variance",np.var(data))
    st.write("Skewness",skew(data))
    st.write("Kurtosis",kurtosis(data))

# -----------------------------
# ML HINT
# -----------------------------

if ml:

    s = skew(st.session_state.data)
    k = kurtosis(st.session_state.data)

    if abs(s) < 0.2:
        st.write("ML hint: symmetric distribution")

    elif s > 1:
        st.write("ML hint: strong right skew")

    elif s < -1:
        st.write("ML hint: strong left skew")

    if k > 3:
        st.write("ML hint: heavy tails")

# -----------------------------
# NEXT ROUND
# -----------------------------

if new:

    dist = random.choice(distribution_names)

    st.session_state.data = generate_distribution(dist,sample_size)
    st.session_state.answer = dist
    st.session_state.rounds += 1

    st.session_state.player += 1
    if st.session_state.player > players:
        st.session_state.player = 1

    st.session_state.start = time.time()

    st.rerun()

# -----------------------------
# LEADERBOARD
# -----------------------------

st.divider()

st.subheader("Leaderboard")

name = st.text_input("Enter Name")

def save(name,score):

    file = "leaderboard.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
    else:
        df = pd.DataFrame(columns=["Name","Score"])

    df.loc[len(df)] = [name,score]
    df = df.sort_values("Score",ascending=False)
    df.to_csv(file,index=False)

if st.button("Save Score"):
    save(name,st.session_state.score)

if os.path.exists("leaderboard.csv"):

    df = pd.read_csv("leaderboard.csv")

    st.dataframe(df)