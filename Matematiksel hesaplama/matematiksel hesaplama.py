import math
import datetime
import random

# Fonksiyonlar

def calculate_circle_area(radius):
    return math.pi * radius**2

def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def roll_dice(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        rolls.append(random.randint(1, 6))
    return rolls

def encrypt_caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def is_palindrome(word):
    reversed_word = word[::-1]
    return word.lower() == reversed_word.lower()

def calculate_factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial_recursive(n - 1)

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def sort_list(numbers):
    return sorted(numbers)


#Developer:Muter
#Discord:https://discord.gg/WRWEk6jKG7