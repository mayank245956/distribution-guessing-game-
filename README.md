# Distribution Guessing Game

A simple interactive statistics game built with **Python and Streamlit** where players try to identify probability distributions by looking at histograms.

The goal of the game is to improve intuition about statistical distributions such as Normal, Poisson, Gamma, Beta, and others.

---

## Project Idea

In statistics classes we often memorize distribution shapes without actually developing intuition for them.

This project turns that learning process into a game.

The application randomly generates data from different probability distributions and displays a histogram.
The player must guess which distribution produced the data.

The game also provides statistical clues like:

* Mean
* Variance
* Skewness
* Kurtosis

These hints help players connect numerical properties with visual patterns.

---

## Distributions Included

The game currently includes several common distributions used in statistics and data science:

Continuous distributions

* Normal
* Student-t
* Cauchy
* Exponential
* Gamma
* Lognormal
* Weibull
* Chi-Square
* Uniform
* Beta
* Pareto
* Gumbel
* Rayleigh
* Laplace

Discrete distributions

* Poisson
* Binomial
* Geometric
* Negative Binomial

---

## How the Game Works

1. The program randomly selects a probability distribution.
2. It generates 1000 data points from that distribution.
3. A histogram of the generated data is displayed.
4. The player guesses which distribution it is.
5. The score updates based on correct guesses.
6. Players can reveal statistical hints to help identify the distribution.

---

## Installation

Clone the repository

```
git clone https://github.com/mayank245956/distribution-guessing-game-.git
```

Move into the project folder

```
cd distribution-guessing-game-
```

Install the required libraries

```
pip install streamlit numpy matplotlib scipy
```

---

## Run the Game

Start the Streamlit app

```
streamlit run distribution_game.py
```

The game will open in your browser.

---

## Technologies Used

Python
Streamlit
NumPy
Matplotlib
SciPy

---

## Educational Purpose

This project is designed to help students develop **statistical intuition** rather than just memorizing formulas.

By repeatedly guessing distributions from visual patterns and statistical summaries, players build a stronger understanding of how different distributions behave.

---

## Possible Future Improvements

* Difficulty levels
* Timed challenges
* Leaderboard system
* Multiplayer mode
* Distribution explanations after each round
* Machine learning model to suggest guesses

---

## Author

Mayank Pant

---

## License

This project is open source and available under the MIT License.
