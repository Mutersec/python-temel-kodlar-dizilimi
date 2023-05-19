import random

def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

#Developer:Muter
#Discord:https://discord.gg/WRWEk6jKG7

#Bu kodda, farklı işlevlere sahip fonksiyonlar bulunmaktadır. generate_random_password() rastgele bir şifre oluşturur, calculate_average() bir sayı listesinin ortalamasını hesaplar, is_prime() bir sayının asal olup olmadığını kontrol eder, reverse_string() bir metni tersine çevirir, fibonacci_sequence() Fibonacci dizisini oluşturur, factorial() bir sayının faktöriyelini hesaplar, bubble_sort() bir sayı listesini kabarcık sıralama yöntemiyle sıralar, binary_search() bir sayı listesinde hedefi arar, find_largest() bir sayı listesindeki en büyük sayıyı bulur, ve count_vowels() bir metindeki sesli harflerin sayısını sayar.