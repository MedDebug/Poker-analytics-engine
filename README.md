# 🃏 Poker Monte Carlo Analytics Engine

A Python-based Texas Hold'em Poker Odds Calculator and Analytics Engine that uses **Monte Carlo Simulation** to estimate winning probabilities against multiple opponents.

The project evaluates poker hands, simulates thousands of random games, exports statistical data, and generates graphical analysis.

---

## 🚀 Features

* ✅ Texas Hold'em hand evaluator
* ✅ Monte Carlo simulation engine
* ✅ Supports **1–8 opponents**
* ✅ Supports **Preflop, Flop, Turn, and River** analysis
* ✅ Detects all poker hands:

  * High Card
  * One Pair
  * Two Pair
  * Three of a Kind
  * Straight
  * Flush
  * Full House
  * Four of a Kind
  * Straight Flush
  * Royal Flush
* ✅ Automatic input validation
* ✅ Best 5-card hand selection from 7 cards
* ✅ Win / Loss / Tie probability calculation
* ✅ Hand frequency analytics
* ✅ CSV export of simulation results
* ✅ Win Rate vs Opponents graph generation
* ✅ Modular project architecture

---

## 📂 Project Structure

```
poker_project/
│
├── main.py            # Entry point
├── cards.py           # Card constants and mappings
├── validation.py      # Input validation
├── evaluator.py       # Poker hand evaluation logic
├── simulation.py      # Monte Carlo simulation engine
├── analytics.py       # Data analysis and graph generation
├── poker_results.csv  # Generated analytics output
└── winrate_vs_opponents.png
```

---

## 🧠 How It Works

The engine performs Monte Carlo simulation by:

1. Removing known cards from the deck.
2. Randomly dealing unknown opponent and community cards.
3. Evaluating every player's strongest possible 5-card hand.
4. Comparing the hero hand against all opponents.
5. Repeating the process thousands of times.
6. Estimating probabilities from the observed outcomes.

As the number of trials increases, the estimated probabilities converge toward the true poker equity.

---

## 📊 Analytics

The project automatically generates:

* Win percentage
* Loss percentage
* Tie percentage
* Hand frequency distribution
* Win Rate vs Opponents graph
* CSV export for further analysis

---

## 🛠 Technologies Used

* Python
* Pandas
* Matplotlib
* itertools
* Random (Monte Carlo Simulation)

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate into the project:

```bash
cd poker_project
```

Install dependencies:

```bash
pip install pandas matplotlib
```

Run:

```bash
python main.py
```

---

## 📈 Example Analysis

Input:

```
Hero Cards:
Ah Kc
```

The engine automatically analyzes the hand against **1–8 opponents**, exports the results to CSV, and generates a graph showing how the win rate changes as the number of opponents increases.

---

## 🎯 Future Improvements

* GUI/Desktop application
* Starting hand heatmaps
* Exact probability calculation (non-Monte Carlo)
* Performance optimizations
* Poker AI decision engine
* Equity comparison between multiple starting hands
* Tournament simulation

---

## 👨‍💻 Author

Built as a personal project to explore:

* Algorithms
* Probability
* Simulation
* Data Analytics
* Software Architecture
* Modular Python Development

This project served as a practical exercise in building a complete software application from scratch.
