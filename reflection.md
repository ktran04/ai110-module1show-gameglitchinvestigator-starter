# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

If you entered a low number it'd tell you to go lower and same for high number. The hints were backwards. The score is also weird. There are 8 attempts but my score was -25 after being wrong 8 times (on the 3rd play). Looking at the code it seems like it would return the range 1-100 regardless of mode (need to check this).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
This is from my 2nd play
|-------|-------------------|-----------------|------------------------|
| 33| "Lower" | "Higher" | "Too High", "📈 Go HIGHER!"|
| 23| "Lower" | "Higher" | "Too High", "📈 Go HIGHER!"|
| 22| "Lower" | "Higher" | "Too High", "📈 Go HIGHER!"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It fixed the backwards hints, fixed the ranges to better reflect the difficulty, st.info to give actual range instead of hardcoding 1 and 100, fixed attempts to start at 0 instead of 1

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It removed the -5 score deduction on each attempt which I think was supposed to stay. It also did not fix the attempt limit to accurately reflect the difficulty. I just checked the code.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Testing the game again and checking if the print statements correspond to the correct action. I also asked it to write pytests and ran them.

- Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.
I reloaded the streamlit website and played a game and verified the visuals that should be fixed.

- Did AI help you design or understand any tests? How?
It added 18 tests to pytests with code explaining what bug each test tests and the expected outputs. It also helped me refactor my code inside logic_utils to have cleaner logic and code design.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
reruns are when the website is reloaded, meaning that the code is run top to bottom and everything is "forgotten". In this case, it gives you a new number and resets the attempts and score. A similar example would be if you are in the middle of playing a non-online game (e.g. RPGs, multiplayer game) without saving, you could lose your progress. A session state establishes that memory that allows you to save a part, or called variables, you would like between reruns. An example is saving the score, the secret number, and the attempts.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Be more focused with my prompts and make it write tests for code that I understand and write.

- What is one thing you would do differently next time you work with AI on a coding task?
Visually read the code myself to confirm, always test the code at runtime. I would also be a lot more specific so the AI is more focused.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Before, I tend to rely on it to code and trusted it a lot more, but now, I will use it more as a planner and use documentation to verify AI code before implementing it.