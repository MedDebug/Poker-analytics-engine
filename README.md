# Poker Engine

A modular Texas Hold'em poker engine built in Python.

The project started as a probability calculator and evolved into a structured poker engine capable of evaluating hands and performing large numbers of simulations.

## Features

* Texas Hold'em hand evaluation
* Card and deck handling
* Community board handling
* Player hand evaluation
* Poker hand ranking
* Monte Carlo simulation
* Win/equity estimation
* Modular architecture

## How It Works

The engine takes the known cards and simulates possible remaining game states.

A simplified flow looks like:

```text
Input Cards
     │
     ▼
Card / Deck Handling
     │
     ▼
Generate Possible Boards
     │
     ▼
Evaluate Hands
     │
     ▼
Compare Results
     │
     ▼
Calculate Equity
```

For simulation-based calculations, the engine repeatedly generates possible outcomes and aggregates the results to estimate the probability of winning.

## Project Structure

The project is separated into modules so individual components can be developed and optimized independently.

```text
poker/
├── main.py
├── ...
└── README.md
```

The exact module structure may evolve as the engine becomes more sophisticated.

## Performance

The project originally performed simulations in a single monolithic implementation.

It was later reorganized into separate modules to improve:

* Maintainability
* Organization
* Testing
* Optimization
* Reusability

Performance is an ongoing focus as simulation counts increase.

## Example

A typical interaction can provide known hole cards and optional community cards:

```text
Enter cards: Ah Kc
Enter known board cards, or press Enter if none:
```

The engine then evaluates possible outcomes through simulation.

## Technologies

* Python
* Object-oriented programming
* Probability
* Monte Carlo simulation
* Modular programming

## What This Project Taught Me

This project provided practical experience with:

* Breaking a large program into modules
* Designing reusable functions
* Probability and simulation
* Algorithmic optimization
* Working with card representations
* Testing and debugging
* Git and GitHub

## Future Improvements

Potential future development includes:

* [ ] More efficient simulation
* [ ] Improved hand-evaluation performance
* [ ] Larger simulation workloads
* [ ] More advanced equity calculations
* [ ] GUI
* [ ] Interactive poker table
* [ ] Opponent modeling
* [ ] Strategy analysis

## Author

Built by **Medhansh Singh**.

