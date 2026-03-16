# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?


- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. the game let me guess a number higher than 100 and lower than 0, when i use a negative number it says go lower (i didnt expect it to let me submit numbers less than one and higher than 100)
  2. the only hint is go lower (no clear hints) - (i expected accurate hints, like when i put a number below secret, it doesnt say go lower, but go higher)
  3. when i try to start a new game, it doesnt work, it just gets stuck (when i try to start a new game, i shouldnt have to refresh the page but it automatically refreshes my history and also refreshes my attempts and lets me start again)
  4. the game says i am out of attempts even when i still have attemptss left - (i expect to be able to play the game till my attempts are 0)

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude (Claude Code) as my AI assistant throughout this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

**Correct suggestion — fixing the hint direction in `check_guess()`:**
I told Claude the game always said "go lower" no matter what number I guessed. Claude looked at `logic_utils.py` and confirmed the comparison logic (`guess > secret` → "Go LOWER!", else → "Go HIGHER!") was actually correct in the current code, and that the real issue was the hints not being surfaced properly. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
**Incorrect/misleading suggestion — doing more than I asked:**
When I first asked Claude to generate tests for the two bugs, it also rewrote the existing three tests (changing how they unpack the return value from `check_guess`) without me asking for that. At first I had to tell Claude to only do what I specifically asked and to be more precise about my instructions — Claude was making extra "improvements" like fixing unrelated code, adding comments everywhere, and refactoring things I never mentioned. Once I was more specific and direct in my prompts ("only generate tests for these two fixes"), Claude stayed focused. I verified that the unrequested changes were unnecessary by reading the original code myself and confirming the only real issues were the two bugs I reported.

---

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I used the tests and i also ran the App and checked if what i fixed actually worked on the frontend 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I used manual, and it showed that the changed we made was correct
- Did AI help you design or understand any tests? How?
AI helped me design the tests but i went through the tests myself to understand

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The original app had `secret = random.randint(low, high)` written at the top level of the script with no protection. Every time a button was clicked, Streamlit re-ran the entire script from top to bottom, which called `random.randint` again and generated a brand new secret number. So the number I was trying to guess kept changing on every click without me knowing.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Imagine every time you click a button on a webpage, the whole page reloads from scratch and forgets everything — that's basically how Streamlit works by default. Session state is like a sticky notepad that survives those reloads. You write something on it once, and it stays there no matter how many times the page reruns. Without it, every variable just resets.

- What change did you make that finally gave the game a stable secret number?

I wrapped the secret number assignment in an `if "secret" not in st.session_state:` check. That way, `random.randint` only runs once — the very first time the game loads. After that, Streamlit skips it and keeps the same number stored in `st.session_state.secret` for the rest of the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Writing tests that directly match the bugs I fixed. Instead of just running the app and hoping things look right, having specific pytest tests for the out-of-range input and the hint direction gave me real confidence the fixes actually worked. I want to keep doing that — write a test that fails first, then fix the code until it passes.

- What is one thing you would do differently next time you work with AI on a coding task?

I would be more specific from the start about the exact scope of what I want. Early on I asked Claude broad questions and it made changes I didn't ask for. Next time I'll say something like "only change this one function, nothing else" so it doesn't go off and refactor things I didn't mention.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I used to assume AI-generated code was basically correct and just needed small tweaks. Now I know it can have real logical bugs — like hints pointing the wrong way — that look fine on the surface but break the game in practice, so I need to actually read and test the code instead of trusting it blindly.
