# 🎮 Distribution Guessing Game

An interactive **statistics learning game** built with **Python and Streamlit** where players identify probability distributions from their visual patterns.

Instead of memorizing formulas, the game helps develop **statistical intuition** by recognizing shapes, skewness, and tails of sampled data.

---

## 🚀 Project Demo

The game generates random samples from many probability distributions and displays them as histograms.  
Your task: **guess the distribution before the timer runs out.**

Features include hints, scoring, streak bonuses, and a leaderboard.

---

## 🧠 Why This Project Exists

Statistics is often taught through equations.  
But the human brain is extremely good at **pattern recognition**.

This project turns statistical learning into a **visual pattern recognition game**.

You learn to identify:

- heavy tails  
- skewness  
- discrete vs continuous patterns  
- bounded vs unbounded distributions  

---

## 🎮 Game Modes

### 🎯 Game Mode
A timed challenge where players guess the distribution.

Features:

- ⏱ Time-limited rounds
- 📊 Histogram visualization
- 💡 Progressive hints
- 🔥 Streak bonus system
- 👥 Multiplayer turns
- 🏆 Leaderboard

---

### 🔬 Explorer Mode
An interactive statistics sandbox.

Users can:

- Choose any distribution
- Change parameters
- Observe how shape changes
- See sample statistics

Perfect for **learning distributions visually**.

---

### 📚 Reference Mode
A visual reference guide of all supported distributions with short descriptions.

---

## 📊 Supported Distributions

### Continuous Distributions

- Normal
- Student-t
- Cauchy
- Exponential
- Gamma
- Uniform
- Beta
- Laplace
- Lognormal
- Weibull
- Chi-Square
- Pareto
- Rayleigh
- Gumbel

### Discrete Distributions

- Poisson
- Binomial
- Geometric
- Negative Binomial
- Hypergeometric

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| NumPy | Random sampling |
| SciPy | Statistical functions |
| Matplotlib | Data visualization |
| Pandas | Leaderboard data storage |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mayank245956/distribution-guessing-game.git
cd distribution-guessing-game
```

Install dependencies:

```bash
pip install streamlit numpy matplotlib pandas scipy
```

Run the application:

```bash
streamlit run distribution_game.py
```

The game will open automatically in your browser.

---

## 🎯 How to Play

1. A histogram appears.
2. Identify the probability distribution.
3. Submit your guess.
4. Use hints if needed.
5. Score points and build streaks.

Fast answers earn **bonus points**.

---

## 📈 Scoring System

| Action | Points |
|------|------|
| Correct answer | +100 |
| Time bonus | up to +50 |
| Hint penalty | −20 per hint |
| Streak bonus | extra multiplier |

---

## 🏆 Leaderboard

Player scores are saved locally in:

```
leaderboard.csv
```

Top scores are displayed inside the game.

---

## 📸 Screenshots

*(Add screenshots here after running the game)*

Example sections:

```
![Game Mode](screenshots/game_mode.png)

![Explorer Mode](screenshots/explorer_mode.png)
```

---

## 💡 Future Improvements

- Online multiplayer
- Global leaderboard
- More probability distributions
- Mobile-friendly interface
- Web deployment

---

## 👨‍💻 Author

**Mayank Pant**

Statistics • Data Science • Interactive Learning Tools

GitHub:  
https://github.com/mayank245956

---

## ⭐ If You Like This Project

Give the repository a **star** and share it with others learning statistics.