import secrets
import string

def generate_password(length=12, include_symbols=True):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

length = 20  # Şifre uzunluğu
include_symbols = True  # Noktalama işaretlerini içersin mi?

password = generate_password(length, include_symbols)
print("Ronesa Oluşturulan şifre:", password)
print("———————————————————————————")
print("Discord sunucumuza beklerim")