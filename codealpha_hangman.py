import random
words = ["python", "java", "coding", "computer", "program"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []
print("Welcome to Hangman Game!")
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", used_letters)
    guess = input("Enter a letter: ").lower()
    if guess in used_letters:
        continue
    used_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
if "_" not in guessed:
    print("You guessed the word:", word)
else:
    print("The guess is wrong and word was:", word)