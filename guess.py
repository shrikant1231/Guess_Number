import random
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak your guess:")
        audio = recognizer.listen(source)

        try:
            guess = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {guess}")
            return int(guess)
        except sr.UnknownValueError:
            print("😕 Sorry, I could not understand. Try again.")
            return None
        except sr.RequestError:
            print("⚠️ Could not request results. Check your internet.")
            return None
        except ValueError:
            print("🚫 That doesn't seem like a number.")
            return None

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    low = 1
    high = 100

    print("🎲 Welcome to the Voice-Driven Number Guessing Game!")
    print("🎯 I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_voice_input()
        if guess is None:
            continue

        attempts += 1
        if guess == number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print("📉 Too low!")
            low = max(low, guess + 1)
        else:
            print("📈 Too high!")
            high = min(high, guess - 1)

        hint = (low + high) // 2
        print(f"💡 AI Hint: Try around {hint}")

number_guessing_game()
