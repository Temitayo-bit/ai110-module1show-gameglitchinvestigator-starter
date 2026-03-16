# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:** A number guessing game where the player picks a number within a range and receives hints until they guess correctly or run out of attempts. Points are awarded based on how few attempts it takes.

**Bugs found:**
1. The game accepted out-of-range inputs (negative numbers and values above 100).
2. Hints were backwards — guessing too low showed "Go LOWER" instead of "Go HIGHER".

**Fixes applied:**
1. Added a range check in `parse_guess()` to reject any number below 1 or above 100.
2. Corrected the comparison logic in `check_guess()` so hints point in the right direction.
3. Refactored all game logic into `logic_utils.py` and added pytest tests to verify both fixes.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
