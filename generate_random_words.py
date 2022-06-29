import random
import string


def random_words(words=10):
    letters = string.ascii_letters
    text = ""
    for word in range(words):
        x = "".join(random.sample(letters, random.randint(1, 10)))
        text += x + " "

    return (text.capitalize()+".")

print(random_words(100))