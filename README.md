# Brain Games

A set of five command-line mini-games for brain training. Each game asks the player a series of questions. A correct answer is rewarded, a wrong one ends the game.

### Hexlet tests and linter status:

[![Maintainability](https://api.codeclimate.com/v1/badges/b52056a9b73c46aab3b4/maintainability)](https://codeclimate.com/github/joshirova/python-project-49/maintainability)

[![Actions Status](https://github.com/joshirova/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/joshirova/python-project-49/actions)

---

## 🧰 Technologies Used

- Python 3.10+
- Poetry (for dependency management)
- Flake8 (for code linting)
- Asciinema (for terminal recordings)
- Git & GitHub Actions (for CI/CD)

---

## 🎮 Available Games

- **Even** – Determine if a given number is even.
- **Calc** – Solve a random arithmetic expression.
- **GCD** – Find the greatest common divisor.
- **Progression** – Guess the missing number in a progression.
- **Prime** – Decide whether a given number is prime.

---

## 📽 Demo

### General Demo

[![asciinema](https://asciinema.org/a/tIq2ox1wu9sND1k1xKG3Y9u9n.svg)](https://asciinema.org/a/tIq2ox1wu9sND1k1xKG3Y9u9n)

### Calculator Game

[![asciicast](https://asciinema.org/a/jhFmipxgLAC1fZdSFT2kkNl8b.svg)](https://asciinema.org/a/jhFmipxgLAC1fZdSFT2kkNl8b)

### GCD Game

[![asciicast](https://asciinema.org/a/nRoQohm2EDB2dxa5SBKyTlFXJ.svg)](https://asciinema.org/a/nRoQohm2EDB2dxa5SBKyTlFXJ)

### Progression Game

[![asciicast](https://asciinema.org/a/EfSg79bVd1QNM9rfLMOO46E6e.svg)](https://asciinema.org/a/EfSg79bVd1QNM9rfLMOO46E6e)

### Prime Number Game

[![asciicast](https://asciinema.org/a/k166stlCucSOEhZ3N1vPlgO6j.svg)](https://asciinema.org/a/k166stlCucSOEhZ3N1vPlgO6j)

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/joshirova/python-project-49.git
cd python-project-49
````

2. Install dependencies using Poetry:

```bash
make install
```

---

## ▶️ Running the Games

Use the following commands to launch each game:

```bash
brain-even        # Even number game
brain-calc        # Calculator game
brain-gcd         # Greatest common divisor game
brain-progression # Arithmetic progression game
brain-prime       # Prime number game
```

---

## ♻️ Reinstallation

If you need to reinstall the project:

```bash
make uninstall
make install
```

---

## ❌ Uninstallation

```bash
make uninstall
```

---

## 🧪 Run Linter and Tests

```bash
make lint        # Run Flake8 linter
make test        # Run tests (if applicable)
```

---

## 📄 License

This project is licensed under the MIT License.
