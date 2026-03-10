import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import os
from scipy.stats import skew, kurtosis
from streamlit_autorefresh import st_autorefresh

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="DistroQuiz — Statistics Game",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; }

.stApp { background: #0a0a0f; color: #e8e8f0; }

section[data-testid="stSidebar"] {
    background: #0f0f1a !important;
    border-right: 1px solid #2a2a4a;
}

/* ── Timer widget ── */
#timer-container {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid #00d4ff33;
    border-radius: 12px;
    padding: 12px 20px 10px;
    margin: 0;
    text-align: center;
    box-shadow: 0 0 20px #00d4ff18;
    font-family: 'Space Mono', monospace;
}
#timer-display {
    font-size: 2.5rem;
    font-weight: 700;
    line-height: 1;
    transition: color 0.4s;
}
#timer-label {
    font-size: 0.7rem;
    color: #7070a0;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 4px;
}
#timer-bar-bg {
    background: #1a1a2e;
    border-radius: 6px;
    height: 6px;
    margin-top: 8px;
    overflow: hidden;
}
#timer-bar-fill {
    height: 100%;
    border-radius: 6px;
    transition: width 0.15s linear, background 0.4s;
}

/* ── Score cards ── */
.score-card {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border: 1px solid #00d4ff33;
    border-radius: 12px;
    padding: 14px 20px;
    margin: 4px 0;
    font-family: 'Space Mono', monospace;
    text-align: center;
    box-shadow: 0 0 20px #00d4ff18;
}
.score-big { font-size: 2.2rem; font-weight: 700; color: #00d4ff; line-height: 1; }
.score-label { font-size: 0.7rem; color: #7070a0; text-transform: uppercase; letter-spacing: 2px; margin-top: 4px; }

/* ── Hint box ── */
.hint-box {
    background: linear-gradient(135deg, #0d1f0d, #0a1a2e);
    border-left: 3px solid #00ff88;
    border-radius: 0 8px 8px 0;
    padding: 10px 16px;
    margin: 6px 0;
    font-family: 'Space Mono', monospace;
    font-size: 0.83rem;
    color: #80ffb8;
}

/* ── Result banners ── */
.result-correct {
    background: linear-gradient(135deg, #0a2e1a, #0f3d1f);
    border: 1px solid #00ff8855;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    color: #00ff88;
    font-size: 1.3rem;
    font-weight: 700;
    font-family: 'Space Mono', monospace;
    margin: 10px 0;
    animation: popIn 0.3s ease;
}
.result-wrong {
    background: linear-gradient(135deg, #2e0a0a, #3d0f0f);
    border: 1px solid #ff446655;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    color: #ff4466;
    font-size: 1.15rem;
    font-weight: 700;
    font-family: 'Space Mono', monospace;
    margin: 10px 0;
    animation: popIn 0.3s ease;
}
.result-timeout {
    background: linear-gradient(135deg, #2a1a00, #3a2a00);
    border: 1px solid #ffaa0055;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
    color: #ffaa00;
    font-size: 1.15rem;
    font-weight: 700;
    font-family: 'Space Mono', monospace;
    margin: 10px 0;
}
@keyframes popIn {
    0%   { transform: scale(0.92); opacity: 0; }
    100% { transform: scale(1);    opacity: 1; }
}

/* ── Chips ── */
.chip-c { color:#00d4ff; font-size:0.65rem; background:#00d4ff15; border:1px solid #00d4ff40; border-radius:4px; padding:1px 6px; font-family:'Space Mono',monospace; }
.chip-d { color:#ff9a00; font-size:0.65rem; background:#ff9a0015; border:1px solid #ff9a0040; border-radius:4px; padding:1px 6px; font-family:'Space Mono',monospace; }

/* ── Leaderboard ── */
.lb-row { display:flex; justify-content:space-between; padding:8px 12px; border-bottom:1px solid #1a1a3a; font-family:'Space Mono',monospace; font-size:0.85rem; }

/* ── Buttons ── */
.stButton > button {
    background: #1a1a3e !important;
    border: 1px solid #3a3a6e !important;
    color: #e0e0ff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    border-color: #00d4ff !important;
    color: #00d4ff !important;
    box-shadow: 0 0 12px #00d4ff33 !important;
}
.stSelectbox > div > div {
    background: #1a1a2e !important;
    border-color: #3a3a6e !important;
    color: #e0e0ff !important;
    font-family: 'Space Mono', monospace !important;
}
h1 { font-family: 'Syne', sans-serif !important; font-weight: 800 !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DISTRIBUTIONS
# ─────────────────────────────────────────────

DISTRIBUTIONS = {
    "Normal":            {"type": "continuous", "emoji": "🔔", "desc": "Bell-shaped, symmetric"},
    "Student-t":         {"type": "continuous", "emoji": "📊", "desc": "Heavier tails than Normal"},
    "Cauchy":            {"type": "continuous", "emoji": "👹", "desc": "Extremely heavy tails, no mean"},
    "Exponential":       {"type": "continuous", "emoji": "📉", "desc": "Memoryless decay"},
    "Gamma":             {"type": "continuous", "emoji": "🌀", "desc": "Generalisation of Exponential"},
    "Uniform":           {"type": "continuous", "emoji": "📏", "desc": "Every value equally likely"},
    "Beta":              {"type": "continuous", "emoji": "🎯", "desc": "Bounded [0,1]"},
    "Laplace":           {"type": "continuous", "emoji": "⛺", "desc": "Double-sided Exponential"},
    "Lognormal":         {"type": "continuous", "emoji": "📈", "desc": "Log of a Normal"},
    "Weibull":           {"type": "continuous", "emoji": "⚙️",  "desc": "Reliability / failure modelling"},
    "Chi-Square":        {"type": "continuous", "emoji": "🔬", "desc": "Sum of squared Normals"},
    "Pareto":            {"type": "continuous", "emoji": "💹", "desc": "Power-law, heavy right tail"},
    "Rayleigh":          {"type": "continuous", "emoji": "🌊", "desc": "Magnitude of 2D vector"},
    "Gumbel":            {"type": "continuous", "emoji": "🌪️",  "desc": "Extreme value distribution"},
    "Poisson":           {"type": "discrete",   "emoji": "🎲", "desc": "Count of rare events"},
    "Binomial":          {"type": "discrete",   "emoji": "🪙", "desc": "Successes in n trials"},
    "Geometric":         {"type": "discrete",   "emoji": "🎳", "desc": "Trials until first success"},
    "Negative Binomial": {"type": "discrete",   "emoji": "🎱", "desc": "Trials until r-th success"},
    "Hypergeometric":    {"type": "discrete",   "emoji": "🎴", "desc": "Draws without replacement"},
}

DIST_NAMES = list(DISTRIBUTIONS.keys())
CONTINUOUS = [k for k, v in DISTRIBUTIONS.items() if v["type"] == "continuous"]
DISCRETE   = [k for k, v in DISTRIBUTIONS.items() if v["type"] == "discrete"]


def generate_distribution(name, n):
    fn = {
        "Normal":            lambda: np.random.normal(0, 1, n),
        "Student-t":         lambda: np.random.standard_t(5, n),
        "Cauchy":            lambda: np.random.standard_cauchy(n),
        "Exponential":       lambda: np.random.exponential(1, n),
        "Gamma":             lambda: np.random.gamma(2, 2, n),
        "Uniform":           lambda: np.random.uniform(0, 1, n),
        "Beta":              lambda: np.random.beta(2, 5, n),
        "Laplace":           lambda: np.random.laplace(0, 1, n),
        "Lognormal":         lambda: np.random.lognormal(0, 1, n),
        "Weibull":           lambda: np.random.weibull(1.5, n),
        "Chi-Square":        lambda: np.random.chisquare(4, n),
        "Pareto":            lambda: np.random.pareto(3, n) + 1,
        "Rayleigh":          lambda: np.random.rayleigh(1, n),
        "Gumbel":            lambda: np.random.gumbel(0, 1, n),
        "Poisson":           lambda: np.random.poisson(3, n),
        "Binomial":          lambda: np.random.binomial(10, 0.5, n),
        "Geometric":         lambda: np.random.geometric(0.3, n),
        "Negative Binomial": lambda: np.random.negative_binomial(5, 0.5, n),
        "Hypergeometric":    lambda: np.random.hypergeometric(7, 13, 5, n),
    }
    return fn[name]()


def plot_histogram(data, answer=None, show_kde=True, color="#00d4ff"):
    fig, ax = plt.subplots(figsize=(9, 3.6))
    fig.patch.set_facecolor("#0a0a0f")
    ax.set_facecolor("#0f0f1a")
    p1, p99 = np.percentile(data, [0.5, 99.5])
    clipped = np.clip(data, p1, p99)
    is_discrete = np.all(data == data.astype(int)) and len(np.unique(data)) < 50
    if is_discrete:
        vals, counts = np.unique(clipped.astype(int), return_counts=True)
        ax.bar(vals, counts / counts.sum(), color=color, alpha=0.75, width=0.6, edgecolor="#ffffff10")
    else:
        ax.hist(clipped, bins=40, density=True, color=color, alpha=0.6, edgecolor="#ffffff08")
        if show_kde:
            from scipy.stats import gaussian_kde
            try:
                kde = gaussian_kde(clipped, bw_method=0.25)
                xs = np.linspace(clipped.min(), clipped.max(), 400)
                ax.plot(xs, kde(xs), color="#ffffff", linewidth=1.8, alpha=0.85)
            except Exception:
                pass
    title = f"✓  {answer}" if answer else "What distribution is this?"
    title_color = "#00ff88" if answer else "#5050a0"
    ax.set_title(title, color=title_color, fontsize=13, fontfamily="monospace", pad=8)
    ax.tick_params(colors="#5050a0", labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor("#2a2a4a")
    ax.grid(axis="y", color="#2a2a4a", linewidth=0.5, alpha=0.5)
    ax.set_xlabel("Value", color="#5050a0", fontsize=9)
    ax.set_ylabel("Density", color="#5050a0", fontsize=9)
    plt.tight_layout()
    return fig


def compute_stats(data):
    safe = np.clip(data, np.percentile(data, 0.1), np.percentile(data, 99.9))
    return {
        "Mean": np.mean(data), "Median": np.median(data),
        "Std Dev": np.std(data), "Variance": np.var(data),
        "Skewness": skew(safe), "Kurtosis": kurtosis(safe),
        "Min": np.min(data), "Max": np.max(data),
    }


def generate_hints(data, n_hints):
    safe = np.clip(data, np.percentile(data, 0.5), np.percentile(data, 99.5))
    s = skew(safe)
    k = kurtosis(safe)
    is_discrete = np.all(data == data.astype(int)) and len(np.unique(data)) < 50
    hints = []
    if n_hints >= 1:
        hints.append("🎲 **Discrete** integer values only" if is_discrete else "📐 **Continuous** distribution")
        if not is_discrete and np.min(data) >= 0:
            hints.append("➡️ Support is **non-negative** (bounded below by 0)")
        if abs(s) < 0.3:      hints.append("⚖️ Roughly **symmetric** shape")
        elif s > 1.5:         hints.append("📈 **Strong right skew** — long tail to the right")
        elif s > 0.4:         hints.append("↗️ Mild **right skew**")
        elif s < -1.5:        hints.append("📉 **Strong left skew** — long tail to the left")
        elif s < -0.4:        hints.append("↙️ Mild **left skew**")
    if n_hints >= 2:
        if k > 5:             hints.append("👹 **Very heavy tails** — extreme outliers frequent")
        elif k > 1:           hints.append("📊 **Moderately heavy tails**")
        elif abs(k) < 0.5:   hints.append("🔔 **Normal-like tails**")
        else:                 hints.append("🪶 **Light tails** — few extreme values")
    if n_hints >= 3:
        if is_discrete:
            vals = np.sort(np.unique(data.astype(int)))
            hints.append(f"🔢 Values range from **{vals[0]}** to **{vals[-1]}** ({len(vals)} unique)")
        else:
            hints.append(f"📏 99th-pct range: **{safe.min():.2f}** – **{safe.max():.2f}**")
            hints.append(f"📊 Mean ≈ **{np.mean(data):.2f}**, Std ≈ **{np.std(data):.2f}**")
    return hints


def score_for_time(elapsed, max_time):
    bonus = max(0, int((max_time - elapsed) / max_time * 50))
    return 100 + bonus


def save_score(name, score, rounds, accuracy):
    file = "leaderboard.csv"
    entry = {"Name": name, "Score": score, "Rounds": rounds,
             "Accuracy %": round(accuracy, 1), "Date": pd.Timestamp.now().strftime("%Y-%m-%d")}
    if os.path.exists(file):
        df = pd.concat([pd.read_csv(file), pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.sort_values("Score", ascending=False).head(20).to_csv(file, index=False)


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("## DistroQuiz ⚡")
    st.markdown("---")
    mode = st.radio("Mode", ["🎮 Game Mode", "🔬 Explorer Mode", "📚 Reference"])
    st.markdown("---")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard", "Extreme"])
    SAMPLE_SIZES = {"Easy": 1200, "Medium": 400, "Hard": 120, "Extreme": 50}
    TIME_LIMITS  = {"Easy": 90,   "Medium": 60,  "Hard": 40,  "Extreme": 25}
    HINTS_MAX    = {"Easy": 3,    "Medium": 2,   "Hard": 1,   "Extreme": 0}
    sample_size = SAMPLE_SIZES[difficulty]
    time_limit  = TIME_LIMITS[difficulty]
    hints_max   = HINTS_MAX[difficulty]
    st.markdown("---")
    players = st.number_input("Players", 1, 5, 1)
    st.markdown("---")
    filter_type = st.radio("Distribution Filter", ["All", "Continuous only", "Discrete only"])
    active_dists = {"All": DIST_NAMES, "Continuous only": CONTINUOUS, "Discrete only": DISCRETE}[filter_type]
    st.markdown("---")
    show_kde = st.checkbox("Show KDE curve", value=True)


# ─────────────────────────────────────────────
# REFERENCE MODE
# ─────────────────────────────────────────────

if "Reference" in mode:
    st.markdown("# 📚 Distribution Reference")
    cols = st.columns(2)
    for i, (name, info) in enumerate(DISTRIBUTIONS.items()):
        with cols[i % 2]:
            chip = "chip-c" if info["type"] == "continuous" else "chip-d"
            st.markdown(f"""<div style='background:#1a1a2e;border:1px solid #2a2a4e;border-radius:10px;
                            padding:10px 14px;margin:5px 0;'>
                <span style='font-size:1.2rem'>{info['emoji']}</span>
                <strong style='color:#e0e0ff'> {name}</strong>
                <span class='{chip}' style='margin-left:6px'>{info['type']}</span><br/>
                <small style='color:#7070a0;font-family:Space Mono,monospace'>{info['desc']}</small>
            </div>""", unsafe_allow_html=True)
            raw = generate_distribution(name, 600)
            sample = np.clip(raw, np.percentile(raw, 0.5), np.percentile(raw, 99.5))
            fig, ax = plt.subplots(figsize=(4, 1.4))
            fig.patch.set_facecolor("#0a0a0f"); ax.set_facecolor("#0f0f1a")
            c = "#00d4ff" if info["type"] == "continuous" else "#ff9a00"
            ax.hist(sample, bins=28, color=c, alpha=0.7, edgecolor="none", density=True)
            ax.set_xticks([]); ax.set_yticks([])
            for sp in ax.spines.values(): sp.set_edgecolor("#2a2a4a")
            plt.tight_layout(pad=0.1)
            st.pyplot(fig); plt.close()
    st.stop()


# ─────────────────────────────────────────────
# EXPLORER MODE
# ─────────────────────────────────────────────

if "Explorer" in mode:
    st.markdown("# 🔬 Distribution Explorer")
    cl, cr = st.columns([1, 2])
    with cl:
        dist = st.selectbox("Distribution", DIST_NAMES,
                            format_func=lambda x: f"{DISTRIBUTIONS[x]['emoji']} {x}")
        info = DISTRIBUTIONS[dist]
        n = st.slider("Sample Size", 50, 5000, 1000)
        st.markdown("**Parameters**")
        if dist == "Normal":
            m = st.slider("Mean", -5.0, 5.0, 0.0); s2 = st.slider("Std Dev", 0.1, 5.0, 1.0)
            data = np.random.normal(m, s2, n)
        elif dist == "Student-t":
            df = st.slider("Degrees of Freedom", 1, 30, 5); data = np.random.standard_t(df, n)
        elif dist == "Cauchy":
            data = np.random.standard_cauchy(n); st.info("No adjustable parameters")
        elif dist == "Exponential":
            sc = st.slider("Scale", 0.1, 5.0, 1.0); data = np.random.exponential(sc, n)
        elif dist == "Gamma":
            sh = st.slider("Shape", 0.5, 10.0, 2.0); sc = st.slider("Scale", 0.1, 5.0, 2.0)
            data = np.random.gamma(sh, sc, n)
        elif dist == "Uniform":
            lo = st.slider("Low", -10.0, 0.0, 0.0); hi = st.slider("High", 0.01, 10.0, 1.0)
            data = np.random.uniform(lo, hi, n)
        elif dist == "Beta":
            a = st.slider("Alpha", 0.1, 10.0, 2.0); b = st.slider("Beta", 0.1, 10.0, 5.0)
            data = np.random.beta(a, b, n)
        elif dist == "Laplace":
            lo = st.slider("Location", -5.0, 5.0, 0.0); sc = st.slider("Scale", 0.1, 5.0, 1.0)
            data = np.random.laplace(lo, sc, n)
        elif dist == "Lognormal":
            m = st.slider("μ (log)", -2.0, 2.0, 0.0); sg = st.slider("σ (log)", 0.1, 2.0, 1.0)
            data = np.random.lognormal(m, sg, n)
        elif dist == "Weibull":
            k = st.slider("Shape", 0.3, 5.0, 1.5); data = np.random.weibull(k, n)
        elif dist == "Chi-Square":
            df = st.slider("Degrees of Freedom", 1, 30, 4); data = np.random.chisquare(df, n)
        elif dist == "Pareto":
            a = st.slider("Shape", 1.1, 10.0, 3.0); data = np.random.pareto(a, n) + 1
        elif dist == "Rayleigh":
            sc = st.slider("Scale", 0.1, 5.0, 1.0); data = np.random.rayleigh(sc, n)
        elif dist == "Gumbel":
            lo = st.slider("Location", -5.0, 5.0, 0.0); sc = st.slider("Scale", 0.1, 5.0, 1.0)
            data = np.random.gumbel(lo, sc, n)
        elif dist == "Poisson":
            lm = st.slider("Lambda", 1, 30, 5); data = np.random.poisson(lm, n)
        elif dist == "Binomial":
            tr = st.slider("Trials", 1, 100, 10); p = st.slider("Probability", 0.01, 0.99, 0.5)
            data = np.random.binomial(tr, p, n)
        elif dist == "Geometric":
            p = st.slider("Probability", 0.05, 0.95, 0.3); data = np.random.geometric(p, n)
        elif dist == "Negative Binomial":
            r = st.slider("Successes", 1, 30, 5); p = st.slider("Probability", 0.1, 0.9, 0.5)
            data = np.random.negative_binomial(r, p, n)
        elif dist == "Hypergeometric":
            N = st.slider("Population", 10, 200, 50)
            K = st.slider("Successes in pop", 1, N - 1, 20)
            nd = st.slider("Draws", 1, N, 10)
            data = np.random.hypergeometric(K, N - K, nd, n)
        else:
            data = generate_distribution(dist, n)
    with cr:
        c = "#00d4ff" if info["type"] == "continuous" else "#ff9a00"
        st.pyplot(plot_histogram(data, answer=dist, show_kde=show_kde, color=c))
        plt.close()
        st_stats = compute_stats(data)
        sc2 = st.columns(4)
        for i, (k, v) in enumerate(st_stats.items()):
            with sc2[i % 4]:
                st.markdown(f"""<div class='score-card'>
                    <div class='score-big' style='font-size:1.3rem'>{v:.3f}</div>
                    <div class='score-label'>{k}</div></div>""", unsafe_allow_html=True)
    st.stop()


# ─────────────────────────────────────────────
# GAME MODE — SESSION STATE
# ─────────────────────────────────────────────

def new_round():
    d = random.choice(active_dists)
    st.session_state.data           = generate_distribution(d, sample_size)
    st.session_state.answer         = d
    st.session_state.rounds        += 1
    st.session_state.start          = time.time()
    st.session_state.hint_used      = 0
    st.session_state.round_answered = False
    st.session_state.round_correct  = None
    st.session_state.points_earned  = 0
    st.session_state.timed_out      = False
    st.session_state.show_stats     = False


DEFAULTS = {
    "score": 0, "rounds": 0, "correct": 0,
    "streak": 0, "best_streak": 0, "player": 1,
    "hint_used": 0, "round_answered": False,
    "round_correct": None, "points_earned": 0,
    "timed_out": False, "show_stats": False, "history": [],
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

if "data" not in st.session_state:
    d = random.choice(active_dists)
    st.session_state.data   = generate_distribution(d, sample_size)
    st.session_state.answer = d
    st.session_state.start  = time.time()
    st.session_state.rounds = 1


# ─────────────────────────────────────────────
#  LIVE TIMER
#  • st_autorefresh fires every 1 s → Python re-runs → checks timeout
#  • JavaScript setInterval ticks every 100 ms → smooth visual countdown
# ─────────────────────────────────────────────

if not st.session_state.round_answered:
    # Fires a full Streamlit re-run every 1 000 ms while round is active.
    # This keeps the server-side time_left in sync and catches timeout.
    st_autorefresh(interval=1000, limit=time_limit + 10, key="game_timer")

# Server-side ground truth
elapsed_now = time.time() - st.session_state.start
time_left   = max(0.0, time_limit - elapsed_now)
pct         = time_left / time_limit


# ─────────────────────────────────────────────
# HEADER + SCOREBOARD
# ─────────────────────────────────────────────

st.markdown(
    "# DistroQuiz ⚡ "
    "<small style='font-size:0.55em;color:#5050a0;'>Statistics Distribution Game</small>",
    unsafe_allow_html=True,
)

s1, s2, s3, s4, s5 = st.columns(5)

with s1:
    st.markdown(f"""<div class='score-card'>
        <div class='score-big'>{st.session_state.score}</div>
        <div class='score-label'>Score</div></div>""", unsafe_allow_html=True)
with s2:
    denom = max(st.session_state.rounds - 1, 1)
    acc = st.session_state.correct / denom * 100
    st.markdown(f"""<div class='score-card'>
        <div class='score-big'>{acc:.0f}%</div>
        <div class='score-label'>Accuracy</div></div>""", unsafe_allow_html=True)
with s3:
    st.markdown(f"""<div class='score-card'>
        <div class='score-big'>{st.session_state.streak}</div>
        <div class='score-label'>🔥 Streak</div></div>""", unsafe_allow_html=True)
with s4:
    st.markdown(f"""<div class='score-card'>
        <div class='score-big'>{st.session_state.rounds}</div>
        <div class='score-label'>Round</div></div>""", unsafe_allow_html=True)

with s5:
    # JavaScript receives the exact remaining seconds from Python,
    # then counts down every 100 ms independently — no flicker, no jump.
    paused_js = "true" if st.session_state.round_answered else "false"
    st.markdown(f"""
    <div id="timer-container">
        <div id="timer-display">--</div>
        <div id="timer-label">TIME LEFT</div>
        <div id="timer-bar-bg">
            <div id="timer-bar-fill" style="width:100%;background:#00ff88"></div>
        </div>
    </div>

    <script>
    (function() {{
        const remaining0 = {time_left:.3f};   // exact float from Python
        const maxTime    = {time_limit};
        const paused     = {paused_js};

        const display = document.getElementById('timer-display');
        const barFill = document.getElementById('timer-bar-fill');

        if (!display || !barFill) return;

        let remaining = remaining0;

        function color(secs) {{
            const p = secs / maxTime;
            return p > 0.4 ? '#00ff88' : p > 0.2 ? '#ffaa00' : '#ff4466';
        }}

        function render(secs) {{
            const s = Math.max(0, secs);
            display.textContent      = Math.ceil(s) + 's';
            display.style.color      = color(s);
            barFill.style.background = color(s);
            barFill.style.width      = ((s / maxTime) * 100).toFixed(2) + '%';
        }}

        render(remaining);        // immediate — no blank flash

        if (paused) return;       // round already answered — freeze here

        const iv = setInterval(() => {{
            remaining -= 0.1;
            if (remaining <= 0) {{
                render(0);
                clearInterval(iv);
                return;
            }}
            render(remaining);
        }}, 100);

        // Safety: clear when Streamlit remounts the component
        window._distroTimerIv = iv;
    }})();
    </script>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TIMEOUT CHECK  (runs after autorefresh tick)
# ─────────────────────────────────────────────

if time_left <= 0 and not st.session_state.round_answered:
    st.session_state.round_answered = True
    st.session_state.round_correct  = False
    st.session_state.timed_out      = True
    st.session_state.streak         = 0
    st.session_state.history.append({
        "Round": st.session_state.rounds, "Answer": st.session_state.answer,
        "Guess": "⏰ Timeout", "Correct": "✗", "Points": 0, "Time (s)": time_limit,
    })
    st.rerun()


# ─────────────────────────────────────────────
# HISTOGRAM
# ─────────────────────────────────────────────

st.markdown("---")
plot_color = "#00d4ff"
if st.session_state.round_answered:
    plot_color = "#00ff88" if st.session_state.round_correct else "#ff4466"

fig = plot_histogram(
    st.session_state.data,
    answer=st.session_state.answer if st.session_state.round_answered else None,
    show_kde=show_kde,
    color=plot_color,
)
st.pyplot(fig)
plt.close()

# ── Result banner ──
if st.session_state.round_answered:
    if st.session_state.timed_out:
        st.markdown(f"""<div class='result-timeout'>
            ⏰ TIME'S UP! — It was <strong>{st.session_state.answer}</strong>
            {DISTRIBUTIONS[st.session_state.answer]['emoji']}
        </div>""", unsafe_allow_html=True)
    elif st.session_state.round_correct:
        stk = f" 🔥 {st.session_state.streak}-streak bonus!" if st.session_state.streak > 1 else ""
        st.markdown(f"""<div class='result-correct'>
            ✓ CORRECT!{stk} &nbsp; +{st.session_state.points_earned} pts
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div class='result-wrong'>
            ✗ Wrong — It was <strong>{st.session_state.answer}</strong>
            {DISTRIBUTIONS[st.session_state.answer]['emoji']}
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# CONTROLS
# ─────────────────────────────────────────────

st.markdown("---")
col_guess, col_btns = st.columns([2, 3])

with col_guess:
    guess = st.selectbox(
        "Guess", active_dists,
        format_func=lambda x: f"{DISTRIBUTIONS[x]['emoji']} {x}",
        disabled=st.session_state.round_answered,
        label_visibility="collapsed",
    )

with col_btns:
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        submit = st.button("✅ Submit",
                           disabled=st.session_state.round_answered,
                           use_container_width=True)
    with b2:
        hints_left = hints_max - st.session_state.hint_used
        hint_btn = st.button(
            f"💡 Hint ({hints_left})",
            disabled=(hints_left <= 0 or st.session_state.round_answered),
            use_container_width=True,
        )
    with b3:
        stats_btn = st.button("📊 Stats", use_container_width=True)
    with b4:
        next_btn = st.button("⏭ Next →", use_container_width=True)


# ── Submit ──
if submit and not st.session_state.round_answered:
    el = time.time() - st.session_state.start
    correct = (guess == st.session_state.answer)
    st.session_state.round_answered = True
    st.session_state.round_correct  = correct
    st.session_state.timed_out      = False
    if correct:
        pts = score_for_time(el, time_limit)
        pts = max(10, pts - st.session_state.hint_used * 20)
        st.session_state.streak += 1
        if st.session_state.streak > 1:
            pts = int(pts * (1 + (st.session_state.streak - 1) * 0.1))
        st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
        st.session_state.score   += pts
        st.session_state.correct += 1
        st.session_state.points_earned = pts
    else:
        st.session_state.streak        = 0
        st.session_state.points_earned = 0
    st.session_state.history.append({
        "Round": st.session_state.rounds, "Answer": st.session_state.answer,
        "Guess": guess, "Correct": "✓" if correct else "✗",
        "Points": st.session_state.points_earned, "Time (s)": round(el, 1),
    })
    st.rerun()


# ── Hint ──
if hint_btn:
    st.session_state.hint_used += 1
    st.rerun()

if st.session_state.hint_used > 0:
    for h in generate_hints(st.session_state.data, st.session_state.hint_used):
        st.markdown(f"<div class='hint-box'>💡 {h}</div>", unsafe_allow_html=True)


# ── Stats toggle ──
if stats_btn:
    st.session_state.show_stats = not st.session_state.get("show_stats", False)

if st.session_state.get("show_stats"):
    st_data = compute_stats(st.session_state.data)
    sc = st.columns(4)
    for i, (k, v) in enumerate(st_data.items()):
        with sc[i % 4]:
            st.markdown(f"""<div class='score-card'>
                <div class='score-big' style='font-size:1.2rem'>{v:.3f}</div>
                <div class='score-label'>{k}</div></div>""", unsafe_allow_html=True)


# ── Next round ──
if next_btn:
    if players > 1:
        st.session_state.player = (st.session_state.player % players) + 1
    new_round()
    st.rerun()


# ─────────────────────────────────────────────
# ROUND HISTORY
# ─────────────────────────────────────────────

if st.session_state.history:
    with st.expander("📋 Round History", expanded=False):
        st.dataframe(pd.DataFrame(st.session_state.history),
                     use_container_width=True, hide_index=True)


# ─────────────────────────────────────────────
# LEADERBOARD
# ─────────────────────────────────────────────

st.markdown("---")
st.markdown("## 🏆 Leaderboard")
lb_col, save_col = st.columns([3, 2])

with save_col:
    player_name = st.text_input("Your name", placeholder="Enter name to save score")
    if st.button("💾 Save Score", use_container_width=True):
        if player_name.strip():
            rp   = max(st.session_state.rounds - 1, 1)
            acc2 = st.session_state.correct / rp * 100
            save_score(player_name.strip(), st.session_state.score, rp, acc2)
            st.success("Saved! 🎉")
        else:
            st.warning("Enter a name first")
    if st.button("🔄 Reset Game", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with lb_col:
    if os.path.exists("leaderboard.csv"):
        df = pd.read_csv("leaderboard.csv")
        for i, row in df.head(10).iterrows():
            medal = ["🥇", "🥈", "🥉"][i] if i < 3 else f"#{i + 1}"
            st.markdown(f"""<div class='lb-row'>
                <span>{medal} &nbsp; {row['Name']}</span>
                <span style='color:#00d4ff;font-family:Space Mono,monospace'>
                    {int(row['Score'])} pts · {row.get('Accuracy %','?')}% acc
                </span></div>""", unsafe_allow_html=True)
    else:
        st.markdown("<div style='color:#5050a0;font-family:Space Mono,monospace'>No scores yet — be first!</div>",
                    unsafe_allow_html=True)