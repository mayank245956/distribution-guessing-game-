# Statistics Distribution Guessing Game

An interactive web application for learning probability distributions through visual intuition.

The app generates random samples from statistical distributions and displays their histograms. Players must identify which probability distribution produced the data.

The project also includes an **Explorer Mode** that allows users to experiment with distribution parameters and observe how shapes change.

Built using **Python, Streamlit, NumPy, SciPy, and Matplotlib**.

---

# Features

### Game Mode

* Random distribution generated each round
* Histogram visualization
* Guess the correct distribution
* Score tracking
* Multiplayer turns
* Timer per round
* Machine learning hints based on statistical moments
* Statistics clues (mean, variance, skewness, kurtosis)

### Explorer Mode

Interactive environment to study distributions.

Users can:

* Select any distribution
* Adjust parameters with sliders
* Change sample sizes
* Observe how histograms change in real time

---

# Supported Distributions

## Continuous Distributions

* Normal
* Student-t
* Cauchy
* Exponential
* Gamma
* Uniform
* Beta
* Laplace
* Lognormal
* Weibull
* Chi-Square
* Pareto
* Rayleigh
* Gumbel

## Discrete Distributions

* Poisson
* Binomial
* Geometric
* Negative Binomial
* Hypergeometric

---

# Technologies Used

* Python
* Streamlit
* NumPy
* SciPy
* Matplotlib
* Pandas

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install dependencies

```bash
pip install streamlit numpy matplotlib pandas scipy
```

Run the application

```bash
streamlit run distribution_game.py
```

The app will open automatically in your browser.

---

# Project Structure

```
distribution_game.py   # Main application
leaderboard.csv        # Saved scores
README.md              # Project documentation
```

---

# Educational Purpose

This project helps build intuition for probability distributions.

Instead of memorizing formulas, users learn by recognizing **patterns in data**.
By repeatedly observing histograms, players develop a stronger understanding of how different distributions behave.

This mirrors real statistical inference, where analysts attempt to identify the underlying process that generated observed data.

---

# Future Improvements

Possible upgrades:

* Machine learning classifier that predicts the distribution automatically
* Mixture distributions
* Parameter estimation challenges
* Online leaderboard
* Interactive density curves

---

# Author

Mayank Pant

---

# License

This project is open source and available under the MIT License.
