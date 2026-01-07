Sherlock Holmes 5-Gram Language Model

This repository contains an implementation of a 5-gram Language Model trained on the works of Sir Arthur Conan Doyle, a collection of Sherlock Holmes stories.

This project was created as part of an assignment to demonstrate N-gram language modeling and text generation in the style of a chosen author.

I chose Arthur Conan Doyle as the author for this project.

Why Arthur Conan Doyle?
 well he is known for Suspenseful & Engaging Storytelling , This makes the generated text especially interesting to analyse.
 
What This Project Does?
This project trains a 5-gram language model, meaning the probability of a word is based on the four words before it. The model is then used to generate new Sherlock-style sentences.

Project Structure
src/
 ├── model.py      # NGramLanguageModel class
 └── main.py       # Main script to train & generate text

data/
 └── sherlock.txt  # Training corpus

Code Brief
model.py

Contains the NGramLanguageModel class with:

preprocess(text)
Cleans text (lowercasing, removing non-alphabetic characters except periods)

train(text)
Builds the N-gram probability model using nested dictionaries to count word-sequence frequencies

generate(seed_text, max_words)
Generates new text using the last n-1 = 4 words to predict the next word

main.py

This is the entry point of the program. It:

✔ Loads the training data from data/sherlock.txt
✔ Initializes the model with n = 5
✔ Trains the model
✔ Generates text for sample prompts

How to Run

Make sure Python is installed

Go to the project folder

Run:

python src/main.py

OUTPUTS:
Sample 1
Input Text : the day was very
Output Text: the day was very would me.

Sample 2
Input Text : i could not help
Output Text: i could not help laughing at the ease with which he explained his process of deduction.

Sample 3
Input Text : it was a singular
Output Text: it was a singular document.

Sample 4
Input Text : holmes looked at me
Output Text: holmes looked at me languor by seemed to its how shall in which interested again i your man what whole little kind and the chain this holmes you stated said do even all and seven the from a until if she heavy wrote without

Sample 5
Input Text : there was a man
Output Text: there was a man a a fourteen other we face last as his unlike before the must mailboat you turned it rest nostrils to run one of find light intelligence turner make sit and as side.

***Predictions may vary slightly each run because the model is probabilistic
