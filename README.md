# Wordle Game AI Bot
## Description
This project is a Python-based AI bot that plays Wordle games using an external API. The bot can choose different games and attempt to solve wordle automatically through strategic guessing.

## Usage
Run the `ai_bot.py` script using Python.
Follow the on-screen instructions to choose and play different Wordle games: Daily Guess, Random Guess, Word Guess.

## Approach and Development Process
### Initial Planning and API Understanding
Project goals: Build an AI bot capable of automatically solving wordle game by using API feedback. 

### Architecture
![image](https://github.com/user-attachments/assets/31a8a7f8-b0fb-4bac-ae37-ac28ddb6d31e)

- **API Client**: Handles communication with the Wordle API
- **AI Bot**: Controls main logic and manages game flow
- **Refining Solver**: Based feedback from API to refine words

### API Specification:
#### API endpoints:
- `/daily`: Interact with a daily wordle.
- `/random`: Guess against a random word, with the addition of an optional "seed" parameter for randomness control.
- `/word/{word}`: We can replace `{word}` with the word you want to guess against and supply your "guess" as a query parameter.

#### Components:
- **GuessResult**: Each result will have a `slot`, `guess`, and `result`. The `result` will indicate if your guess was `absent`, `present`, or `correct`.
- **HTTPValidationError**: Describes the format of an error in case your request is not valid.
- **ValidationError**: Details on validation errors including location, message, and error type.

### Design AI Bot
1. Start with an initial word (the length of word is equal to the wordle `size`)
2. Iteratively refining each letter based on feedback: 
    - For `absent`: Remove these letters.
    - For `correct`: Keep letters in the exact position.
    - For `present`: Place the letter in alternative positions, excluding the given position.
3. Iterate guesses based on feedback, modifying one letter at a time with strategic adjustment. This approach uses a more strategic guessing method similar to what human players might do

## Implementation
### Environment Setup
Set up the Python environment in VS code. Based on API doc, I determined the use of the “requests” library to handle HTTP requests for API interaction.

### API Integration
Developed functions to manage GET requests to each endpoint (`/daily`, `/random`, and `/word/{word}`), passing the parameters including `guess`, `size`, `word`, handle responses, and extract meaningful results as `response.json`.
Conducted test cases via `test_api_endpoints()` with initial guess "apple" verifying HTTP responses and diagnosing issues via response.status_code. For example, I set "apple" as target word in Guess Word Game, and the outputs as below:
`Status Code: 200 Response`


      [
          {
              "slot": 0,
              "guess": "a",
              "result": "correct"
          },
          {
              "slot": 1,
              "guess": "p",
              "result": "correct"
          },
          {
              "slot": 2,
              "guess": "p",
              "result": "correct"
          },
          {
              "slot": 3,
              "guess": "l",
              "result": "correct"
          },
          {
              "slot": 4,
              "guess": "e",
              "result": "correct"
          }
      ]

### Implement the AI Logic
- To begin with word_guess, because we can select word as the target and easily to test and verify outputs of implementation.
- Processed initial guess word to get GuessResult. 
- Mapped guesses to feedback and refine guesses.
- Implemented new guessing strategies, including letter-by-letter refinement for increased accuracy and efficiency. 
- Iteratively refined the AI logic: Focused on incrementally improving guesses based on "correct," "present," and "absent" feedback.

## Testing and Iteration:
- Conducted testing with different target words, seeds, and wordle types to validate correctness and robustness.
- Utilized feedback loops to identify potential improvements, such as constraint adjustments and seed control for random games.

## User Interaction Enhancement:
- Developed a function to allow users to select wordle modes interactively, enhancing user engagement and customization.
- Ensured the user interface (CLI) in terminal was clear and provided helpful prompts and feedback.
