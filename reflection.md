# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - A game where the player guess a number within a range.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints that advised to go higher and lower were not the correct direction. 
  - When clicking the new game button, nothing happened.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location
|-------|-------------------|-----------------|------------------------|------------------------|
| 1 | Hint should display go higher | Hint displays go lower | N/A | app.py, check_guess
| -1 | Should not be allowed to input lower than 1 | Hint displays go lower | N/A | app.py, check_guess
| 101 | Should not be allowed to input higher than 100 | Hint displays go higher | N/A | app.py, check_guess
| 6 (when secret is 40) | Hint should appear displaying go higher | Hint does not appear and score goes negative | N/A | app.py, update_score
| Clicked "New Game" button | Attempts reset | Nothing changed | N/A | app.py, new_game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - It correctly identified source of the bug of negative scores and understood the logic. I verified the result by reviewing the logic of the AI generated code.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - For the new game bug, it fixed a different bug that was unrelated to my prompt. I instructed it to fix a  bug where the state was not being updated, but it fixed a different bug in the same area where values were hardcoded.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I ran the app and ran tests and confirmed it worked as expected.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran the original 3 tests and when they failed, realized that it wasn't the app code but the test code that had bugs.
- Did AI help you design or understand any tests? How?
  - Yes. I asked it for test suggestions based on the application code, and it gave thorough tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Its reruns occur when a user interacts with the app, and the rerun will reload the app based on the user's changes. Its session state saves its data for the next run.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - I learned how to add reference files for AI to find references easier.  
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would use new chats for different topics. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I think that AI can be helpful even if the task is simple, because it can sometimes find overlooked bugs.
